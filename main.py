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

def print_with_delay(text, delay=0.2):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

print_with_delay("Привет бро я хочу сказать что не юзайте этот софт для манипуляции против других людей так как это может плохо 
для тебя закончиться но ты скорее все ровно меня не послушаешься. Удачи!!!")


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
print(f"{White}          ║    <1> Посик по базам                 <2> Красивие символы         ║  ")
time.sleep(0.2)
print(f"{White}          ╚════════════════════════════════════════════════════════════════════╝   ")


input(f"{Yellow}Введите запрос{Reset}")

if input() == "1":
    subprocess.run("python", ["search.py"], capture_output=True, text=True)
    
elif input() == "2":
    subprocess.run("python", ["symbols.py"], capture_output=True, text=True)
    
elif input() == "3":
    subprocess.run("python" ["template.py"], capture_output=True, text=True)
