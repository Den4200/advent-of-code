use lazy_static::lazy_static;

use regex::Regex;

fn main() {
    let data = get_input();

    println!("Day 02 Part 01: {}", part_one(&data));
    println!("Day 02 Part 02: {}", part_two(&data));
}

fn get_input<'a>() -> Vec<(&'a str, i32)> {
    lazy_static! {
        static ref PARSER: Regex = Regex::new(r"(\w+) (\d+)").unwrap();
    }

    let input = include_str!("input.txt");

    PARSER
        .captures_iter(input)
        .map(|m| (m.get(1).unwrap().as_str(), m[2].parse::<i32>().unwrap()))
        .collect()
}

fn part_one(data: &Vec<(&str, i32)>) -> i32 {
    let (x, depth) = data
        .iter()
        .map(|(direction, amount)| match *direction {
            "forward" => (*amount, 0),
            "up" => (0, -amount),
            "down" => (0, *amount),
            _ => panic!("unknown direction"),
        })
        .reduce(|(x1, depth1), (x2, depth2)| (x1 + x2, depth1 + depth2))
        .unwrap();

    x * depth
}

fn part_two(data: &Vec<(&str, i32)>) -> i32 {
    let (x, depth, _aim) =
        data.iter().fold(
            (0, 0, 0),
            |(x, depth, aim), (direction, amount)| match *direction {
                "forward" => (x + amount, depth + aim * amount, aim),
                "up" => (x, depth, aim - amount),
                "down" => (x, depth, aim + amount),
                _ => panic!("unknown direction"),
            },
        );

    x * depth
}
