import requests
import re
import json
import random
import string

def generate_random_string(length=4):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def clean_string(value):
    # Regular expression to capture the pattern "@<any characters including . and _>"
    pattern_telegram = r'@[\w\._]+'
    replacement = generate_random_string()
    cleaned = re.sub(pattern_telegram, replacement, value)
    cleaned = cleaned.replace("رایگان", '').strip()
    return cleaned

def recursive_clean(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, str):
                data[key] = clean_string(value)
            else:
                recursive_clean(value)
    elif isinstance(data, list):
        for i in range(len(data)):
            if isinstance(data[i], str):
                data[i] = clean_string(data[i])
            else:
                recursive_clean(data[i])
    return data

def fetch_and_clean_json_from_url(url):
    # Fetch the JSON from the provided URL
    response = requests.get(url)
    data = response.json()

    # Recursively clean the JSON
    cleaned_data = recursive_clean(data)

    return cleaned_data

def save_to_file(data, filename='mix.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

url = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/singbox/sfasfi/mix.json'
cleaned_data = fetch_and_clean_json_from_url(url)

# Save the cleaned JSON data to a new file
save_to_file(cleaned_data)
