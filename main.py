def main():
    while True:
        print("\n=== Меню трекера книг ===")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            show_all_books()
        elif choice == "3":
            show_average_rating()
        elif choice == "4":
            show_author_stats()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("До свидания! Хорошего чтения.")
            break
        else:
            print("Неверный ввод, пожалуйста, выберите пункт от 1 до 6.")


if __name__ == "__main__":
    main()
