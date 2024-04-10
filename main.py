import requests
import json

def fetch(url):
    try:
        response = requests.get(url)
        print(response)

        # Print the status code and response text for debugging
        #print(f"Status Code: {response.status_code}")
        #print(f"Response Content: {response.text}")

        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        return None


def save_to_file(data, filename='mix.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        # Convert the JSON object to a string
        #json_string = json.dumps(data, ensure_ascii=False, indent=4)
        file.write(data)

url = 'https://raw.githubusercontent.com/yebekhe/TVC/main/lite/subscriptions/singbox/mix.json'
url2 = 'https://raw.githubusercontent.com/yebekhe/TVC/main/lite/subscriptions/singbox/mix.json'
cleaned_data = fetch(url)
cleaned_data2 = fetch(url2)

if cleaned_data is not None:
    save_to_file(cleaned_data, "mix.json")
else:
    print("No data to save.")

if cleaned_data2 is not None:
    save_to_file(cleaned_data2, "mix2.json")
else:
    print("No data to save.")
