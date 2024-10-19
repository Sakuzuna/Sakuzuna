import colorama
from colorama import Fore
import os 
import csv 
import sys
import time
import pandas as pd

Red = Fore.RED 
Yellow = Fore.YELLOW 
White = Fore.WHITE
Reset = Fore.RESET 
data_dir = os.path.join(os.getcwd(), 'data')

print(f"{Yellow}Введите юзернейм{Reset}")

def юзернейм():
    input()
    
if input() == "Sakuzuna":
    print(f"{Red}Юзернейм подошел{Reset}")
    print(f"{Red}Введите пароль{Reset}")
else:
    print(f"{Red}Неправильный юзернейм{Reset}")
    exit()

if input() == "YaPidar":
    print(f"{Red}Пароль подошел{Reset}")
    print(f"{Red}Нажмите ENTER для запуска софта{Reset}")
else:
    print(f"{Red}Неправильный пароль{Reset}")
    exit()
    
юзернейм()

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

print_with_delay("Привет бро я хочу сказать что не юзайте этот софт для плохих вещей против других людей так как это может плохо для тебя закончиться но ты скорее всего ровно меня не послушаешься. Удачи!!!")


print(f"{Red}     .--.--.                     ,-.           ")
time.sleep(0.2)
print(f"{Red}    /  /    '.               ,--/ /|         ")
time.sleep(0.2)
print(f"{Red}   |  :  /`. /             ,--. :/ |          ,--,        ,----,         ,--,      ,---,          ")
time.sleep(0.2)
print(f"{Red}   ;  |  |--`              :  : ' /         ,'_ /|      .'   .`|       ,'_ /|  ,-+-. /  |          ")     
time.sleep(0.2)
print(f"{Red}   |  :  ;_      ,--.--.   |  '  /     .--. |  | :   .'   .'  .'  .--. |  | : ,--.'|'   |  ,--.--.     ") 
time.sleep(0.2)
print(f"{Red}    \  \    `.  /       \  '  |  :   ,'_ /| :  . | ,---, '   ./ ,'_ /| :  . ||   |  , ' | /       \  ")
time.sleep(0.2)
print(f"{Red}     `----.   \.--.  .-. | |  |   \  |  ' | |  . . ;   | .'  /  |  ' | |  . .|   | /  | |.--.  .-. |    ")
time.sleep(0.2)
print(f"{Red}     __ \  \  | \__\/: . . '  : |. \ |  | ' |  | | `---' /  ;--,|  | ' |  | ||   | |  | | \__\/: . .    ")
time.sleep(0.2)
print(f"{Red}    /  /`--'  / ,  .--.; | |  | ' \ \:  | : ;  ; |   /  /  / .`|:  | : ;  ; ||   | |  |/  ,  .--.; |    ")
time.sleep(0.2)
print(f"{White}   '--'.     / /  /  ,.  | '  : |--' '  :  `--'   \./__;     .' '  :  `--'   \   | |--'  /  /  ,.  |    ")
time.sleep(0.2)
print(f"{White}     `--'---' ;  :   .'   \;  |,'    :  ,      .-./;   |  .'    :  ,      .-./   |/     ;  :   .'   \   ")
time.sleep(0.2)
print(f"{White}              |  ,     .-./'--'       `--`----'    `---'         `--`----'   '---'      |  ,     .-./   ")
time.sleep(0.2)
print(f"{White}               `--`---'                                                                  `--`---'       ")
time.sleep(0.2)
print(f"{White}            ")                                                                                          
time.sleep(0.2)
print(f"{White}       ")
time.sleep(0.2)
print(f"{White}          ╔════════════════════════════════════════════════════════════════════╗  ")
time.sleep(0.2)
print(f"{White}          ║ Софт был написан во временна древних Римляней так что не осуждайте ║       ")                                                       
time.sleep(0.2)
print(f"{White}          ╚════════════════════════════════════════════════════════════════════╝       ")
time.sleep(0.2)
print(f"{White}          ╔════════════════════════════════════════════════════════════════════╗  ")
time.sleep(0.2)
print(f"{White}          ║                    </// Coded by Sakuzuna \\\>                     ║  ")
time.sleep(0.2)
print(f"{White}          ╚════════════════════════════════════════════════════════════════════╝   ")

def search_in_txt_and_csv(file_path, search_query):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if search_query in line:
                print(f"Найдено в {file_path}, строка {line_number}: {line.strip()}")

def search_in_xlsx(file_path, search_query):
    xlsx_data = pd.read_excel(file_path, engine='openpyxl')
    for sheet_name in xlsx_data.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        for row_number, row in df.iterrows():
            if row.astype(str).str.contains(search_query).any():
                print(f"Найдено в {file_path} (лист: {sheet_name}), строка {row_number + 1}: {row.to_string(index=False)}")

def main():
    search_query = input("Введите запрос для поиска: ")
    current_directory = os.getcwd()

    for filename in os.listdir(current_directory):
        if filename.endswith('.txt') or filename.endswith('.csv'):
            file_path = os.path.join(current_directory, filename)
            search_in_txt_and_csv(file_path, search_query)
        elif filename.endswith('.xlsx'):
            file_path = os.path.join(current_directory, filename)
            search_in_xlsx(file_path, search_query)

if __name__ == '__main__':
    main()
