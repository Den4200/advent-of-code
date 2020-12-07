fn main() {
    let data = get_input();

    println!("Day 01 Part 01: {}", part_one(&data).unwrap());
    println!("Day 01 Part 02: {}", part_two(&data).unwrap());
}

fn get_input() -> Vec<i64> {
    let input = String::from(include_str!("input.txt"));
    
    input
        .lines()
        .map(|num| num.parse::<i64>().unwrap())
        .collect()
}

fn part_one(data: &Vec<i64>) -> Option<i64> {
    for x in data {
        let y = 2020 - x;

        if data.contains(&y) {
            return Some(x * y);
        }
    }
    None
}

fn part_two(data: &Vec<i64>) -> Option<i64> {
    for x in data {
        for y in data {
            let z = 2020 - y - x;

            if data.contains(&z) {
                return Some(x * y * z);
            }
        }
    }
    None
}
