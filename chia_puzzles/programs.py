from chia_puzzles.load_clvm import load_clvm_bytes

chialisp_dictionary = [
        # CAT Puzzles
        ("CAT_PUZZLE", "chia_puzzles.puzzles.cat_puzzles", "cat_v2.clsp"),
        ("DELEGATED_TAIL", "chia_puzzles.puzzles.cat_puzzles", "delegated_tail.clsp"),
        ("EVERYTHING_WITH_SIGNATURE", "chia_puzzles.puzzles.cat_puzzles", "everything_with_signature.clsp"),
        ("GENESIS_BY_COIN_ID_OR_SINGLETON", "chia_puzzles.puzzles.cat_puzzles", "genesis_by_coin_id_or_singleton.clsp"),
        ("GENESIS_BY_COIN_ID", "chia_puzzles.puzzles.cat_puzzles", "genesis_by_coin_id.clsp"),
        ("GENESIS_BY_PUZZLE_HASH", "chia_puzzles.puzzles.cat_puzzles", "genesis_by_puzzle_hash.clsp"),
        # DAO Puzzles
        ("DAO_CAT_EVE", "chia_puzzles.puzzles.dao_puzzles", "dao_cat_eve.clsp"),
        ("DAO_CAT_LAUNCHER", "chia_puzzles.puzzles.dao_puzzles", "dao_cat_launcher.clsp"),
        ("DAO_FINISHED_STATE", "chia_puzzles.puzzles.dao_puzzles", "dao_finished_state.clsp"),
        ("DAO_LOCKUP", "chia_puzzles.puzzles.dao_puzzles", "dao_lockup.clsp"),
        ("DAO_PROPOSAL_TIMER", "chia_puzzles.puzzles.dao_puzzles", "dao_proposal_timer.clsp"),
        ("DAO_PROPOSAL_VALIDATOR", "chia_puzzles.puzzles.dao_puzzles", "dao_proposal_validator.clsp"),
        ("DAO_PROPOSAL", "chia_puzzles.puzzles.dao_puzzles", "dao_proposal.clsp"),
        ("DAO_SPEND_P2_SINGLETON", "chia_puzzles.puzzles.dao_puzzles", "dao_spend_p2_singleton_v2.clsp"),
        ("DAO_TREASURY", "chia_puzzles.puzzles.dao_puzzles", "dao_treasury.clsp"),
        ("DAO_UPDATE_PROPOSAL", "chia_puzzles.puzzles.dao_puzzles", "dao_update_proposal.clsp"), 
        # DID Puzzles
        ("DID_INNERPUZ", "chia_puzzles.puzzles.did_puzzles", "did_innerpuz.clsp"),
        # NFT Puzzles
        ("CREATE_NFT_LAUNCHER_FROM_DID", "chia_puzzles.puzzles.nft_puzzles", "create_nft_launcher_from_did.clsp"),
        ("NFT_INTERMEDIATE_LAUNCHER", "chia_puzzles.puzzles.nft_puzzles", "nft_intermediate_launcher.clsp"),
        ("NFT_METADATA_UPDATER_DEFAULT", "chia_puzzles.puzzles.nft_puzzles", "nft_metadata_updater_default.clsp"),
        ("NFT_METADATA_UPDATER_UPDATEABLE", "chia_puzzles.puzzles.nft_puzzles", "nft_metadata_updater_updateable.clsp"),
        ("NFT_OWNERSHIP_LAYER", "chia_puzzles.puzzles.nft_puzzles", "nft_ownership_layer.clsp"),
        ("NFT_OWNERSHIP_TRANSFER_PROGRAM_ONE_WAY_CLAIM_WITH_ROYALTIES", "chia_puzzles.puzzles.nft_puzzles", "nft_ownership_transfer_program_one_way_claim_with_royalties.clsp"),
        ("NFT_STATE_LAYER", "chia_puzzles.puzzles.nft_puzzles", "nft_state_layer.clsp"),
        # CR Puzzles
        ("CONDITIONS_W_FEE_ANNOUNCE", "chia_puzzles.puzzles.vc_puzzles.cr_puzzles", "conditions_w_fee_announce.clsp"),
        ("CREDENTIAL_RESTRICTION", "chia_puzzles.puzzles.vc_puzzles.cr_puzzles", "credential_restriction.clsp"),
        ("FLAG_PROOFS_CHECKER", "chia_puzzles.puzzles.vc_puzzles.cr_puzzles", "flag_proofs_checker.clsp"),
        # VC Puzzles
        ("COVENANT_LAYER", "chia_puzzles.puzzles.vc_puzzles", "covenant_layer.clsp"),
        ("EML_COVENANT_MORPHER", "chia_puzzles.puzzles.vc_puzzles", "eml_covenant_morpher.clsp"),
        ("EML_TRANSFER_PROGRAM_COVENANT_ADAPTER", "chia_puzzles.puzzles.vc_puzzles", "eml_transfer_program_covenant_adapter.clsp"),
        ("EML_UPDATE_METADATA_WITH_DID", "chia_puzzles.puzzles.vc_puzzles", "eml_update_metadata_with_DID.clsp"),
        ("EXIGENT_METADATA_LAYER", "chia_puzzles.puzzles.vc_puzzles", "exigent_metadata_layer.clsp"),
        ("P2_ANNOUNCED_DELEGATED_PUZZLE", "chia_puzzles.puzzles.vc_puzzles", "p2_announced_delegated_puzzle.clsp"),
        ("STANDARD_VC_BACKDOOR_PUZZLE", "chia_puzzles.puzzles.vc_puzzles", "standard_vc_backdoor_puzzle.clsp"),
        ("STD_PARENT_MORPHER", "chia_puzzles.puzzles.vc_puzzles", "std_parent_morpher.clsp"),
        ("VIRAL_BACKDOOR", "chia_puzzles.puzzles.vc_puzzles", "viral_backdoor.clsp"),
        # Misc Puzzles
        ("AUGMENTED_CONDITION", "chia_puzzles.puzzles", "augmented_condition.clsp"),
        ("NOTIFICATION", "chia_puzzles.puzzles", "notification.clsp"),
        ("P2_1_OF_N", "chia_puzzles.puzzles", "p2_1_of_n.clsp"),
        ("P2_CONDITIONS", "chia_puzzles.puzzles", "p2_conditions.clsp"),
        ("P2_DELEGATED_CONDITIONS", "chia_puzzles.puzzles", "p2_delegated_conditions.clsp"),
        ("P2_DELEGATED_PUZZLE_OR_HIDDEN_PUZZZLE", "chia_puzzles.puzzles", "p2_delegated_puzzle_or_hidden_puzzle.clsp"),
        ("P2_DELEGATED_PUZZLE", "chia_puzzles.puzzles", "p2_delegated_puzzle.clsp"),
        ("P2_M_OF_N_DELEGATE_DIRECT", "chia_puzzles.puzzles", "p2_m_of_n_delegate_direct.clsp"),
        ("P2_PARENT", "chia_puzzles.puzzles", "p2_parent.clsp"),
        ("P2_SINGLETON_AGGREGATOR", "chia_puzzles.puzzles", "p2_singleton_aggregator.clsp"),
        ("P2_SINGLETON_OR_DELAYED_PUZHASH", "chia_puzzles.puzzles", "p2_singleton_or_delayed_puzhash.clsp"),
        ("P2_SINGLETON_VIA_DELEGATED_PUZZLE", "chia_puzzles.puzzles", "p2_singleton_via_delegated_puzzle.clsp"),
        ("P2_SINGLETON", "chia_puzzles.puzzles", "p2_singleton.clsp"),
        ("SETTLEMENT_PAYMENT", "chia_puzzles.puzzles", "settlement_payments.clsp"),
        # Singleton Puzzle
        ("SINGLETON_LAUNCHER", "chia_puzzles.puzzles", "singleton_launcher.clsp"),
        ("SINGLETON_TOP_LAYER_V1_1", "chia_puzzles.puzzles", "singleton_top_layer_v1_1.clsp"),
        ("SINGLETON_TOP_LAYER", "chia_puzzles.puzzles", "singleton_top_layer.clsp"),
    ]

for (name, package_path, filename) in chialisp_dictionary:
     globals()[name] = load_clvm_bytes(filename, package_or_requirement=package_path)