from dictionary_class import Dictionary
from unittest import TestCase


class TestDictionary(TestCase):

    def setUp(self):
        self.fw = Dictionary("nine", "дев'ять")
        self.sw = Dictionary("ice", "лід")

    def test_init(self):
        self.assertEqual(self.fw.word, "nine")
        self.assertEqual(self.fw.value, "дев'ять")
        self.assertEqual(self.sw.word, "ice")
        self.assertEqual(self.sw.value, "лід")

    def test_repr(self):
        self.assertEqual(self.fw.__repr__(), "nine - дев'ять")
        self.assertEqual(self.sw.__repr__(), "ice - лід")
