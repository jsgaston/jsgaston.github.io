import requests
import json
from random import shuffle

# Base de URL para los JSON en GitHub
BASE_URL = "https://raw.githubusercontent.com/jsgaston/Musica_assets_{}/main/song_list{}.json"

combined_songs = []

# Recorremos song_list001 a song_list004
for i in range(1, 6):  # Cambia el rango si tienes más
    repo_num = f"{i:03}"
    url = BASE_URL.format(repo_num, repo_num)
    try:
        print(f"📥 Descargando: {url}")
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()

        if isinstance(data, list):
            for song in data:
                # Aseguramos que todos los campos estén
                song_data = {
                    "title": song.get("title"),
                    "artist": song.get("artist"),
                    "album": song.get("album"),
                    "duration": song.get("duration"),
                    "genre": song.get("genre"),
                    "year": song.get("year"),
                    "filename": song.get("filename"),
                    "url": song.get("url")
                }
                combined_songs.append(song_data)
            print(f"✓ {len(data)} canciones añadidas")
        else:
            print(f"⚠️ Formato inesperado en {url}")

    except Exception as e:
        print(f"❌ Error al descargar {url}: {e}")

# Guardamos el resultado
if combined_songs:
    shuffle(combined_songs)
    with open("music_list.json", "w", encoding="utf-8") as f:
        json.dump(combined_songs, f, ensure_ascii=False, indent=2)
    print(f"✅ Generado music_list.json con {len(combined_songs)} canciones")
else:
    print("🚫 No se generó ninguna lista")
