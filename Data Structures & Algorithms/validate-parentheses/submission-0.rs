impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut s = s;
        loop {
            let prev = s.len();
            s = s.replace("()", "");
            s = s.replace("{}", "");
            s = s.replace("[]", "");
            if s.len() == prev {
                break;
            }
        }   
        s.is_empty()
    }
}
