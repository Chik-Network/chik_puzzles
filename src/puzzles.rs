use std::fs::File;
use std::io::{self, Read};
use std::path::Path;
use hex::decode;

fn load_hex_file<P: AsRef<Path>>(file_path: P) -> Result<Vec<u8>, io::Error> {
    // Open the file
    let mut file = File::open(file_path)?;
    
    // Read the file contents into a string
    let mut hex_string = String::new();
    file.read_to_string(&mut hex_string)?;
    
    // Remove any whitespace or newlines (if necessary)
    let hex_string = hex_string.trim().replace('\n', "").replace('\r', "");
    
    // Decode the hex string into bytes
    match hex::decode(&hex_string) {
        Ok(bytes) => Ok(bytes),
        Err(e) => {
            eprintln!("Error decoding hex string: {}", e);
            Err(io::Error::new(io::ErrorKind::InvalidData, "Invalid hex string"))
        }
    }
}

pub const CAT_PUZZLE: [u8; 1672] = load_hex_file!()?.as_ref();