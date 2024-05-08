import json
from database import dados

object_json = json.dumps(dados, indent=4)

with open("C:/inetpub/wwwroot/assets/data/dashboard.json", "w") as file:
    file.write(object_json)
