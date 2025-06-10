# BooksCollector Unit Tests

Реализованы тесты:

1. `test_add_new_book_success` — добавление валидной книги.
2. `test_add_new_book_invalid_length` — проверка длины названия (пустое или >40).
3. `test_add_new_book_duplicate` — проверка дублирования.
4. `test_set_book_genre_success` — корректное присвоение жанра.
5. `test_set_book_genre_nonexistent` — присвоение жанра отсутствующей книге.
6. `test_set_book_genre_invalid_genre` — неверный жанр.
7. `test_get_books_with_specific_genre` — фильтр по жанру.
8. `test_get_books_for_children_excludes_age_rating` — фильтр детских книг.
9. `test_add_and_delete_favorites` — добавление и удаление из избранных.
10. `test_add_favorites_only_existing` — нельзя добавить постороннюю книгу.

## Запуск тестов

```bash
pytest -v test_books_collector.py