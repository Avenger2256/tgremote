import json
import os

def save(data):
    try:
        with open("settings.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception:
        pass

def load():
    if not os.path.exists("settings.json"):
        return "NoFile error"
    try:
        with open("settings.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except (json.JSONDecodeError, Exception):
        return "Decode/Other error"

def start():
	cfg = load()
	token = input('Enter bot token: ')
	cfg['token']=token
	save(cfg)
	

if __name__ == '__main__':
    start()