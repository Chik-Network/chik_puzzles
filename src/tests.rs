#[cfg(test)]
mod tests {
    use crate::loaded_chialisp::{CAT_PUZZLE, SINGLETON_TOP_LAYER};
    #[test]
    fn puzzle_hashes() {
        assert!(CAT_PUZZLE.len() == 1672);
        assert!(SINGLETON_TOP_LAYER.len() == 1168);
    }
}
