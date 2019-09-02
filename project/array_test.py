from unittest import TestCase
from arrays import Array, DynamicArray


class TestArray(TestCase):

    def setUp(self):
        self.arr = Array(13)

    def test_init(self):
        self.assertEqual(self.arr._size, 13)
        for i in range(len(self.arr._elements)):
            self.assertTrue(self.arr._elements[i] is None)

    def test_len(self):
        self.assertEqual(self.arr._size, len(self.arr))

    def test_getitem(self):
        self.assertEqual(self.arr[0], self.arr._elements[0])

    def test_setitem(self):
        self.arr[0] = "item"
        self.assertEqual(self.arr[0], "item")

    def test_clear(self):
        self.arr[0] = "item"
        self.assertEqual(self.arr[0], "item")
        self.arr.clear(None)
        for i in range(len(self.arr._elements)):
            self.assertTrue(self.arr._elements[i] is None)

    def test_str(self):
        self.assertEqual(type(str(self.arr)), str)


class TestDynamicArray(TestCase):

    def setUp(self):
        self.arr = DynamicArray()
        self.arr.append("item1")
        self.arr.append("item2")

    def test_init(self):
        self.assertEqual(self.arr._n, 2)

    def test_len(self):
        self.assertEqual(self.arr._n, len(self.arr))

    def test_getitem(self):
        self.assertEqual(self.arr[0], self.arr._A[0])

    def test_append(self):
        self.arr.append("item3")
        self.assertEqual(self.arr[0], "item1")
        self.assertEqual(self.arr[1], "item2")
        self.assertEqual(self.arr[2], "item3")
        self.assertEqual(len(self.arr), 3)

    def test_resize(self):
        self.arr._resize(3)
        self.assertEqual(self.arr._A._size, 3)

    def test_make_array(self):
        self.assertEqual(type(self.arr._make_array(13)), Array)

    def test_insert(self):
        self.arr._resize(2)
        self.arr.insert(0, "item0")
        self.assertEqual(self.arr._A._size, 3)
        self.assertEqual(self.arr._A[0], "item0")
        self.assertEqual(self.arr._n, 3)

    def test_remove(self):
        self.arr.insert(1, "item1_2")
        self.arr.remove("item1")
        self.assertEqual(self.arr._n, 2)

    def test_str(self):
        self.assertEqual(type(str(self.arr)), str)

    def test_pop(self):
        self.arr.insert(2, "item3")
        last = self.arr._A[self.arr._n - 1]
        self.assertEqual(self.arr.pop(), last)
        self.assertEqual(self.arr._n, 2)

    def test_clear(self):
        self.assertEqual(self.arr[0], "item1")
        self.assertEqual(self.arr[1], "item2")
        self.arr.clear()
        for i in range(len(self.arr._A)):
            self.assertTrue(self.arr._A[i] is None)
        self.assertTrue(self.arr._n == 0)
