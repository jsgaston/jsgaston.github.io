import os
import json
#
folder_path = 'Musica'  # Ruta de la carpeta ¿funcionas?
try:
    music_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    with open('music_list.json', 'w') as json_file:
        json.dump(music_files, json_file)

    print("JSON generado exitosamente.")
except Exception as e:
    print("Error durante la generación del JSON:", str(e))

