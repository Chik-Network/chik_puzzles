use std::fs;
use std::path::Path;
use hex::decode;
use std::fs::File;
use std::io::{BufWriter, Write};

fn main() {
    let chialisp_dictionary = [
        ("CAT_PUZZLE", "./chia_puzzles/puzzles/cat_puzzles/cat_v2.clsp.hex"),
    ];
    let dest_path = Path::new("./src/loaded_chialisp.rs");
    let f = File::create(dest_path).expect("unable to create file");
    let mut f = BufWriter::new(f);

    for (name, file_path) in chialisp_dictionary{
        let hex_file_path = Path::new(file_path);

        let hex_data = fs::read_to_string(hex_file_path)
            .expect("Failed to read the hex file");

        println!("Loaded hex data: {}", hex_data);

        let hex_data = hex_data.trim().replace('\n', "").replace('\r', "");

        let bytes = decode(&hex_data).expect("Failed to decode hex string");

        let byte_array_string = bytes
            .iter()
            .map(|byte| format!("0x{:02x}", byte))
            .collect::<Vec<_>>()
            .join(", ");

        writeln!(
            f,
            "pub const {}: [u8; {}] = [{}];",
            name,
            bytes.len(),
            byte_array_string
        ).expect("Failed to write to loaded_chialisp.rs");
    }
}