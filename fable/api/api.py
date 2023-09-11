import requests
import json
from fable.credentials import api_key


def get_results(arr_keys):
    if len(arr_keys) == 0:
        return ['No useful information could be inferred from the given text.']
    else:
        for i in arr_keys:
            phrase = i[0]
            lst_phrase = phrase.split()
            if len(lst_phrase) == 0 or len(lst_phrase) == 1:
                continue
            phrase_str = '+'.join(lst_phrase)
            request_string = 'https://newsdata.io/api/1/news?apikey={}&language=en&q="{}"'.format(
                api_key, phrase_str)

            print(request_string)

            request_json = requests.get(request_string).json()
            if request_json['totalResults'] > 0:
                description = request_json['results'][0]['description']
                content = request_json['results'][0]['content']
                pub_date = request_json['results'][0]['pubDate']
                source = request_json['results'][0]['source_id']
                return [description, content, pub_date, source]
        else:
            return ['No recent news on the requested information could be found.']
