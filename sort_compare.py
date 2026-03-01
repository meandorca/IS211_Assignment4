import time
import random

def insertion_sort(a_list):
    start = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end = time.time()
    return end - start


def shell_sort(a_list):
    start = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()
    return end - start


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return end - start


def main():
    sizes = [500, 1000, 5000]
    trials = 100

    for size in sizes:
        insertion_times = []
        shell_times = []
        python_times = []

        for _ in range(trials):
            rand_list = [random.randint(0, 10000) for _ in range(size)]

            insertion_times.append(insertion_sort(rand_list.copy()))
            shell_times.append(shell_sort(rand_list.copy()))
            python_times.append(python_sort(rand_list.copy()))

        print(f"List size {size}")
        print(f"Insertion Sort took {sum(insertion_times)/trials:10.7f} seconds to run, on average")
        print(f"Shell Sort took {sum(shell_times)/trials:10.7f} seconds to run, on average")
        print(f"Python Sort took {sum(python_times)/trials:10.7f} seconds to run, on average\n")


if __name__ == "__main__":
    main()

