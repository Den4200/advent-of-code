#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *data;
    int size;
} Vector;

void Vec_push(Vector *vec, int num) {
    vec->data = realloc(vec->data, ++vec->size * sizeof(int));
    vec->data[vec->size - 1] = num;
}

Vector get_input(char *filename);
int part_one(Vector *input);
int part_two(Vector *input);

int main()
{
    Vector input = get_input("input.txt");

    printf("Day 01 Part 01: %d\n", part_one(&input));
    printf("Day 01 Part 02: %d\n", part_two(&input));

    return 0;
}

Vector get_input(char *filename)
{
    Vector input = {};

    int num;
    FILE *file = fopen(filename, "r");
    while (fscanf(file, "%d", &num) != EOF) {
        Vec_push(&input, num);
    }

    fclose(file);
    return input;
}

int part_one(Vector *input) {
    int increases = 0;

    for (int i = 1; i < input->size; i++)
    {
        if (input->data[i] > input->data[i - 1]) {
            increases++;
        }
    }

    return increases;
}

int part_two(Vector *input) {
    int increases = 0;

    for (int i = 3; i < input->size; i++) {
        if (input->data[i] > input->data[i - 3]) {
            increases++;
        }
    }

    return increases;
}
