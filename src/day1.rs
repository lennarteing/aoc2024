fn part_1(mut left: Vec<i32>, mut right: Vec<i32>) -> i32 {
    left.sort();
    right.sort();
    32
}

fn part_2(left: Vec<i32>, right: Vec<i32>) -> i32 {
    32
}

#[cfg(test)]
mod tests {

    use super::{part_1, part_2};

    #[test]
    fn test_part_1() {
        let test_input = String::from("3   4
4   3
2   5
1   3
3   9
3   3");
        println!("{}", test_input)
    }

}
