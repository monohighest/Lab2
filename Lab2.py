
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    input_str = input()

    str_list = input_str.split(",")

    float_list = []
    for item in str_list:
        float_list.append(float(item.strip()))

    return float_list


def calc_average(num_list):
    if len(num_list) == 0:
        return 0.0

    average = sum(num_list) / len(num_list)
    return average


def find_min_max(num_list):
    if len(num_list) == 0:
        return [0.0, 0.0]

    minimum = min(num_list)
    maximum = max(num_list)

    return [minimum, maximum]


def sort_temperature(num_list):
    sorted_list = sorted(num_list)
    return sorted_list


def calc_median_temperature(num_list):
    if len(num_list) == 0:
        return 0.0

    sorted_list = sorted(num_list)
    n = len(sorted_list)
    middle = n // 2

    if n % 2 == 1:
        return sorted_list[middle]
    else:
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    display_main_menu()
    num_list = get_user_input()

    print("User input float list:", num_list)

    average = calc_average(num_list)
    print("Average temperature:", average)

    min_max = find_min_max(num_list)
    print("Minimum temperature:", min_max[0])
    print("Maximum temperature:", min_max[1])

    sorted_list = sort_temperature(num_list)
    print("Sorted temperatures:", sorted_list)

    median = calc_median_temperature(num_list)
    print("Median temperature:", median)


if __name__ == "__main__":
    main()
