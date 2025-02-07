use std::io;


fn main()
{
    let mut line = String::new();
    let c: u32;
    let k: u32;
    let p: u32;

    io::stdin().read_line(
        &mut line
    ).expect("Failed to read line");

    let mut iter = line.trim().split_whitespace();
    c = iter.next().unwrap().parse().unwrap();
    k = iter.next().unwrap().parse().unwrap();
    p = iter.next().unwrap().parse().unwrap();

    // 1..3 = 1, 2, 3
    let mut result_vector: Vec<u32> = Vec::new();
    for i in 1..=c as u32 {
        let calculation = i * k + p * i.pow(2);        
        result_vector.push(calculation);
    }
    let total_sum: u32 = result_vector.iter().sum();
    println!("{}", total_sum);
}