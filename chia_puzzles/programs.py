from chia_puzzles.load_clvm import load_clvm_bytes

GENESIS_BY_ID_MOD = load_clvm_bytes(
    "genesis_by_coin_id.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles"
)
GENESIS_BY_PUZHASH_MOD = load_clvm_bytes(
    "genesis_by_puzzle_hash.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles"
)
EVERYTHING_WITH_SIG_MOD = load_clvm_bytes(
    "everything_with_signature.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles"
)
DELEGATED_LIMITATIONS_MOD = load_clvm_bytes(
    "delegated_tail.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles"
)
GENESIS_BY_ID_OR_SINGLETON_MOD = load_clvm_bytes(
    "genesis_by_coin_id_or_singleton.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles"
)
