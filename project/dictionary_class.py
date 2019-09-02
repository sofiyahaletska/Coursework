class Dictionary:
    """
    Creates an item with word and its translation.
    """
    def __init__(self, word, value):
        """
        Create a piece of dictionary
        Initialize each element.
        :param word:
        :param value:
        """
        self.word = word
        self.value = value

    def __repr__(self):
        """
        Returns a representation of class.
        :return:
        """
        return "{0} - {1}".format(self.word, self.value)
