class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list


    def __iter__(self):
        self.count_1 = 0
        self.count_2 = 0

        self.count_len_1 = len(self.list_of_list)
        self.count_len_2 = None
        return self

    def __next__(self):
        if self.count_1 >= self.count_len_1:
            raise StopIteration

        if not self.count_len_2:
            self.count_len_2 = len(self.list_of_list[self.count_1])

        item = self.list_of_list[self.count_1][self.count_2]
        self.count_2 += 1

        if self.count_2 >= self.count_len_2:
            self.count_2 = 0
            self.count_1 += 1
            self.count_len_2 = None

        return item


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