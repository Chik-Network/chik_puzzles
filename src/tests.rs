#[cfg(test)]
mod tests {
    use crate::loaded_chialisp::CAT_PUZZLE;
    #[test]
    fn puzzle_hashes() {
        assert!(CAT_PUZZLE.len() == 1672);
    }
}
