#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант: ((N^2+1)^2 mod 19) + 1 = 2
# Задание: Использовать словарь, содержащий следующие ключи: фамилия и
# инициалы; номер группы; успеваемость(список из пяти элементов). Написать
# программу, выполняющую следующие действия: ввод с клавиатуры данных в список,
# состоящий из словарей заданной структуры; записи должны быть упорядочены по
# возрастанию среднего балла; вывод на дисплей фамилий и номеров групп для всех
# студентов, имеющих оценки 4 и 5; если таких студентов нет, вывести
# соответствующее сообщение.

import sys
import json


if __name__ == '__main__':
    # Список студентов.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о студенте.
            name = input("Фамилия и инициалы? ")
            group = input("Номер группы? ")
            marks = list(map(int, input("Оценки: ").split()))

            # Создать словарь
            student = {
                'name': name,
                'group': group,
                'marks': sum(marks)/5,
            }

            # Добавить словарь в список.
            students.append(student)
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('marks', 0))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 17
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                    "№",
                    "Ф.И.О",
                    "Номер группы",
                    "Успеваемость (средний балл)",
                )
            )
            print(line)

            # Вывести данные о всех студентах.
            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        student.get('marks', '')
                    )
                )

            print(line)

        elif command == 'select':

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения студентов из списка.
            for student in students:
                if student.get('marks', '') >= 4:
                    count += 1
                    print(
                        '{:>4}: {}, {}'.format(
                            count,
                            student.get('name', ' '),
                            student.get('group', ' '))
                    )

            # Если счетчик равен 0, то студент не найден.
            if count == 0:
                print("Студент с данным номером не найден.")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла JSON.
            with open(parts[1], 'r') as f:
                students = json.load(f)
                print(students)

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Сохранить данные в файл JSON.
            with open(parts[1], 'w') as f:
                json.dump(students, f)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select <успеваемость> - запросить студентов с успеваемостью;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
