import random
from TTS_request import make_url
from translation import translate_to_uk
from google.cloud import translate_v3beta1 as translate
import os
from programming_jokes import new_joke1
from another_source_of_jokes import new_joke2
from make_end_of_html import add_end
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/shale/Downloads/artful-memento-250518-2de2b5613887.json'


def update_page():
    """
    Makes new updated page with a new joke.
    :return:
    """
    joke1 = new_joke1()
    joke2 = new_joke2()
    wrapper = """<html>
    <head>
        <meta charset=utf-8>  
        <title>Funny English</title>
    </head>
    <body>{0}
    <p>Переклад:</p>
    <p><b>{1}</b></p>
    <p>English (Australia)</p>
    <audio controls="" name="en-au">
    <source src="{2}" type="audio/wav"></audio>
    <p>English (Canada)</p>
    <audio controls="" name="en-ca">
    <source src="{3}" type="audio/wav"></audio>
    <p>English (Great Britain)</p>
    <audio controls="" name="en-gb">
    <source src="{4}" type="audio/wav"></audio>
    <p>English (India)</p>
    <audio controls="" name="en-in">
    <source src="{5}" type="audio/wav"></audio>
    <p>English (United States)</p>
    <audio controls="" name="en-us">
    <source src="{6}" type="audio/wav"></audio>
    """
    joke = random.choice([joke1, joke2])
    words = joke.split()
    words = set(words)
    words = list(words)
    end = add_end(words)
    whole = wrapper.format(joke, translate_to_uk(joke), make_url("en-au", joke), make_url("en-ca", joke),
                           make_url("en-gb", joke), make_url("en-in", joke), make_url("en-us", joke))
    return whole + "\n" + end
