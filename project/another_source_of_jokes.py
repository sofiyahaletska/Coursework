import requests
import json


def new_joke2():
    """
    Makes request to API Joke and gets a response in json format. Then from this json this function extracts text of
    the joke and return it.
    :return:
    """
    url = "https://joke3.p.rapidapi.com/v1/joke"

    headers = {
        'x-rapidapi-host': "joke3.p.rapidapi.com",
        'x-rapidapi-key': "95bf6ad4a9mshf282d172c8f84d3p1998eajsn92f3bbf892b7"
        }

    response = requests.request("GET", url, headers=headers)
    response = json.loads(response.text)
    if '"' in response['content']:
        response['content'] = response['content'].replace('"', "'")
    joke2 = response['content']
    return joke2
