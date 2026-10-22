struct MinStack {
    stack: Vec<i32>,
}

impl MinStack {
    fn new() -> Self {
        Self { stack: Vec::new() }
    }

    fn push(&mut self, val: i32) {
        self.stack.push(val);
    }

    fn pop(&mut self) {
        self.stack.pop();
    }

    fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }

    fn get_min(&mut self) -> i32 {
        let mut tmp = Vec::new();
        let mut mini = *self.stack.last().unwrap();

        while let Some(val) = self.stack.pop() {
            mini = mini.min(val);
            tmp.push(val);
        }

        while let Some(val) = tmp.pop() {
            self.stack.push(val);
        }

        mini
    }
}
