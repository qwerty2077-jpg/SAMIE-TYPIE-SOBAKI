import os
import requests
import shutil
FOLDER = "КАРТИНКЭЭЭЭ"
URL = 'https://random.dog/woof.json/'
PAYLOAD = {
    "filter": "mp4,webm"
}

def download_picture(FOLDER, file_name, URL):
    file_path = os.path.join(FOLDER, file_name)
    response = requests.get(URL,params=PAYLOAD) 
    with open(file_path, 'wb') as file:
        file.write(response.content)
def main():
    if os.path.isdir(FOLDER):
        shutil.rmtree(FOLDER)
    os.mkdir(FOLDER)
    for number in range(50):
        response = requests.get(URL,params=PAYLOAD)    
        response.raise_for_status()
        picture_link = response.json()['URL']
        link, picture_extension = os.path.splitext(picture_link)
        file_name = f'dog_{number+1}{picture_extension}'
        download_picture(FOLDER, file_name, picture_link)

if __name__ == '__name__':
    main()