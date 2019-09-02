# coding=utf8
def add_end(words):
    """
    Makes the end of the main html page. I can`t make all html page with one function and needed a another function
     to avoid some issues.
    :param words:
    :return:
    """
    end = """
    <p>Виберіть нові для вас слова.</p>
    <p>Для того, щоб вибрати більше ніж одне слово - затисніть Cntr(Windows) або Command (Mac)</p>
    <form method="POST" action="dictionary_append" >
    <select name="words" size="{0}" multiple>
    {1}
    </select>
    <input type="submit" value="Записати слова в словник"><br>
    </form>
    <form method="GET" action="next_joke" >
    <input type="submit" value="Наступний жарт"><br>
    </form>
    <form method="GET" action="dictionary_show" >
    <input type="submit" value="Показати словник"><br>
    </form>
    </body>
    </html>
    """
    options = """"""
    for word in words:
        options += """<option value="{0}">{1}</option>""".format(word, word) + "\n"
    end = end.format(len(words), options)
    return end
