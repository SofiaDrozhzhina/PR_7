def filter_words(input_string, max_length):
    words = input_string.split(', ')
    filtered_words = [word.lower() for word in words if len(word) <= max_length]
    return ' '.join(filtered_words)


def main():
    input_string = input("Введите слова через запятую и пробел: ")
    n = int(input('Введите число: '))
    print(filter_words(input_string, n))


main()
