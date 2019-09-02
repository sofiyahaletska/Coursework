from dictionary_class import Dictionary
from unittest import TestCase


class TestDictionary(TestCase):

    def setUp(self):
        self.fw = Dictionary("nine", "���'���")
        self.sw = Dictionary("ice", "��")

    def test_init(self):
        self.assertEqual(self.fw.word, "nine")
        self.assertEqual(self.fw.value, "���'���")
        self.assertEqual(self.sw.word, "ice")
        self.assertEqual(self.sw.value, "��")

    def test_repr(self):
        self.assertEqual(self.fw.__repr__(), "nine - ���'���")
        self.assertEqual(self.sw.__repr__(), "ice - ��")
