import os
from pathlib import Path

# Define the Chialisp dictionary
chialisp_dictionary = [
        # CAT Puzzles
        ("CAT_PUZZLE", "./puzzles/cat_puzzles/cat_v2.clsp.hex"),
        ("DELEGATED_TAIL", "./puzzles/cat_puzzles/delegated_tail.clsp.hex"),
        ("EVERYTHING_WITH_SIGNATURE", "./puzzles/cat_puzzles/everything_with_signature.clsp.hex"),
        ("GENESIS_BY_COIN_ID_OR_SINGLETON", "./puzzles/cat_puzzles/genesis_by_coin_id_or_singleton.clsp.hex"),
        ("GENESIS_BY_COIN_ID", "./puzzles/cat_puzzles/genesis_by_coin_id.clsp.hex"),
        ("GENESIS_BY_PUZZLE_HASH", "./puzzles/cat_puzzles/genesis_by_puzzle_hash.clsp.hex"),
        # DAO Puzzles
        ("DAO_CAT_EVE", "./puzzles/dao_puzzles/dao_cat_eve.clsp.hex"),
        ("DAO_CAT_LAUNCHER", "./puzzles/dao_puzzles/dao_cat_launcher.clsp.hex"),
        ("DAO_FINISHED_STATE", "./puzzles/dao_puzzles/dao_finished_state.clsp.hex"),
        ("DAO_LOCKUP", "./puzzles/dao_puzzles/dao_lockup.clsp.hex"),
        ("DAO_PROPOSAL_TIMER", "./puzzles/dao_puzzles/dao_proposal_timer.clsp.hex"),
        ("DAO_PROPOSAL_VALIDATOR", "./puzzles/dao_puzzles/dao_proposal_validator.clsp.hex"),
        ("DAO_PROPOSAL", "./puzzles/dao_puzzles/dao_proposal.clsp.hex"),
        ("DAO_SPEND_P2_SINGLETON", "./puzzles/dao_puzzles/dao_spend_p2_singleton_v2.clsp.hex"),
        ("DAO_TREASURY", "./puzzles/dao_puzzles/dao_treasury.clsp.hex"),
        ("DAO_UPDATE_PROPOSAL", "./puzzles/dao_puzzles/dao_update_proposal.clsp.hex"), 
        # DID Puzzles
        ("DID_INNERPUZ", "./puzzles/did_puzzles/did_innerpuz.clsp.hex"),
        # NFT Puzzles
        ("CREATE_NFT_LAUNCHER_FROM_DID", "./puzzles/nft_puzzles/create_nft_launcher_from_did.clsp.hex"),
        ("NFT_INTERMEDIATE_LAUNCHER", "./puzzles/nft_puzzles/nft_intermediate_launcher.clsp.hex"),
        ("NFT_METADATA_UPDATER_DEFAULT", "./puzzles/nft_puzzles/nft_metadata_updater_default.clsp.hex"),
        ("NFT_METADATA_UPDATER_UPDATEABLE", "./puzzles/nft_puzzles/nft_metadata_updater_updateable.clsp.hex"),
        ("NFT_OWNERSHIP_LAYER", "./puzzles/nft_puzzles/nft_ownership_layer.clsp.hex"),
        ("NFT_OWNERSHIP_TRANSFER_PROGRAM_ONE_WAY_CLAIM_WITH_ROYALTIES", "./puzzles/nft_puzzles/nft_ownership_transfer_program_one_way_claim_with_royalties.clsp.hex"),
        ("NFT_STATE_LAYER", "./puzzles/nft_puzzles/nft_state_layer.clsp.hex"),
        # CR Puzzles
        ("CONDITIONS_W_FEE_ANNOUNCE", "./puzzles/vc_puzzles/cr_puzzles/conditions_w_fee_announce.clsp.hex"),
        ("CREDENTIAL_RESTRICTION", "./puzzles/vc_puzzles/cr_puzzles/credential_restriction.clsp.hex"),
        ("FLAG_PROOFS_CHECKER", "./puzzles/vc_puzzles/cr_puzzles/flag_proofs_checker.clsp.hex"),
        # VC Puzzles
        ("COVENANT_LAYER", "./puzzles/vc_puzzles/covenant_layer.clsp.hex"),
        ("EML_COVENANT_MORPHER", "./puzzles/vc_puzzles/eml_covenant_morpher.clsp.hex"),
        ("EML_TRANSFER_PROGRAM_COVENANT_ADAPTER", "./puzzles/vc_puzzles/eml_transfer_program_covenant_adapter.clsp.hex"),
        ("EML_UPDATE_METADATA_WITH_DID", "./puzzles/vc_puzzles/eml_update_metadata_with_DID.clsp.hex"),
        ("EXIGENT_METADATA_LAYER", "./puzzles/vc_puzzles/exigent_metadata_layer.clsp.hex"),
        ("P2_ANNOUNCED_DELEGATED_PUZZLE", "./puzzles/vc_puzzles/p2_announced_delegated_puzzle.clsp.hex"),
        ("STANDARD_VC_BACKDOOR_PUZZLE", "./puzzles/vc_puzzles/standard_vc_backdoor_puzzle.clsp.hex"),
        ("STD_PARENT_MORPHER", "./puzzles/vc_puzzles/std_parent_morpher.clsp.hex"),
        ("VIRAL_BACKDOOR", "./puzzles/vc_puzzles/viral_backdoor.clsp.hex"),
        # Misc Puzzles
        ("AUGMENTED_CONDITION", "./puzzles/augmented_condition.clsp.hex"),
        ("NOTIFICATION", "./puzzles/notification.clsp.hex"),
        ("P2_1_OF_N", "./puzzles/p2_1_of_n.clsp.hex"),
        ("P2_CONDITIONS", "./puzzles/p2_conditions.clsp.hex"),
        ("P2_DELEGATED_CONDITIONS", "./puzzles/p2_delegated_conditions.clsp.hex"),
        ("P2_DELEGATED_PUZZLE_OR_HIDDEN_PUZZZLE", "./puzzles/p2_delegated_puzzle_or_hidden_puzzle.clsp.hex"),
        ("P2_DELEGATED_PUZZLE", "./puzzles/p2_delegated_puzzle.clsp.hex"),
        ("P2_M_OF_N_DELEGATE_DIRECT", "./puzzles/p2_m_of_n_delegate_direct.clsp.hex"),
        ("P2_PARENT", "./puzzles/p2_parent.clsp.hex"),
        ("P2_SINGLETON_AGGREGATOR", "./puzzles/p2_singleton_aggregator.clsp.hex"),
        ("P2_SINGLETON_OR_DELAYED_PUZHASH", "./puzzles/p2_singleton_or_delayed_puzhash.clsp.hex"),
        ("P2_SINGLETON_VIA_DELEGATED_PUZZLE", "./puzzles/p2_singleton_via_delegated_puzzle.clsp.hex"),
        ("P2_SINGLETON", "./puzzles/p2_singleton.clsp.hex"),
        ("SETTLEMENT_PAYMENT", "./puzzles/settlement_payments.clsp.hex"),
        # Singleton Puzzle
        ("SINGLETON_LAUNCHER", "./puzzles/singleton_launcher.clsp.hex"),
        ("SINGLETON_TOP_LAYER_V1_1", "./puzzles/singleton_top_layer_v1_1.clsp.hex"),
        ("SINGLETON_TOP_LAYER", "./puzzles/singleton_top_layer.clsp.hex"),
    ]

# File paths for generated files
rust_dest_path = Path("./src/loaded_chialisp.rs")
python_dest_path = Path("./chia_puzzles_py/programs.py")

# Ensure the output directory exists
os.makedirs(rust_dest_path.parent, exist_ok=True)
os.makedirs(python_dest_path.parent, exist_ok=True)

with open(rust_dest_path, "w") as rust_file, open(python_dest_path, "w") as python_file:
    python_file.write("# Auto-generated Python file with loaded Chialisp constants\n\n")
    rust_file.write("// Auto-generated Rust file with loaded Chialisp constants\n\n")

    for name, file_path in chialisp_dictionary:
        try:
            with open(file_path, "r") as hex_file:
                hex_data = hex_file.read().strip().replace("\n", "").replace("\r", "")

            bytes_data = bytes.fromhex(hex_data)

            rust_byte_array_string = ", ".join(f"0x{byte:02x}" for byte in bytes_data)
            rust_file.write(
                f"pub const {name}: [u8; {len(bytes_data)}] = [{rust_byte_array_string}];\n"
            )

            python_bytes_literal = "".join(f"\\x{byte:02x}" for byte in bytes_data)
            python_file.write(
                f"{name} = b\"{python_bytes_literal}\"\n"
            )

            print(f"Processed {name} from {file_path}")

        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception:
            print(f"Failed to decode hex data in file: {file_path}")

print(f"Rust and Python files generated successfully:\n- {rust_dest_path}\n- {python_dest_path}")
