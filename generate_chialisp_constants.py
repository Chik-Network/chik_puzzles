import os
from pathlib import Path
from clvm_tools_rs import compile_clvm
from chia_puzzles_py.manage_clvm import generate_hash_bytes

chialisp_dictionary = [
        # CAT Puzzles
        ("CAT_PUZZLE", "./puzzles/cat_puzzles/cat_v2.clsp.hex", "37bef360ee858133b69d595a906dc45d01af50379dad515eb9518abb7c1d2a7a"),
        ("DELEGATED_TAIL", "./puzzles/cat_puzzles/delegated_tail.clsp.hex", "999c3696e167f8a79d938adc11feba3a3dcb39ccff69a426d570706e7b8ec399"),
        ("EVERYTHING_WITH_SIGNATURE", "./puzzles/cat_puzzles/everything_with_signature.clsp.hex", "1720d13250a7c16988eaf530331cefa9dd57a76b2c82236bec8bbbff91499b89"),
        ("GENESIS_BY_COIN_ID_OR_SINGLETON", "./puzzles/cat_puzzles/genesis_by_coin_id_or_singleton.clsp.hex", "40170305e3a71c3e7523f37fbcfc3188f9f949da0818a6331f28251e76e8c56f"),
        ("GENESIS_BY_COIN_ID", "./puzzles/cat_puzzles/genesis_by_coin_id.clsp.hex", "493afb89eed93ab86741b2aa61b8f5de495d33ff9b781dfc8919e602b2afa150"),
        ("GENESIS_BY_PUZZLE_HASH", "./puzzles/cat_puzzles/genesis_by_puzzle_hash.clsp.hex", "de5a6e06d41518be97ff6365694f4f89475dda773dede267caa33da63b434e36"),
        # DAO Puzzles
        ("DAO_CAT_EVE", "./puzzles/dao_puzzles/dao_cat_eve.clsp.hex", "488f55bedaca5a599544dfd5ab341e2e5c7e6fca67d9b98a3d856f876c52f53e"),
        ("DAO_CAT_LAUNCHER", "./puzzles/dao_puzzles/dao_cat_launcher.clsp.hex", "a01a838d18d4e031e937c79fa3f80f213fa00a3e64af6c16a1f137770cd3a567"),
        ("DAO_FINISHED_STATE", "./puzzles/dao_puzzles/dao_finished_state.clsp.hex", "694c99e1fb07671771bbca3d110880693a9ecc37a6529891ec979d0f3e760eba"),
        ("DAO_LOCKUP", "./puzzles/dao_puzzles/dao_lockup.clsp.hex", "d6215f0916715a69fbbf2d1a679f437fde81787adeb90c666642fb9c2deff7ce"),
        ("DAO_PROPOSAL_TIMER", "./puzzles/dao_puzzles/dao_proposal_timer.clsp.hex", "1acd912fca662d1474f7a6c762280fc1430875bef518883387086c1125027526"),
        ("DAO_PROPOSAL_VALIDATOR", "./puzzles/dao_puzzles/dao_proposal_validator.clsp.hex", "92209b0f7efb2dbaaaa3aab94dcadcafa9d008d39661763841c7d92065b3fd34"),
        ("DAO_PROPOSAL", "./puzzles/dao_puzzles/dao_proposal.clsp.hex", "fe6d5c0373c1750598d137ce50b5b025a203655ccab4ab3329315abad49c3586"),
        ("DAO_SPEND_P2_SINGLETON", "./puzzles/dao_puzzles/dao_spend_p2_singleton_v2.clsp.hex", "7bc8942159e600f56a87e1d9c059c8705307ec2fb996a949503298dedfed00be"),
        ("DAO_TREASURY", "./puzzles/dao_puzzles/dao_treasury.clsp.hex", "637d78acd395b6bb03211bcfc5f5f2e878cba2d62b2f53871d49a8b928411b19"),
        ("DAO_UPDATE_PROPOSAL", "./puzzles/dao_puzzles/dao_update_proposal.clsp.hex" , "fc032384cfece9b542c3e1ea77ba119fb1013a3d74b622302c0b670447e4343d"), 
        # DID Puzzles
        ("DID_INNERPUZ", "./puzzles/did_puzzles/did_innerpuz.clsp.hex", "33143d2bef64f14036742673afd158126b94284b4530a28c354fac202b0c910e"),
        # NFT Puzzles
        ("CREATE_NFT_LAUNCHER_FROM_DID", "./puzzles/nft_puzzles/create_nft_launcher_from_did.clsp.hex", "7a32d2d9571d3436791c0ad3d7fcfdb9c43ace2b0f0ff13f98d29f0cc093f445"),
        ("NFT_INTERMEDIATE_LAUNCHER", "./puzzles/nft_puzzles/nft_intermediate_launcher.clsp.hex", "7a32d2d9571d3436791c0ad3d7fcfdb9c43ace2b0f0ff13f98d29f0cc093f445"),
        ("NFT_METADATA_UPDATER_DEFAULT", "./puzzles/nft_puzzles/nft_metadata_updater_default.clsp.hex", "fe8a4b4e27a2e29a4d3fc7ce9d527adbcaccbab6ada3903ccf3ba9a769d2d78b"),
        ("NFT_METADATA_UPDATER_UPDATEABLE", "./puzzles/nft_puzzles/nft_metadata_updater_updateable.clsp.hex", "0b1ffba1601777c06b78ab38636e9624f2f8da73be9b36e0ce17c8d8ef3bad9f"),
        ("NFT_OWNERSHIP_LAYER", "./puzzles/nft_puzzles/nft_ownership_layer.clsp.hex", "c5abea79afaa001b5427dfa0c8cf42ca6f38f5841b78f9b3c252733eb2de2726"),
        ("NFT_OWNERSHIP_TRANSFER_PROGRAM_ONE_WAY_CLAIM_WITH_ROYALTIES", "./puzzles/nft_puzzles/nft_ownership_transfer_program_one_way_claim_with_royalties.clsp.hex", "025dee0fb1e9fa110302a7e9bfb6e381ca09618e2778b0184fa5c6b275cfce1f"),
        ("NFT_STATE_LAYER", "./puzzles/nft_puzzles/nft_state_layer.clsp.hex", "a04d9f57764f54a43e4030befb4d80026e870519aaa66334aef8304f5d0393c2"),
        # CR Puzzles
        ("CONDITIONS_W_FEE_ANNOUNCE", "./puzzles/vc_puzzles/cr_puzzles/conditions_w_fee_announce.clsp.hex", "1a169582dc619f2542f8eb79f02823e1595ba0aca53820f503eda5ff20b47856"),
        ("CREDENTIAL_RESTRICTION", "./puzzles/vc_puzzles/cr_puzzles/credential_restriction.clsp.hex", "2fdfc1f058cfd65e7ec4e253bfeb394da163ecd0036f508df8629b0a2b8fde96"),
        ("FLAG_PROOFS_CHECKER", "./puzzles/vc_puzzles/cr_puzzles/flag_proofs_checker.clsp.hex", "fe2e3c631562fbb9be095297f762bf573705a0197164e9361ad5d50e045ba241"),
        # VC Puzzles
        ("COVENANT_LAYER", "./puzzles/vc_puzzles/covenant_layer.clsp.hex", "b982796850336aabf9ab17c3f21e299f0c633444117ab5e9ebeafadf1860d9fc"),
        ("EML_COVENANT_MORPHER", "./puzzles/vc_puzzles/eml_covenant_morpher.clsp.hex", "6a87946257f555ae82aca6a11b5205058b844f634ecb6c7dc6b0c54eb2996308"),
        ("EML_TRANSFER_PROGRAM_COVENANT_ADAPTER", "./puzzles/vc_puzzles/eml_transfer_program_covenant_adapter.clsp.hex", "4218fbebbb6f3c0907ebe8a672fa5d1e4bc655645a3a0073601e6c9b50b07c47"),
        ("EML_UPDATE_METADATA_WITH_DID", "./puzzles/vc_puzzles/eml_update_metadata_with_DID.clsp.hex", "d3a9a1fc20f247d009b4b0e941707d50b91885c99d0b27ef882e1294e771139d"),
        ("EXIGENT_METADATA_LAYER", "./puzzles/vc_puzzles/exigent_metadata_layer.clsp.hex", "d5fd32e069fda83e230ccd8f6a7c4f652231aed5c755514b3d996cbeff4182b8"),
        ("P2_ANNOUNCED_DELEGATED_PUZZLE", "./puzzles/vc_puzzles/p2_announced_delegated_puzzle.clsp.hex", "c4d24c3c5349376f3e8f3aba202972091713b4ec4915f0f26192ae4ace0bd04d"),
        ("STANDARD_VC_BACKDOOR_PUZZLE", "./puzzles/vc_puzzles/standard_vc_backdoor_puzzle.clsp.hex", "fbce76408ebaf9b3d0b8cd90cc68607755eeca67cd7432d5eea85f3f498cc002"),
        ("STD_PARENT_MORPHER", "./puzzles/vc_puzzles/std_parent_morpher.clsp.hex", "8c3f1dc2e46c0d7ec4c2cbd007e23c0368ff8f80c5bc0101647a5c27626ebce6"),
        ("VIRAL_BACKDOOR", "./puzzles/vc_puzzles/viral_backdoor.clsp.hex", "00848115554ea674131f89f311707a959ad3f4647482648f3fe91ba289131f51"),
        # Misc Puzzles
        ("AUGMENTED_CONDITION", "./puzzles/augmented_condition.clsp.hex", "d303eafa617bedf0bc05850dd014e10fbddf622187dc07891a2aacba9d8a93f6"),
        ("NOTIFICATION", "./puzzles/notification.clsp.hex", "b8b9d8ffca6d5cba5422ead7f477ecfc8f6aaaa1c024b8c3aeb1956b24a0ab1e"),
        ("P2_1_OF_N", "./puzzles/p2_1_of_n.clsp.hex", "46b29fd87fbeb6737600c4543931222a6c1ed3db6fa5601a3ca284a9f4efe780"),
        ("P2_CONDITIONS", "./puzzles/p2_conditions.clsp.hex", "1c77d7d5efde60a7a1d2d27db6d746bc8e568aea1ef8586ca967a0d60b83cc36"),
        ("P2_DELEGATED_CONDITIONS", "./puzzles/p2_delegated_conditions.clsp.hex", "0ff94726f1a8dea5c3f70d3121945190778d3b2b3fcda3735a1f290977e98341"),
        ("P2_DELEGATED_PUZZLE_OR_HIDDEN_PUZZZLE", "./puzzles/p2_delegated_puzzle_or_hidden_puzzle.clsp.hex", "e9aaa49f45bad5c889b86ee3341550c155cfdd10c3a6757de618d20612fffd52"),
        ("P2_DELEGATED_PUZZLE", "./puzzles/p2_delegated_puzzle.clsp.hex", "542cde70d1102cd1b763220990873efc8ab15625ded7eae22cc11e21ef2e2f7c"),
        ("P2_M_OF_N_DELEGATE_DIRECT", "./puzzles/p2_m_of_n_delegate_direct.clsp.hex", "0f199d5263ac1a62b077c159404a71abd3f9691cc57520bf1d4c5cb501504457"),
        ("P2_PARENT", "./puzzles/p2_parent.clsp.hex", "b10ce2d0b18dcf8c21ddfaf55d9b9f0adcbf1e0beb55b1a8b9cad9bbff4e5f22"),
        ("P2_SINGLETON_AGGREGATOR", "./puzzles/p2_singleton_aggregator.clsp.hex", "f79a31fcfe3736cc75720617b4cdcb4376b4b8f8f71108617710612b909a4924"),
        ("P2_SINGLETON_OR_DELAYED_PUZHASH", "./puzzles/p2_singleton_or_delayed_puzhash.clsp.hex", "adb656e0211e2ab4f42069a4c5efc80dc907e7062be08bf1628c8e5b6d94d25b"),
        ("P2_SINGLETON_VIA_DELEGATED_PUZZLE", "./puzzles/p2_singleton_via_delegated_puzzle.clsp.hex", "9590eaa169e45b655a31d3c06bbd355a3e2b2e3e410d3829748ce08ab249c39e"),
        ("P2_SINGLETON", "./puzzles/p2_singleton.clsp.hex", "40f828d8dd55603f4ff9fbf6b73271e904e69406982f4fbefae2c8dcceaf9834"),
        ("SETTLEMENT_PAYMENT", "./puzzles/settlement_payments.clsp.hex", "cfbfdeed5c4ca2de3d0bf520b9cb4bb7743a359bd2e6a188d19ce7dffc21d3e7"),
        # Singleton Puzzle
        ("SINGLETON_LAUNCHER", "./puzzles/singleton_launcher.clsp.hex", "eff07522495060c066f66f32acc2a77e3a3e737aca8baea4d1a64ea4cdc13da9"),
        ("SINGLETON_TOP_LAYER_V1_1", "./puzzles/singleton_top_layer_v1_1.clsp.hex", "7faa3253bfddd1e0decb0906b2dc6247bbc4cf608f58345d173adb63e8b47c9f"),
        ("SINGLETON_TOP_LAYER", "./puzzles/singleton_top_layer.clsp.hex", "24e044101e57b3d8c908b8a38ad57848afd29d3eecc439dba45f4412df4954fd"),
    ]

rust_dest_path = Path("./src/loaded_chialisp.rs")
python_dest_path = Path("./chia_puzzles_py/programs.py")

os.makedirs(rust_dest_path.parent, exist_ok=True)
os.makedirs(python_dest_path.parent, exist_ok=True)

with open(rust_dest_path, "w") as rust_file, open(python_dest_path, "w") as python_file:
    python_file.write("# Auto-generated Python file with loaded Chialisp constants\n\n")
    rust_file.write("// Auto-generated Rust file with loaded Chialisp constants\n\n")
    here = Path(__file__).parent.resolve()
    # Create the temp directory referenced below if it doesn't exist
    os.makedirs("puzzles/temp", exist_ok=True)
    temp_file = here.joinpath("puzzles/temp/tempfile.clsp.hex")
    try:
        for name, file_path, hash in chialisp_dictionary:
        
            with open(file_path, "r") as hex_file:
                hex_data = hex_file.read().strip().replace("\n", "").replace("\r", "")

            bytes_data = bytes.fromhex(hex_data)

            try:
                os.unlink(temp_file)
            except FileNotFoundError:
                # Fine if the file doesn't exist
                pass

            source_code_path = here.joinpath(file_path[2:-4])
            source_code_dir = here.joinpath(file_path).parent
            compile_clvm(
                input_path=os.fspath(source_code_path),
                output_path=os.fspath(temp_file),
                search_paths=[os.fspath(here.joinpath("puzzles")), os.fspath(source_code_dir)],
            )
            with open(temp_file, "r") as hex_file:
                temp_hex_data = hex_file.read().strip().replace("\n", "").replace("\r", "")

            if temp_hex_data != hex_data:
                raise ValueError(f"Compilation of {name} different then checked in hex file")

            # Check if the actual treehash of the Program matches the recorded hash
            if generate_hash_bytes(bytes_data).hex() != hash:
                raise ValueError(f"Hash mismatch found in: {name}")

            rust_byte_array_string = ", ".join(f"0x{byte:02x}" for byte in bytes_data)
            rust_file.write(
                f"pub const {name}: [u8; {len(bytes_data)}] = [{rust_byte_array_string}];\n"
            )

            python_bytes_literal = "".join(f"\\x{byte:02x}" for byte in bytes_data)
            python_file.write(
                f"{name} = b\"{python_bytes_literal}\"\n"
            )

            print(f"Processed {name} from {file_path}")
        
        print(f"Rust and Python files generated successfully:\n- {rust_dest_path}\n- {python_dest_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(e)


