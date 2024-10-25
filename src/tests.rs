

// const fn load_hex_file<P: AsRef<Path>>(file_path: P) -> Result<Vec<u8>, io::Error> {
//     // Open the file
//     let mut file = File::open(file_path);
    
//     // Read the file contents into a string
//     let mut hex_string = String::new();
//     file.read_to_string(&mut hex_string)?;
    
//     // Remove any whitespace or newlines (if necessary)
//     let hex_string = hex_string.trim().replace('\n', "").replace('\r', "");
    
//     // Decode the hex string into bytes
//     match hex::decode(&hex_string) {
//         Ok(bytes) => Ok(bytes),
//         Err(e) => {
//             eprintln!("Error decoding hex string: {}", e);
//             Err(io::Error::new(io::ErrorKind::InvalidData, "Invalid hex string"))
//         }
//     }
// }

#[cfg(test)]
mod tests {
    use crate::loaded_chialisp::CAT_PUZZLE;
    #[test]
    fn puzzle_hashes() {
        assert!(CAT_PUZZLE.len() == 1672);
    }
}