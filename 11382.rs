use std::io::stdin;

fn main() {
    let mut buffer = String::new();
    stdin().read_line(&mut buffer).unwrap();
    
    let s = String::from(buffer.trim());
    if s.contains(" ") {
        let result: usize;
        let mut number: usize = 0;
        for w in s.split_whitespace() {
            number += w.parse::<usize>().unwrap();
        }
        result = number;

        println!("{}", result);
    }
}
