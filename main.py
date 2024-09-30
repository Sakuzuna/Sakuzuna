import colorama
from colorama import Fore
import os 
import csv 
import sys
import time
import subprocess

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
