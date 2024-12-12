from chia_puzzles_py.programs import CAT_PUZZLE, SINGLETON_TOP_LAYER


def test_import_CAT_PUZZLE():
    assert CAT_PUZZLE is not None
    assert SINGLETON_TOP_LAYER is not None
