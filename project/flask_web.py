# coding=utf8
from flask import Flask, request, render_template
import generate_html_with_new_joke
from generate_html_with_new_joke import update_page
from make_dictionary_txt import make_txt
from form_dictionary import create_dict, add_new_word
from make_dictionary_html_page import make_dictionary_html
app = Flask(__name__)
app.config['DEBUG'] = True
global dictionary
dictionary = create_dict()
@app.route("/", methods=['GET', 'POST'])
def home():
    """
    Returns starting page.
    :return:
    """
    page = update_page()
    f = open("templates/main.html", "w", encoding='utf-8')
    f.write(page)
    f.close()
    return page


@app.route("/next_joke", methods=['GET', 'POST'])
def next_joke():
    """
    Reloads page to present new joke.
    :return:
    """
    page = update_page()
    f = open("templates/main.html", "w", encoding='utf-8')
    f.write(page)
    f.close()
    return page


@app.route("/dictionary_append", methods=['GET', 'POST'])
def dictionary_append():
    """
    Appends dictionary with words selected by user.
    :return:
    """
    words = request.form.getlist('words')
    for word in words:
        add_new_word(word, dictionary)
    make_txt(dictionary)
    f = open("templates/main.html", "r", encoding='utf-8')
    text = f.read()
    return text


@app.route("/dictionary_show", methods=['GET', 'POST'])
def dictionary_show():
    """
    Shows page with dictionary.
    :return:
    """
    return make_dictionary_html()


@app.route("/return_to_home", methods=['GET', 'POST'])
def return_to_home():
    """
    Returns to homepage from dictionary page.
    :return:
    """
    f = open("templates/main.html", "r", encoding='utf-8')
    text = f.read()
    return text


if __name__ == "__main__":
    app.run(debug=True)
