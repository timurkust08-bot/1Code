def delete_book():
    books = load_books()
    print("\n--- Удаление книги ---")
    if not books:
        print("Нечего удалять, трекер пуст.")
        return

    print("Выберите способ удаления:")
    print("1. По номеру (индексу) в списке")
    print("2. По автору и названию")
    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        show_all_books()
        try:
            idx = int(input("Введите номер книги для удаления: "))
            if 1 <= idx <= len(books):
                removed = books.pop(idx - 1)
                save_books(books)
                print(
                    f"Книга '{removed['author']} - {removed['title']}' успешно удалена!"
                )
            else:
                print("Неверный номер.")
        except ValueError:
            print("Введен некорректный номер.")

    elif choice == "2":
        author = input("Введите автора книги для удаления: ").strip()
        title = input("Введите название книги для удаления: ").strip()

        initial_count = len(books)
        books = [
            b
            for b in books
            if not (
                b["author"].lower() == author.lower()
                and b["title"].lower() == title.lower()
            )
        ]

        if len(books) < initial_count:
            save_books(books)
            print(f"Книга '{author} - {title}' успешно удалена!")
        else:
            print("Книга с такими параметрами не найдена.")
    else:
        print("Неверный пункт меню.")
