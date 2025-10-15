import pytest
from main import average_rating, read_file


def test_read_file():
    test_case = [['name', 'brand', 'price', 'rating'],
                 ['iphone 15 pro', 'apple', '999', '4.9'],
                 ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
                 ['redmi note 12', 'xiaomi', '199', '4.6'],
                 ['iphone 14', 'apple', '799', '4.7'],
                 ['galaxy a54', 'samsung', '349', '4.2'],
                 ['poco x5 pro', 'xiaomi', '299', '4.4'],
                 ['iphone se', 'apple', '429', '4.1'],
                 ['galaxy z flip 5', 'samsung', '999', '4.6'],
                 ['redmi 10c', 'xiaomi', '149', '4.1'],
                 ['iphone 13 mini', 'apple', '599', '4.5']]
    path_ = ["products1.csv", "products2.csv"]
    path_1 = ["not existed file"]
    assert read_file(path_) == test_case
    with pytest.raises(FileNotFoundError) as e:
        read_file(path_1)
        assert e.type == FileNotFoundError


def test_avarege_rating():
    test_case = [['name', 'brand', 'price', 'rating'],
                 ['iphone 15 pro', 'apple', '999', '4.9'],
                 ['galaxy s23 ultra', 'samsung', '1199', '4.8'],
                 ['redmi note 12', 'xiaomi', '199', '4.6'],
                 ['iphone 14', 'apple', '799', '4.7'],
                 ['galaxy a54', 'samsung', '349', '4.2'],
                 ['poco x5 pro', 'xiaomi', '299', '4.4'],
                 ['iphone se', 'apple', '429', '4.1'],
                 ['galaxy z flip 5', 'samsung', '999', '4.6'],
                 ['redmi 10c', 'xiaomi', '149', '4.1'],
                 ['iphone 13 mini', 'apple', '599', '4.5']]
    test_case2 = []
    test_case3 = [[1]]
    test_case4 = [[]]
    ans = [[0, 'name', 'rating'],
           [1, 'iphone 15 pro', '4.9'],
           [2, 'galaxy s23 ultra', '4.8'],
           [3, 'iphone 14', '4.7'],
           [4, 'redmi note 12', '4.6'],
           [5, 'galaxy z flip 5', '4.6'],
           [6, 'iphone 13 mini', '4.5'],
           [7, 'poco x5 pro', '4.4'],
           [8, 'galaxy a54', '4.2'],
           [9, 'iphone se', '4.1'],
           [10, 'redmi 10c', '4.1']]
    assert average_rating(test_case) == ans
    assert average_rating(test_case2) == []
    assert average_rating(test_case3) == [[0, 1, 1]]
    with pytest.raises(IndexError) as e:
        average_rating(test_case4)
        assert e.type == IndexError


if __name__ == "__main__":
    test_avarege_rating()
    test_read_file()

