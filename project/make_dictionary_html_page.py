# coding=utf8
def make_dictionary_html():
    """
    Makes dictionary html.
    :return:
    """
    r = open("dictionary.txt", "r").readlines()
    wrapper = """<html>
        <head>
            <meta charset=utf-8>  
            <title>Funny English</title>
        </head>
        <body>{0}
    <form method="GET" action="return_to_home" >
    <input type="submit" value="Повернутися на головну"><br>
    </form>
    </body>
    </html>
        """
    s = ""
    for line in r:
        s += "<p>" + line + "</p>\n"
    whole = wrapper.format(s)
    return whole
