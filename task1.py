from task2 import get_files_count
from task3 import FileProcessing
from task3 import list_sorting


def main():
    fp = FileProcessing
    print(f'Task 1: count files\n{get_files_count("D:/pe_lab4") = }')
    print(f'Task 2: making list from file\n{fp.make_list_from_file("students.csv") = }')
    data = fp.make_list_from_file("students.csv")
    print(f'Task 2.1: list sorting by last name\n{list_sorting(data[1:], 1) = }')
    print(f'Task 2.2: age > 22\n{[x for x in data[1:] if int(x[2]) >= 22] = }')
    print(f'Task 2.3: writing in csv\n{fp.write_csv(data, "test.csv") = }')
    print(f'Task 2.3: writing in csv\n{fp.write_csv(data, "test.csv") = }')
    data.append(['11', 'Воронов Василий Евгеньевич', '173', 'БДО-123'])
    fp.write_csv(data, "students_changed.csv")
    print(f'Task 2.4: writing in csv changed data\n{data = }')
    print(f'{fp.make_list_from_file("students_changed.csv") = }')
    print(f'Task 2.5: writing in pickle')
if __name__ == '__main__':
    main()
