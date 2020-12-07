fn main() {
    let data = get_input();

    println!("{}", part_one(&data));
    println!("{}", part_two(&data));
}

fn get_input<'a>() -> Vec<&'a str> {
    let input = include_str!("input.txt");

    input.lines().collect::<Vec<&str>>()
}

fn get_trees(data: &Vec<&str>, dx: usize, dy: usize) -> u8 {
    let height = data.len();
    let width = data[0].len();

    let mut trees = 0;
    let mut x = 0;

    for y in (0..height).step_by(dy) {
        if data[y].chars().nth(x).unwrap() == '#' {
            trees += 1;
        }

        x = (x + dx) % width;
    }

    trees
}

fn part_one(data: &Vec<&str>) -> u8 {
    return get_trees(data, 3, 1);
}

fn part_two(data: &Vec<&str>) -> u32 {
    let slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];

    slopes
        .iter()
        .map(|(dx, dy)| get_trees(data, *dx as usize, *dy as usize) as u32)
        .product()
}
