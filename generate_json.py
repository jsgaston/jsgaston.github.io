import requests
from bs4 import BeautifulSoup
import json

# Repositorios de donde extraer
repos = [
    "https://github.com/jsgaston/Musica_assets_001",
    "https://github.com/jsgaston/Musica_assets_002",
    "https://github.com/jsgaston/Musica_assets_003",
    "https://github.com/jsgaston/Musica_assets_004"
]

# Extensiones de archivos permitidas
valid_extensions = ['.mp3', '.m4a', '.wav', '.ogg']

# Base para raw.githubusercontent
def github_raw_url(repo, file_path):
    parts = repo.replace("https://github.com/", "").split('/')
    user, repo_name = parts[0], parts[1]
    return f"https://raw.githubusercontent.com/{user}/{repo_name}/main/{file_path}"

playlist = []

for repo in repos:
    print(f"🕵️‍♂️ Analizando {repo}...")
    res = requests.get(repo)
    if res.status_code != 200:
        print(f"⚠️ Error al acceder a {repo}")
        continue

    soup = BeautifulSoup(res.text, 'html.parser')
    files = soup.select('a.js-navigation-open.Link--primary')

    for file_tag in files:
        file_name = file_tag.text.strip()
        if any(file_name.endswith(ext) for ext in valid_extensions):
            raw_url = github_raw_url(repo, file_name)
            playlist.append(raw_url)

# Guardar en JSON
with open("music_list.json", "w") as f:
    json.dump(playlist, f, indent=2)

print(f"✅ {len(playlist)} canciones añadidas.")
