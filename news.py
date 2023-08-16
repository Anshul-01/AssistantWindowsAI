def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

def newsHeadlines(url,i):
    import requests
    import json
    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    return my_json['articles'][i]['title']


if __name__ == '__main__':
    
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=439913c16a5644c7a165664f0bccdeed')
    newsHeadlines(url)
    