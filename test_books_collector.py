import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book_success(collector):
    collector.add_new_book('Книга1')
    assert 'Книга1' in collector.get_books_genre()

@pytest.mark.parametrize('name', ['', 'A'*41])
def test_add_new_book_invalid_length(collector, name):
    collector.add_new_book(name)
    assert name not in collector.get_books_genre()

def test_add_new_book_duplicate(collector):
    collector.add_new_book('КнигаX')
    collector.add_new_book('КнигаX')
    assert list(collector.get_books_genre().keys()).count('КнигаX') == 1

def test_set_book_genre_success(collector):
    collector.add_new_book('КнигаЖанр')
    collector.set_book_genre('КнигаЖанр', 'Фантастика')
    assert collector.get_book_genre('КнигаЖанр') == 'Фантастика'

def test_set_book_genre_nonexistent(collector):
    collector.set_book_genre('НетКниги', 'Фантастика')
    assert collector.get_book_genre('НетКниги') is None

def test_set_book_genre_invalid_genre(collector):
    collector.add_new_book('Книга2')
    collector.set_book_genre('Книга2', 'Неизвестно')
    assert collector.get_book_genre('Книга2') == ''

def test_get_books_with_specific_genre(collector):
    collector.add_new_book('КнигаA')
    collector.add_new_book('КнигаB')
    collector.set_book_genre('КнигаA', 'Комедии')
    assert collector.get_books_with_specific_genre('Комедии') == ['КнигаA']

def test_get_books_for_children_excludes_age_rating(collector):
    collector.add_new_book('К1'); collector.set_book_genre('К1', 'Ужасы')
    collector.add_new_book('К2'); collector.set_book_genre('К2', 'Комедии')
    assert collector.get_books_for_children() == ['К2']

def test_add_and_delete_favorites(collector):
    collector.add_new_book('FavBook')
    collector.add_book_in_favorites('FavBook')
    assert collector.get_list_of_favorites_books() == ['FavBook']
    collector.delete_book_from_favorites('FavBook')
    assert collector.get_list_of_favorites_books() == []

def test_add_favorites_only_existing(collector):
    collector.add_book_in_favorites('NoBook')
    assert collector.get_list_of_favorites_books() == []
