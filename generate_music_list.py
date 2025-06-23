import requests
import json
from random import shuffle

BASE_URL = "https://raw.githubusercontent.com/jsgaston/Musica_assets_00{}/main/song_list00{}.json"
combined_songs = []

for i in range(1, 5):  # 001 a 004
    repo_num = f"{i:03}"
    url = BASE_URL.format(repo_num, repo_num)
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        combined_songs.extend(data)
        print(f"Cargadas {len(data)} canciones desde {url}")
    except Exception as e:
        print(f"Error al cargar {url}: {e}")

shuffle(combined_songs)

with open("music_list.json", "w", encoding="utf-8") as f:
    json.dump(combined_songs, f, ensure_ascii=False, indent=2)

print(f"Total de canciones combinadas: {len(combined_songs)}")
