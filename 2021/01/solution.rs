use itertools::zip;

fn main() {
    let data = get_input();

    println!("Day 01 Part 01: {}", part_one(&data));
    println!("Day 01 Part 02: {}", part_two(&data));
}

fn get_input() -> Vec<u32> {
    let input = String::from(include_str!("input.txt"));
    
    input
        .lines()
        .map(|num| num.parse::<u32>().unwrap())
        .collect()
}

fn part_one(data: &Vec<u32>) -> usize {
    zip(data, &data[1..])
        .filter(|(prev, curr)| curr > prev)
        .count()
}

fn part_two(data: &Vec<u32>) -> usize {
    zip(data, &data[3..])
        .filter(|(prev, curr)| curr > prev)
        .count()
}
