from chia.wallet.puzzles.load_clvm import load_clvm_maybe_recompile

GENESIS_BY_ID_MOD = load_clvm_maybe_recompile(
    "genesis_by_coin_id.clsp", package_or_requirement="chia.wallet.cat_wallet.puzzles"
)
GENESIS_BY_PUZHASH_MOD = load_clvm_maybe_recompile(
    "genesis_by_puzzle_hash.clsp", package_or_requirement="chia.wallet.cat_wallet.puzzles"
)
EVERYTHING_WITH_SIG_MOD = load_clvm_maybe_recompile(
    "everything_with_signature.clsp", package_or_requirement="chia.wallet.cat_wallet.puzzles"
)
DELEGATED_LIMITATIONS_MOD = load_clvm_maybe_recompile(
    "delegated_tail.clsp", package_or_requirement="chia.wallet.cat_wallet.puzzles"
)
GENESIS_BY_ID_OR_SINGLETON_MOD = load_clvm_maybe_recompile(
    "genesis_by_coin_id_or_singleton.clsp", package_or_requirement="chia.wallet.cat_wallet.puzzles"
)
