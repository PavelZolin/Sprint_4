import pytest
from main import BooksCollector

def test_add_new_book_success(collector):
    """
    Проверяет успешное добавление новой книги с корректным именем.
    """
    collector.add_new_book('Книга1')
    assert 'Книга1' in collector.get_books_genre()

@pytest.mark.parametrize('name', ['', 'A'*41])
def test_add_new_book_invalid_length(collector, name):
    """
    Проверяет, что книги с некорректной длиной имени не добавляются.
    Параметризованный тест: пустая строка и строка длиной 41 символ.
    """
    collector.add_new_book(name)
    assert name not in collector.get_books_genre()

def test_add_new_book_duplicate(collector):
    """
    Проверяет, что одну и ту же книгу нельзя добавить дважды.
    """
    collector.add_new_book('КнигаX')
    initial_books_count = len(collector.get_books_genre())
    collector.add_new_book('КнигаX')
    assert len(collector.get_books_genre()) == initial_books_count
    assert list(collector.get_books_genre().keys()).count('КнигаX') == 1


def test_set_book_genre_success(collector):
    """
    Проверяет успешную установку жанра существующей книге.
    """
    collector.add_new_book('КнигаЖанр')
    collector.set_book_genre('КнигаЖанр', 'Фантастика')
    assert collector.get_book_genre('КнигаЖанр') == 'Фантастика'

def test_set_book_genre_nonexistent_book(collector):
    """
    Проверяет, что нельзя установить жанр для несуществующей книги.
    """
    collector.set_book_genre('НетКниги', 'Фантастика')
    assert collector.get_book_genre('НетКниги') is None

def test_set_book_genre_invalid_genre(collector):
    """
    Проверяет, что нельзя установить невалидный жанр.
    Жанр должен остаться пустым, если был пустым.
    """
    collector.add_new_book('Книга2')
    collector.set_book_genre('Книга2', 'Неизвестно')
    assert collector.get_book_genre('Книга2') == ''

def test_get_books_with_specific_genre(collector):
    """
    Проверяет получение списка книг по конкретному жанру.
    """
    collector.add_new_book('КнигаA')
    collector.add_new_book('КнигаB')
    collector.set_book_genre('КнигаA', 'Комедии')
    collector.set_book_genre('КнигаB', 'Комедии') # Добавим вторую книгу того же жанра
    assert collector.get_books_with_specific_genre('Комедии') == ['КнигаA', 'КнигаB']
    assert collector.get_books_with_specific_genre('Ужасы') == [] # Проверка отсутствия книг

def test_get_books_for_children_excludes_age_rating(collector):
    """
    Проверяет, что книги с возрастным рейтингом не попадают в список для детей.
    """
    collector.add_new_book('К1')
    collector.set_book_genre('К1', 'Ужасы') # Возрастной рейтинг
    collector.add_new_book('К2')
    collector.set_book_genre('К2', 'Комедии') # Для детей
    collector.add_new_book('К3')
    collector.set_book_genre('К3', 'Фантастика') # Для детей
    assert sorted(collector.get_books_for_children()) == sorted(['К2', 'К3']) # Используем sorted для сравнения списков
    assert 'К1' not in collector.get_books_for_children()

def test_get_books_genre_returns_dict(collector):
    """
    Проверяет, что метод get_books_genre возвращает словарь.
    (Добавлен по замечанию ревьюера)
    """
    collector.add_new_book('Книга0')
    collector.set_book_genre('Книга0', 'Фантастика')
    result = collector.get_books_genre()
    assert isinstance(result, dict)
    assert result == {'Книга0': 'Фантастика'}

    empty_collector = BooksCollector()
    assert empty_collector.get_books_genre() == {}


def test_add_book_in_favorites_success(collector):
    """
    Проверяет успешное добавление книги в избранное.
    (Разделен на отдельный тест по замечанию ревьюера)
    """
    collector.add_new_book('FavBook')
    collector.add_book_in_favorites('FavBook')
    assert 'FavBook' in collector.favorites

def test_add_favorites_only_existing(collector):
    """
    Проверяет, что в избранное можно добавить только существующую книгу.
    """
    collector.add_book_in_favorites('NoBook')
    assert collector.get_list_of_favorites_books() == []

def test_add_book_in_favorites_duplicate(collector):
    """
    Проверяет, что одну и ту же книгу нельзя добавить в избранное дважды.
    """
    collector.add_new_book('КнигаДубликат')
    collector.add_book_in_favorites('КнигаДубликат')
    initial_fav_count = len(collector.favorites)
    collector.add_book_in_favorites('КнигаДубликат')
    assert len(collector.favorites) == initial_fav_count
    assert collector.favorites.count('КнигаДубликат') == 1


def test_delete_book_from_favorites_success(collector):
    """
    Проверяет успешное удаление книги из избранного.
    (Разделен на отдельный тест по замечанию ревьюера)
    """
    collector.add_new_book('FavBook2')
    collector.add_book_in_favorites('FavBook2')
    assert 'FavBook2' in collector.favorites
    collector.delete_book_from_favorites('FavBook2')
    assert 'FavBook2' not in collector.favorites
    assert collector.favorites == [] # Если это был единственный элемент

def test_delete_book_from_favorites_nonexistent(collector):
    """
    Проверяет, что удаление несуществующей книги из избранного не вызывает ошибок.
    """
    initial_favorites = collector.favorites.copy()
    collector.delete_book_from_favorites('Несуществующая в избранном')
    assert collector.favorites == initial_favorites # Список избранного не изменился


def test_get_list_of_favorites_books_returns_list(collector):
    """
    Проверяет, что метод get_list_of_favorites_books возвращает список избранных книг.
    (Добавлен по замечанию ревьюера)
    """
    collector.add_new_book('ЛюбимаяКнига1')
    collector.add_new_book('ЛюбимаяКнига2')
    collector.add_book_in_favorites('ЛюбимаяКнига1')
    collector.add_book_in_favorites('ЛюбимаяКнига2')
    result = collector.get_list_of_favorites_books()
    assert isinstance(result, list)
    assert result == ['ЛюбимаяКнига1', 'ЛюбимаяКнига2']

    empty_collector = BooksCollector()
    assert empty_collector.get_list_of_favorites_books() == []