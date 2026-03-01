import time
import random


def sequential_search(a_list, item):
    start = time.time()

    found = False
    for element in a_list:
        if element == item:
            found = True
            break

    end = time.time()
    return found, end - start


def ordered_sequential_search(a_list, item):
    start = time.time()

    found = False
    for element in a_list:
        if element == item:
            found = True
            break
        elif element > item:
            break

    end = time.time()
    return found, end - start


def binary_search_iterative(a_list, item):
    start = time.time()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if a_list[midpoint] == item:
            found = True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    end = time.time()
    return found, end - start


def binary_search_recursive(a_list, item):
    start = time.time()

    def helper(sub_list):
        if len(sub_list) == 0:
            return False

        midpoint = len(sub_list) // 2

        if sub_list[midpoint] == item:
            return True
        elif item < sub_list[midpoint]:
            return helper(sub_list[:midpoint])
        else:
            return helper(sub_list[midpoint + 1:])

    found = helper(a_list)

    end = time.time()
    return found, end - start


def main():
    sizes = [500, 1000, 5000]
    trials = 100
    target = 99999999  # worst case: not in list

    for size in sizes:
        seq_times = []
        ord_seq_times = []
        bin_iter_times = []
        bin_rec_times = []

        for _ in range(trials):
            rand_list = [random.randint(0, 10000) for _ in range(size)]

            # Sequential search (unsorted list)
            _, t = sequential_search(rand_list, target)
            seq_times.append(t)

            # Sort list BEFORE ordered/binary searches
            sorted_list = rand_list.copy()
            sorted_list.sort()

            # Ordered sequential search
            _, t = ordered_sequential_search(sorted_list, target)
            ord_seq_times.append(t)

            # Binary search iterative
            _, t = binary_search_iterative(sorted_list, target)
            bin_iter_times.append(t)

            # Binary search recursive
            _, t = binary_search_recursive(sorted_list, target)
            bin_rec_times.append(t)

        print(f"List size {size}")
        print(f"Sequential Search took {sum(seq_times)/trials:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {sum(ord_seq_times)/trials:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {sum(bin_iter_times)/trials:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {sum(bin_rec_times)/trials:10.7f} seconds to run, on average\n")


if __name__ == "__main__":
    main()

    