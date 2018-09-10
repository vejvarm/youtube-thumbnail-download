# Download thumbnail images in max resolution from YouTube videos specified by an url
import sys
import re
import requests

from bs4 import BeautifulSoup


def check_url(url):
    # check if it is actually a valid YouTube link using regexp
    youtube = re.compile(r'(https?://)?(w{3}\.)?(youtube.com/watch\?v=|youtu.be/).{11}')

    return True if youtube.match(url) else False


def get_page():
    """ read url input by the user and return the source code of the requested page"""

    try:
        url = sys.argv[1]
    except IndexError:
        print('No url specified in the arguments.')
        sys.exit()

    if check_url(url):
        try:
            response = requests.get(url)
        except requests.exceptions.MissingSchema:  # catch if url doesn't have http(s):// at the beginning
            response = requests.get("https://" + url)

        return response.text
    else:
        raise ValueError("The url doesn't seem to be a valid YouTube address.")


def get_thumbnail_url():
    """ get the url of the thumbnail image in max resolution"""

    try:
        html = get_page()
    except ValueError:
        raise

    soup = BeautifulSoup(html, 'html.parser')

    thumbnail = soup.find("meta", property="og:image")

    if thumbnail:
        return thumbnail["content"]
    else:
        raise ValueError("Property og:image not found.")


def save_thumbnail():
    thumb_url = get_thumbnail_url()
    thumb_data = requests.get(thumb_url).content

    folder = './'
    filename = 'yt-thumb-{}.{}'.format(thumb_url[-29:-18], thumb_url[-3:])

    with open(folder + filename, 'wb') as image:
        image.write(thumb_data)

    print("Thumbnail url: {}".format(thumb_url))
    print("Thumbnail saved to {}{}".format(folder, filename))


if __name__ == '__main__':
    save_thumbnail()
