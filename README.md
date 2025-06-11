# BooksCollector Unit Tests

**Особенности:**
- Фикстура `collector` вынесена в `conftest.py`
- Тесты на каждый метод, включая:
  - `get_books_genre()` — проверяет тип dict и наличие ключа.
  - Раздельные тесты для добавления и удаления избранного.
- Используется параметризация в тестах `add_new_book`.

## Список тестов

1. `test_add_new_book_success`
2. `test_add_new_book_invalid_length`
3. `test_add_new_book_duplicate`
4. `test_set_book_genre_success`
5. `test_set_book_genre_nonexistent_book`
6. `test_set_book_genre_invalid_genre`
7. `test_get_books_with_specific_genre`
8. `test_get_books_for_children_excludes_age_rating`
9. `test_get_books_genre_returns_dict`
10. `test_add_book_in_favorites_success`
11. `test_add_favorites_only_existing`
12. `test_add_book_in_favorites_duplicate`
13. `test_delete_book_from_favorites_success`
14. `test_delete_book_from_favorites_nonexistent`
15. `test_get_list_of_favorites_books_returns_list`

## Запуск тестов

```bash
pytest -v