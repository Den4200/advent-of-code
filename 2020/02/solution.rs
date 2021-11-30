use lazy_static::lazy_static;

use regex::Regex;

fn main() {
    let data = get_input();

    println!("Day 02 Part 01: {}", part_one(&data));
    println!("Day 02 Part 02: {}", part_two(&data));
}

fn get_input() -> Vec<(u16, u16, String, String)> {
    lazy_static! {
        static ref PARSER: Regex = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();
    }

    let input = include_str!("input.txt");

    PARSER
        .captures_iter(input)
        .map(|m| {
            (
                m[1].parse::<u16>().unwrap(),
                m[2].parse::<u16>().unwrap(),
                m[3].to_string(),
                m[4].to_string(),
            )
        })
        .collect()
}

fn compare_letter(letter: &String, string: &String, index: usize) -> bool {
    string.chars().nth(index).unwrap().to_string() == *letter
}

fn part_one(data: &Vec<(u16, u16, String, String)>) -> u16 {
    data.iter()
        .map(|(lower, upper, letter, pw)| {
            let matches = &(pw.matches(letter).count() as u16);
            (lower <= matches && matches <= upper) as u16
        })
        .sum()
}

fn part_two(data: &Vec<(u16, u16, String, String)>) -> u16 {
    data.iter()
        .map(|(first, second, letter, pw)| {
            (compare_letter(letter, pw, (first - 1) as usize) ^ compare_letter(letter, pw, (second - 1) as usize)) as u16
        })
        .sum()
}
