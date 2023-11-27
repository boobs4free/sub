import requests

def fetch(url):
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        print("Response content:", response.text)
        return None

url = 'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/singbox/sfasfi/mix.json'
cleaned_data = fetch(url)

if cleaned_data is not None:
    save_to_file(cleaned_data)
else:
    print("No data to save.")
