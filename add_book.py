def add_book():
    print("\n--- Добавление книги ---")
    author = input("Введите автора книги: ").strip()
    title = input("Введите название книги: ").strip()

    if not author or not title:
        print("Ошибка: Автор и название не могут быть пустыми!")
        return

    books = load_books()
    for book in books:
        if (
            book["author"].lower() == author.lower()
            and book["title"].lower() == title.lower()
        ):
            print(
                f"Ошибка: Книга '{author} - {title}' уже есть в трекере! (Дублирование запрещено)"
            )
            return

    while True:
        try:
            rating = int(input("Введите оценку (целое число от 1 до 5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть в диапазоне от 1 до 5!")
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

    date_read = input("Введите дату прочтения (например, ГГГГ-ММ-ДД): ").strip()
    if not date_read:
        date_read = "Не указана"

    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date_read,
    }

    books.append(new_book)
    save_books(books)
    print(f"Книга '{title}' успешно добавлена!")
