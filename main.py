import time


dictionary = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def input_words(f):
    data_input = open(f'{f}.txt', 'r', encoding='utf-8').read()
    data = data_input.split()
    data_words = [word.strip(",.;!?:") for word in data if word[0] in dictionary]
    return data_words, data_input


def to_file(original_text, words, timed):
    result = open('D:\\2\\result.txt', 'w', encoding='utf-8')
    for i in dictionary.upper():
        checker = False
        for word in words:
            if word[0] == i or word[0] == i.lower():
                result.write(word + ' ')
                checker = True
        if checker:
            result.write('\n')
    result.close()
    analysis = open('D:\\2\\analysis.txt', 'w', encoding='utf-8')
    analysis.write(f"""Введенный текст:
{original_text}
\nВариант 17: кириллица, по алфавиту, по возрастанию, не учитывать числа, быстрая сортировка.
Количество слов: {len(words)}
Время сортировки: {round(timed, 4)} сек
Статистика:\n""")
    for i in dictionary.lower():
        count = 0
        for word in words:
            if word.startswith(i) or word.startswith(i.upper()):
                count += 1
        analysis.write(f'{i} - {count}\n')


def quick_sort(array):
    if len(array) == 0:
        return array
    pivot = array[len(array)//2]
    first = [num for num in array if num < pivot]
    second = [num for num in array if num > pivot]
    element = [pivot] * array.count(pivot)
    return quick_sort(first) + element + quick_sort(second)


file = input("Введите путь к файлу:")
start_time = time.time()
list_of_words, input_text = input_words(file)
sorted_words = quick_sort(list_of_words)
end_time = time.time()
needed_time = end_time - start_time
to_file(input_text, sorted_words, needed_time)
