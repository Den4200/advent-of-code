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

fn part_one(data: &Vec<u32>) -> u32 {
    zip(data, &data[1..])
        .map(|(prev, curr)| if curr > prev { 1 } else { 0 })
        .sum()
}

fn part_two(data: &Vec<u32>) -> u32 {
    zip(data, &data[3..])
        .map(|(prev, curr)| if curr > prev { 1 } else { 0 })
        .sum()
}
