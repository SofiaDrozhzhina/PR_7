def find_common_numbers(line1, line2, line3):
    set1 = set(line1.split())
    set2 = set(line2.split())
    set3 = set(line3.split())
    common_numbers = set2.intersection(set3) - set1
    common_numbers = list(common_numbers)
    total_sum = sum(int(num) for num in common_numbers)
    return "; ".join(common_numbers), total_sum


def main():
    line1 = input("Введите первую строку чисел (разделённых пробелами): ")
    line2 = input("Введите вторую строку чисел (разделённых пробелами): ")
    line3 = input("Введите третью строку чисел (разделённых пробелами): ")
    result, total_sum = find_common_numbers(line1, line2, line3)
    print("Совпадающие числа:", result)
    print("Сумма совпадающих чисел:", total_sum)


main()
