# Chia Puzzles

This is a collection of the standard Chia puzzles.
These are the puzzles which are deployed on chain and therefore cannot change.

This repository tracks the source code, the compiled hex, and a hash of the compiled hex to ensure continuity.

All puzzles are kept in the `puzzles` folder as both a `.clsp` and `.clsp.hex` file.

The Python and Rust bindings are created by running `generate_chialisp_constants.py`

# Testing

This project is managed with `uv` for Python and `cargo` for Rust.

To run the Python tests:
```
pip install uv
uv venv
. ./venv/bin/activate
uv sync
uv run pytest chia_puzzles_py/tests
```
If you're on Windows activate the venv with `.venv\Scripts\activate` instead

To run the Rust tests:
```
cargo test --all
```