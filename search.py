input("Введите запрос пример [7999999999], [Виктор Викторович]")

def search_files(query):
    # Путь к папке "data" вы можете поменять название папке просто поменяв нащвание папки в 51-ой строке
    data_dir = os.path.join(os.getcwd(), 'data')

    # Посик по базам в папке "data"
    for filename in os.listdir(data_dir):
        # Проверка формата файлов
        if filename.endswith(('.txt', '.csv', '.xlsx')):
            # Чтение баз
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r') as file:
                for line_num, line in enumerate(file, start=1):
                    # Найдено/Не найдено
                    if query in line:
                        # Есл найдено то
                        print(f"База: {filename}, Строка {line_num}: {line.strip()}")

query = '7999999999'
search_files(query)