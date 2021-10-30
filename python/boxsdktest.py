from boxsdk import DevelopmentClient
client = DevelopmentClient()

foldername = '147514427103'
folder = client.folder(folder_id=foldername).get()

for item in folder.item_collection['entries']:
    print(f"{item.name}, {item.id}")
