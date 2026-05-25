import json
import os
from collections import defaultdict

FILENAME = "books.json"


def load_books():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_books(books):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


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


def show_all_books():
    books = load_books()
    print("\n--- Список всех книг ---")
    if not books:
        print("Ваш трекер пока пуст.")
        return

    for idx, book in enumerate(books, start=1):
        print(
            f"{idx}. {book['author']} — «{book['title']}» | Оценка: {book['rating']}/5 | Дата: {book['date_read']}"
        )


def show_average_rating():
    books = load_books()
    print("\n--- Средняя оценка ---")
    if not books:
        print("Нет книг для расчета средней оценки.")
        return

    total_rating = sum(book["rating"] for book in books)
    avg_rating = total_rating / len(books)
    print(
        f"Всего книг: {len(books)}. Средняя оценка всех прочитанных книг: {avg_rating:.2f}"
    )


def show_author_stats():
    books = load_books()
    print("\n--- Статистика по авторам ---")
    if not books:
        print("Нет данных для составления статистики.")
        return

    stats = defaultdict(int)
    for book in books:
        stats[book["author"]] += 1

    for author, count in stats.items():
        print(f"Автор: {author} — Прочитано книг: {count}")


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
