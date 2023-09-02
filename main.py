import requests
import re
import json
import random
import string


def fetch(url):
    # Fetch the JSON from the provided URL
    response = requests.get(url)
    data = response.json()

    return data

def save_to_file(data, filename='mix.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

url = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/singbox/sfasfi/mix.json'
cleaned_data = fetch(url)

# Save the cleaned JSON data to a new file
save_to_file(cleaned_data)
