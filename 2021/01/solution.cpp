#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

vector<int> get_input(string filename);
int part_one(vector<int> input);
int part_two(vector<int> input);

int main() {
    vector<int> input = get_input("input.txt");

    cout << "Day 01 Part 01: " << part_one(input) << endl;
    cout << "Day 01 Part 02: " << part_two(input) << endl;

    return 0;
}

vector<int> get_input(string filename) {
    ifstream file(filename);
    vector<int> input;

    int num;
    while (file >> num) {
        input.push_back(num);
    }

    file.close();
    return input;
}

int part_one(vector<int> input) {
    int increases = 0;

    for (int i = 1; i < input.size(); i++) {
        if (input[i] > input[i - 1]) {
            increases++;
        }
    }

    return increases;
}

int part_two(vector<int> input) {
    int increases = 0;

    for (int i = 3; i < input.size(); i++) {
        if (input[i] > input[i - 3]) {
            increases++;
        }
    }

    return increases;
}
