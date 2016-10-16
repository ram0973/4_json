# Решение задачи [№4](https://devman.org/challenges/4/) с сайта [devman.org](https://devman.org)

## Условие задачи:

Написать скрипт, который на вход принимает путь до файла, в котором 
хранится json и выводит его содержимое в консоль в удобном формате 
(это называется pretty print).

## Системные требования

```
Python 3.5.2+
Внешний модуль win-unicode-console
```

## Установка

Windows

```    
git clone https://github.com/ram0973/4_json.git
cd 4_json
pip install -r requirements.txt
```

Linux
```    
git clone https://github.com/ram0973/4_json.git
cd 4_json
pip3 install -r requirements.txt
```
    
## Описание работы
Пользователь вводит путь к файлу как аргумент.
Пример: 
```
python pprint_json.py --json Бары.json
```
Скрипт печатает данные из файла с красивым форматированием. 
    
## Запуск

Windows

python pprint_json.py --json ИмяФайла
 
Linux
 
python3 pprint_json.py --json ИмяФайла

## Лицензия

[MIT](http://opensource.org/licenses/MIT)