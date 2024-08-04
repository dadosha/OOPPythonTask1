import os


# def comparison_files(file1, file2):
#     return max(file1, file2), min(file1, file2)
#
#
# def read_file(file):
#     with open(file, encoding="UTF-8") as f:
#         return f.readlines()
#
#
# def parsing_recipes_file(file_path1, file_path2):
#     file1_lines = read_file(os.path.join(os.getcwd(), file_path1))
#     file2_lines = read_file(os.path.join(os.getcwd(), file_path2))
#
#     more_file, less_file = comparison_files(file1_lines, file2_lines)
#
#     with open('../files/final_file.txt', 'w', encoding="UTF-8") as f:
#         f.write(str(len(less_file)) + '\n')
#         for line in less_file:
#             f.write(line)
#
#         f.write('\n' + str(len(more_file)) + '\n')
#         for line in more_file:
#             f.write(line)
#
#
# def main():
#     file_path1 = '../files/1.txt'
#     file_path2 = '../files/2.txt'
#
#     parsing_recipes_file(file_path1, file_path2)


import os


def read_file(file_path):
    """Читает содержимое файла и возвращает количество строк и содержимое"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return len(lines), lines


def write_combined_file(files_info, output_file_path):
    """Записывает отсортированное содержимое файлов в итоговый файл"""
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for file_name, line_count, content in files_info:
            f.write(f"{file_name}\n{line_count}\n")
            f.writelines(content)
            f.write("\n")  # Добавим пустую строку между содержимым файлов


def main():
    # Задаем путь к директории с файлами
    directory_path = '../files/'  # Замените на путь к вашей папке
    output_file_path = '../files/final_file.txt'  # Итоговый файл

    # Получаем список файлов в директории
    file_names = ['1.txt', '2.txt']  # Укажите ваши файлы

    # Собираем информацию о каждом файле
    files_info = []
    for file_name in file_names:
        file_path = os.path.join(directory_path, file_name)
        line_count, content = read_file(file_path)
        files_info.append((file_name, line_count, content))

    # Сортируем файлы по количеству строк
    files_info.sort(key=lambda x: x[1])

    # Записываем объединенный файл
    write_combined_file(files_info, output_file_path)
    print(f"Объединенный файл создан: {output_file_path}")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()