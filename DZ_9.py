# task1
b = b'r\xc3\xa9sum\xc3\xa9'
s = b.decode('utf-8')
print(s)
s = s.encode('Latin1')
print(s)
res = s.decode('Latin1')
print(res)
# task2
Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создать файл и записать в него первые 2 строки и закрыть файл.
Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с
новой строки.
str1 = input()
str2 = input()
str3 = input()
str4 = input()
f = open('languages.txt', 'w')
f.write(str1 +'\n')
f.write(str2 + '\n')
f.close()
f = open('languages.txt', 'a')
f.write(str3 + '\n')
f.write(str4 + '\n')
f.close()
# task3
 Создать словарь в качестве ключа которого будет 6-ти значное число id,
а в качестве значений кортеж состоящий из 2 элементов – имя(str), возраст(int)
Сделать около 5-6 элементов. Записать данный словарь на диск в json-файл.
import json

d = {
    111111 : ('Max', 25),
    222222 : ('Vlad', 18),
    333333 : ('Anton', 41),
    444444 : ('Pasha', 26),
    555555 : ('Valery', 54)
}

with open('dictionary.json', 'w') as file:
    json.dump(d, file, indent=3)

