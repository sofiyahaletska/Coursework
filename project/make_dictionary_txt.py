def make_txt(dictionary):
    """
    Makes dictionary txt file.
    :param dictionary:
    :return:
    """
    f = open("dictionary.txt", "w")
    f.write(str(dictionary))
