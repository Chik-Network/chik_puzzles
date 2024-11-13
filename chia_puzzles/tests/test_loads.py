import json
import os
import pathlib
import tempfile
import traceback
import typing

import pytest
from chia_puzzles.load_clvm import compile_clvm
from chia_puzzles.programs import CAT_PUZZLE
from chia_puzzles.manage_clvm import Cache, ClvmBytes, ClvmPaths, ManageClvmError, create_cache_entry, create_empty_cache, dump_cache, find_stems, load_cache

here = pathlib.Path(__file__).parent.resolve()
root = here.parent
cache_path = root.joinpath(".chia_cache", "manage_clvm.json")
# Suffixes and path definitions
clvm_suffix = ".clvm"
clsp_suffix = ".clsp"
hex_suffix = ".clsp.hex"
all_suffixes = {"clsp": clsp_suffix, "hex": hex_suffix, "clvm": clvm_suffix}
top_levels = {"chia_puzzles"}
hashes_path = root.joinpath("chia-puzzles/deployed_puzzle_hashes.json")
std_libraries = root.joinpath("puzzles")

excludes: typing.Set[str] = set()

CacheVersion = typing.List[int]

class CacheVersionError(ManageClvmError):
    pass


class NoCacheVersionError(CacheVersionError):
    def __init__(self) -> None:
        super().__init__("Cache must specify a version, none found")


class WrongCacheVersionError(CacheVersionError):
    def __init__(self, found_version: object, expected_version: CacheVersion) -> None:
        self.found_version = found_version
        self.expected_version = expected_version
        super().__init__(f"Cache has wrong version, expected {expected_version!r} got: {found_version!r}")


def test_import():
    assert CAT_PUZZLE is not None

@pytest.mark.parametrize(
        "use_cache",
        [True, False],
    )
def test_check(use_cache: bool) -> int:
    used_excludes = set()
    overall_fail = False

    HASHES: typing.Dict[str, str] = json.loads(hashes_path.read_text()) if hashes_path.exists() else {}

    cache: Cache
    if not use_cache:
        cache = create_empty_cache()
    else:
        try:
            print(f"Attempting to load cache from: {cache_path}")
            with cache_path.open(mode="r") as file:
                cache = load_cache(file=file)
        except FileNotFoundError:
            print("Cache not found, starting fresh")
            cache = create_empty_cache()
        except NoCacheVersionError:
            print("Ignoring cache due to lack of version")
            cache = create_empty_cache()
        except WrongCacheVersionError as e:
            print(f"Ignoring cache due to incorrect version, expected {e.expected_version!r} got: {e.found_version!r}")
            cache = create_empty_cache()

    cache_entries = cache["entries"]
    cache_modified = False

    found_stems = find_stems(top_levels)
    assert len(found_stems["hex"]) > 20
    found = found_stems["hex"]
    suffix = all_suffixes["hex"]
    extra = found - found_stems["clsp"]

    print()
    print(f"Extra {suffix} files:")

    if len(extra) == 0:
        print("    -")
    else:
        overall_fail = True
        for stem in extra:
            print(f"    {stem.with_name(stem.name + suffix)}")

    print()
    print("Checking that no .clvm files begin with `(mod`")
    for stem_path in sorted(found_stems["clvm"]):
        with open(stem_path.with_name(stem_path.name + clvm_suffix)) as file:
            file_lines = file.readlines()
            for line in file_lines:
                non_comment: str = line.split(";")[0]
                if "(" in non_comment:
                    paren_index: int = non_comment.find("(")
                    if len(non_comment) >= paren_index + 4 and non_comment[paren_index : paren_index + 4] == "(mod":
                        overall_fail = True
                        print(f"FAIL    : {stem_path.name + clvm_suffix} contains `(mod`")
                    break
    
    missing_files: typing.List[str] = []
    all_hash_stems: typing.List[str] = []

    print()
    print("Checking that all existing .clsp files compile to .clsp.hex that match existing caches:")
    for stem_path in sorted(found_stems["clsp"]):
        clsp_path = stem_path.with_name(stem_path.name + clsp_suffix)
        if clsp_path.name in excludes:
            used_excludes.add(clsp_path.name)
            continue

        file_fail = False
        error = None

        cache_key = str(stem_path)
        try:
            reference_paths = ClvmPaths.from_clvm(clvm=clsp_path, hash_dict=HASHES)
            if reference_paths.missing_files != []:
                missing_files.extend(reference_paths.missing_files)
                continue
            all_hash_stems.append(reference_paths.hash)
            reference_bytes = ClvmBytes.from_clvm_paths(paths=reference_paths, hash_dict=HASHES)

            new_cache_entry = create_cache_entry(reference_paths=reference_paths, reference_bytes=reference_bytes)
            existing_cache_entry = cache_entries.get(cache_key)
            cache_hit = new_cache_entry == existing_cache_entry

            if not cache_hit:
                with tempfile.TemporaryDirectory() as temporary_directory:
                    generated_paths = ClvmPaths.from_clvm(
                        clvm=pathlib.Path(temporary_directory).joinpath(reference_paths.clvm.name),
                        hash_dict=HASHES,
                    )
                    compile_clvm(
                        full_path=os.fspath(reference_paths.clvm),
                        output=os.fspath(generated_paths.hex),
                        search_paths=[os.fspath(reference_paths.clvm.parent), str(std_libraries)],
                    )

                    generated_bytes = ClvmBytes.from_hex_bytes(hex_bytes=generated_paths.hex.read_bytes())

                if generated_bytes != reference_bytes:
                    file_fail = True
                    error = f"        reference: {reference_bytes!r}\n"
                    error += f"        generated: {generated_bytes!r}"
                else:
                    cache_modified = True
                    cache_entries[cache_key] = new_cache_entry
        except Exception:
            file_fail = True
            error = traceback.format_exc()

        if file_fail:
            print(f"FAIL    : {clsp_path}")
            if error is not None:
                print(error)
        else:
            print(f"    pass: {clsp_path}")

        if file_fail:
            overall_fail = True

    if missing_files != []:
        overall_fail = True
        print()
        print("Missing files (run tools/manage_clvm.py build to build them):")
        for filename in missing_files:
            print(f" - {filename}")

    unused_excludes = sorted(excludes - used_excludes)
    if len(unused_excludes) > 0:
        overall_fail = True
        print()
        print("Unused excludes:")

        for exclude in unused_excludes:
            print(f"    {exclude}")

    extra_hashes = HASHES.keys() - all_hash_stems
    if len(extra_hashes) != 0:
        overall_fail = True
        print()
        print("Hashes without corresponding files:")
        for extra_hash in extra_hashes:
            print(f"    {extra_hash}")

    if use_cache and cache_modified:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        with cache_path.open(mode="w") as file:
            dump_cache(cache=cache, file=file)
    
    assert not overall_fail