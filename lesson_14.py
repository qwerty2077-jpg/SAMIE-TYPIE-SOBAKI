import os
import requests
import shutil
folder = "КАРТИНКЭЭЭЭ"
url = 'https://random.dog/woof.json/'
payload = {
    "filter": "mp4,webm"
}
def download_picture(folder, file_name, url):
    file_path = os.path.join(folder, file_name)
    response = requests.get(url,params=payload)
    with open(file_path, 'wb') as file:
        file.write(response.content)


def main():
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)
    for number in range(50):
        response = requests.get(url,params=payload)
        response.raise_for_status()
        picture_link = response.json()['url']
        link, picture_extension = os.path.splitext(picture_link)
        file_name = f'dog_{number+1}{picture_extension}'
        download_picture(folder, file_name, picture_link)
if __name__ == '__name__':
    main()