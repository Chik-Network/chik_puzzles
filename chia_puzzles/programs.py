from chia_puzzles.load_clvm import load_clvm_bytes

# CAT Puzzles
CAT_PUZZLE = load_clvm_bytes("cat_v2.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles")
DELEGATED_TAIL = load_clvm_bytes("delegated_tail.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles")
EVERYTHING_WITH_SIGNATURE = load_clvm_bytes("everything_with_signature.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles")
GENESIS_BY_COIN_ID_OR_SINGLETON = load_clvm_bytes("genesis_by_coin_id_or_singleton.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles")
GENESIS_BY_COIN_ID = load_clvm_bytes("genesis_by_coin_id.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles")
GENESIS_BY_PUZZLE_HASH = load_clvm_bytes("genesis_by_puzzle_hash.clsp", package_or_requirement="chia_puzzles.puzzles.cat_puzzles")

# DAO Puzzles
DAO_CAT_EVE = load_clvm_bytes("dao_cat_eve.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_CAT_LAUNCHER = load_clvm_bytes("dao_cat_launcher.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_FINISHED_STATE = load_clvm_bytes("dao_finished_state.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_LOCKUP = load_clvm_bytes("dao_lockup.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_PROPOSAL_TIMER = load_clvm_bytes("dao_proposal_timer.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_PROPOSAL_VALIDATOR = load_clvm_bytes("dao_proposal_validator.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_PROPOSAL = load_clvm_bytes("dao_proposal.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_SPEND_P2_SINGLETON = load_clvm_bytes("dao_spend_p2_singleton_v2.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_TREASURY = load_clvm_bytes("dao_treasury.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")
DAO_UPDATE_PROPOSAL = load_clvm_bytes("dao_update_proposal.clsp", package_or_requirement="chia_puzzles.puzzles.dao_puzzles")

# DID Puzzles
DID_INNERPUZ = load_clvm_bytes("did_innerpuz.clsp", package_or_requirement="chia_puzzles.puzzles.did_puzzles")

# NFT Puzzles
CREATE_NFT_LAUNCHER_FROM_DID = load_clvm_bytes("create_nft_launcher_from_did.clsp", package_or_requirement="chia_puzzles.puzzles.nft_puzzles")
NFT_INTERMEDIATE_LAUNCHER = load_clvm_bytes("nft_intermediate_launcher.clsp", package_or_requirement="chia_puzzles.puzzles.nft_puzzles")
NFT_METADATA_UPDATER_DEFAULT = load_clvm_bytes("nft_metadata_updater_default.clsp", package_or_requirement="chia_puzzles.puzzles.nft_puzzles")
NFT_METADATA_UPDATER_UPDATEABLE = load_clvm_bytes("nft_metadata_updater_updateable.clsp", package_or_requirement="chia_puzzles.puzzles.nft_puzzles")
NFT_OWNERSHIP_LAYER = load_clvm_bytes("nft_ownership_layer.clsp", package_or_requirement="chia_puzzles.puzzles.nft_puzzles")
NFT_OWNERSHIP_TRANSFER_PROGRAM_ONE_WAY_CLAIM_WITH_ROYALTIES = load_clvm_bytes("nft_ownership_transfer_program_one_way_claim_with_royalties.clsp", package_or_requirement="chia_puzzles.puzzles.nft_puzzles")
NFT_STATE_LAYER = load_clvm_bytes("nft_state_layer.clsp", package_or_requirement="chia_puzzles.puzzles.nft_puzzles")

# CR Puzzles
CONDITIONS_W_FEE_ANNOUNCE = load_clvm_bytes("conditions_w_fee_announce.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles.cr_puzzles")
CREDENTIAL_RESTRICTION = load_clvm_bytes("credential_restriction.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles.cr_puzzles")
FLAG_PROOFS_CHECKER = load_clvm_bytes("flag_proofs_checker.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles.cr_puzzles")

# VC Puzzles
COVENANT_LAYER = load_clvm_bytes("covenant_layer.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
EML_COVENANT_MORPHER = load_clvm_bytes("eml_covenant_morpher.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
EML_TRANSFER_PROGRAM_COVENANT_ADAPTER = load_clvm_bytes("eml_transfer_program_covenant_adapter.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
EML_UPDATE_METADATA_WITH_DID = load_clvm_bytes("eml_update_metadata_with_DID.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
EXIGENT_METADATA_LAYER = load_clvm_bytes("exigent_metadata_layer.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
P2_ANNOUNCED_DELEGATED_PUZZLE = load_clvm_bytes("p2_announced_delegated_puzzle.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
STANDARD_VC_BACKDOOR_PUZZLE = load_clvm_bytes("standard_vc_backdoor_puzzle.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
STD_PARENT_MORPHER = load_clvm_bytes("std_parent_morpher.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")
VIRAL_BACKDOOR = load_clvm_bytes("viral_backdoor.clsp", package_or_requirement="chia_puzzles.puzzles.vc_puzzles")

# Misc Puzzles
AUGMENTED_CONDITION = load_clvm_bytes("augmented_condition.clsp", package_or_requirement="chia_puzzles.puzzles")
NOTIFICATION = load_clvm_bytes("notification.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_1_OF_N = load_clvm_bytes("p2_1_of_n.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_CONDITIONS = load_clvm_bytes("p2_conditions.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_DELEGATED_CONDITIONS = load_clvm_bytes("p2_delegated_conditions.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_DELEGATED_PUZZLE_OR_HIDDEN_PUZZLE = load_clvm_bytes("p2_delegated_puzzle_or_hidden_puzzle.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_DELEGATED_PUZZLE = load_clvm_bytes("p2_delegated_puzzle.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_M_OF_N_DELEGATE_DIRECT = load_clvm_bytes("p2_m_of_n_delegate_direct.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_PARENT = load_clvm_bytes("p2_parent.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_SINGLETON_AGGREGATOR = load_clvm_bytes("p2_singleton_aggregator.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_SINGLETON_OR_DELAYED_PUZHASH = load_clvm_bytes("p2_singleton_or_delayed_puzhash.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_SINGLETON_VIA_DELEGATED_PUZZLE = load_clvm_bytes("p2_singleton_via_delegated_puzzle.clsp", package_or_requirement="chia_puzzles.puzzles")
P2_SINGLETON = load_clvm_bytes("p2_singleton.clsp", package_or_requirement="chia_puzzles.puzzles")
SETTLEMENT_PAYMENT = load_clvm_bytes("settlement_payments.clsp", package_or_requirement="chia_puzzles.puzzles")

# Singleton Puzzle
SINGLETON_LAUNCHER = load_clvm_bytes("singleton_launcher.clsp", package_or_requirement="chia_puzzles.puzzles")
SINGLETON_TOP_LAYER_V1_1 = load_clvm_bytes("singleton_top_layer_v1_1.clsp", package_or_requirement="chia_puzzles.puzzles")
SINGLETON_TOP_LAYER = load_clvm_bytes("singleton_top_layer.clsp", package_or_requirement="chia_puzzles.puzzles")
