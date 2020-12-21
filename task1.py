from files import get_files_count
from file import FileProcessing
from file import list_sorting


def main():
    fp = FileProcessing
    print(f'Task 1: count files\n{get_files_count("D:/pe_lab4") = }')
    print(f'Task 2: making list from file\n{fp.make_list_from_file("students.csv") = }')

if __name__ == '__main__':
    main()
