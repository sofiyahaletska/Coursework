import requests
import json


def new_joke1():
    """
    Makes request to JokeAPI and gets a response in json format. Then from this json this function extracts text of
    the joke and return it.
    :return:
    """
    url = "https://jokeapi.p.rapidapi.com/category/Any"

    querystring = {"format": "json"}

    headers = {
        'x-rapidapi-host': "jokeapi.p.rapidapi.com",
        'x-rapidapi-key': "95bf6ad4a9mshf282d172c8f84d3p1998eajsn92f3bbf892b7"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = json.loads(response.text)

    if response['type'] == "twopart":
        if '"' in response['setup'] or '"' in response['delivery']:
            response['setup'] = response['setup'].replace('"', "'")
            response['delivery'] = response['delivery'].replace('"', "'")
        joke1 = response['setup'] + "\n" + response['delivery']
    else:
        if '"' in response['joke']:
            response['joke'] = response['joke'].replace('"', "'")
        joke1 = response['joke']
    return joke1
