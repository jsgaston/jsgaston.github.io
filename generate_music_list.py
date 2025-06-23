import requests
import json
from random import shuffle

BASE_URL ="https://raw.githubusercontent.com/jsgaston/Musica_assets_{}/main/song_list{}.json" #"https://raw.githubusercontent.com/jsgaston/Musica_assets_00{}/refs/heads/main/song_list00{}.json"  #  
combined_songs = []

for i in range(1, 5):  # 001 a 004
    repo_num = f"{i:03}"
    url = BASE_URL.format(repo_num, repo_num)
    try:
        print(f"Descargando: {url}")
        r = requests.get(url)
        r.raise_for_status()  # Esto lanza error si el archivo no existe
        data = r.json()
        if isinstance(data, list):
            combined_songs.extend(data)
            print(f"✓ {len(data)} canciones añadidas")
        else:
            print(f"⚠️ El contenido no es una lista en {url}")
    except Exception as e:
        print(f"❌ Error al descargar {url}: {e}")

# Verifica si hay canciones
if not combined_songs:
    print("🚫 No se añadieron canciones. Revisa las URLs de origen.")
else:
    shuffle(combined_songs)
    with open("music_list.json", "w", encoding="utf-8") as f:
        json.dump(combined_songs, f, ensure_ascii=False, indent=2)
    print(f"✅ Lista combinada generada con {len(combined_songs)} canciones")
