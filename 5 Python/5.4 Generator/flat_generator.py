import types


def flat_generator(list_of_lists):
    list_cursor = 0
    list_len = len(list_of_lists)
    while list_cursor < list_len:
        val_cursor = 0
        for _ in list_of_lists[list_cursor]:
            item = list_of_lists[list_cursor][val_cursor]
            yield item
            val_cursor +=1
        list_cursor += 1

# Проверяем работу генератора
# if __name__ == '__main__':
#     list_of_lists_1 = [
#             ['a', 'b', 'c'],
#             ['d', 'e', 'f', 'h', False],
#             [1, 2, None]
#         ]

#     for item in flat_generator(list_of_lists_1):
#         print(item)

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    