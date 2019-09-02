import arrays
import dictionary_class
from translation import translate_to_uk
from google.cloud import translate_v3beta1 as translate
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/shale/Downloads/artful-memento-250518-2de2b5613887.json'


def create_dict():
    """
    Creates dictionary.
    :return:
    """
    dictionary = arrays.DynamicArray()
    return dictionary


def add_new_word(word, dictionary):
    """
    Adds new word to the dictionary.
    :param word:
    :param dictionary:
    :return:
    """
    dictionary.append(dictionary_class.Dictionary(word, translate_to_uk(word)))
