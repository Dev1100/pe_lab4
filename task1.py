from files import get_files_count
from file import FileProcessing
from file import list_sorting


def main():
    fp = FileProcessing
    print(f'Task 1: count files\n{get_files_count("D:/pe_lab4") = }')
    print(f'Task 2: making list from file\n{fp.make_list_from_file("students.csv") = }')
    data = fp.make_list_from_file("students.csv")
    print(f'Task 2.1: list sorting by last name\n{list_sorting(data[1:], 1) = }')
    print(f'Task 2.2: age > 22\n{[x for x in data[1:] if int(x[2]) >= 22] = }')
    print(f'Task 2.3: writing in csv\n{fp.write_csv(data, "test.csv") = }')

if __name__ == '__main__':
    main()
