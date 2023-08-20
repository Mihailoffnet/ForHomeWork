class FlatIterator:
    def __init__(self, list_of_list):
        self.list = list_of_list
        self.list_cursor = -1
        self.list_len = len(self.list)

    def __iter__(self):
        self.list_cursor += 1
        self.val_cursor = 0
        return self

    def __next__(self):
        if self.val_cursor == len(self.list[self.list_cursor]):
            iter(self)
        if self.list_cursor >= self.list_len:
            raise StopIteration
        self.val_cursor += 1     
        return self.list[self.list_cursor][self.val_cursor-1]

# Проверяем работу итератора
# list_of_lists_1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None]
# ]

# if __name__ == '__main__':
#     for item in FlatIterator(list_of_lists_1):
#         print(item)


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

