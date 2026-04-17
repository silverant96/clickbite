# CSV Report Generator

Утилита для чтения CSV файлов и генерации отчетов с фильтрацией данных.

## Установка

pip install tabulate

## **Использование**

python main.py --files <файлы.csv> --report <тип_отчета>

## Аргументы
--files - список CSV файлов для обработки

--report - тип отчета (clickbite или другой)

--delimiter - разделитель для чтения файла (по умолчанию ",")

## Пример

python main.py --files data.csv --report clickbite


## Тесты

Модуль для тестов test_report