impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        for row in 0..9 {
            let mut seen = HashSet::new();
            for i in 0..9 {
                if board[row][i] == '.' { continue; }
                if !seen.insert(board[row][i]) { return false; }
            }
        }

        for col in 0..9 {
            let mut seen = HashSet::new();
            for i in 0..9 {
                if board[i][col] == '.' { continue; }
                if !seen.insert(board[i][col]) { return false; }
            }
        }

        for square in 0..9 {
            let mut seen = HashSet::new();
            for i in 0..3 {
                for j in 0..3 {
                    let row = (square / 3) * 3 + i;
                    let col = (square % 3) * 3 + j;
                    if board[row][col] == '.' { continue; }
                    if !seen.insert(board[row][col]) { return false; }
                }
            }
        }

        true
    }
}