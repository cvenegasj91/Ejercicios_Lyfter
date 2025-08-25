import actions
import menu
import data


def main():
    student_list = []
    while True:
        option = menu.show_menu()
        if option == 1:
            actions.enter_students_info(student_list)
        elif option == 2:
            actions.print_students_list(student_list)
        elif option == 3:
            actions.print_top3_average(student_list)
        elif option == 4:
            actions.print_overall_average(student_list)
        elif option == 5:
            data.write_csv_file('student_list.csv', student_list, student_list[0].keys() if student_list else None)
        elif option == 6:
            data.read_csv_file('student_list.csv', student_list)
        elif option == 7:
            print("Programa finalizado")
            break


if __name__ == '__main__':
    main()