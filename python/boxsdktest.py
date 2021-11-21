from boxsdk import OAuth2, Client
from flask import Flask
import datetime
import re
import json
from python import config

oauth = OAuth2(
    client_id=config.client_id,
    client_secret=config.client_secret,
)
client = Client(oauth)
app = Flask(__name__)

foldername = '125566015976'
folder = client.folder(folder_id=foldername).get()

yearSearch = re.compile(r'-\d\d(\d\d)')

maxYear = 0
shortest = 0
id = ""

for item in folder.item_collection['entries']:
    result = yearSearch.search(item.name)
    thisYear = int(result.group(1))
    length = len(result.group(0))
    if (thisYear > maxYear):
        maxYear = thisYear
        id = item.id
    elif ((thisYear == maxYear) and (len(id) > len(item.id))):
        id = item.id

semesterPlans = json.loads('{"files": []}')

subfolder = client.search().query(query=".pdf", limit=200, file_extensions=['pdf'], ancestor_folder_ids=[id])
for item in subfolder:
    file = json.loads('{}')
    parent_folders = {'parent_folders': [x.name for x in item.path_collection['entries']].copy()}
    name = {'name': item.name}
    url = {'url': client.file(item.id).get_url()}
    file.update(parent_folders)
    file.update(name)
    file.update(url)
    semesterPlans['files'].append(file)

print(json.dumps(semesterPlans, indent = 4))

@app.route("/files.json")
def index():
    return str(json.dumps(semesterPlans))

if __name__ == "__main__":
    app.run()
