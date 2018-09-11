# Download thumbnail images in max resolution from YouTube videos specified by an url
import sys
import re
import requests

from os import (path, makedirs)
from bs4 import BeautifulSoup


# Custom error for input fail
class PropertyNotFoundError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def check_url(url):
    """ Check if url is actually a valid YouTube link using regexp.

    :param url: string url that is to be checked by regexp
    :return: boolean True if the url matches the regexp (it is a valid YouTube page), otherwise False
    """
    youtube = re.compile(r'(https?://)?(w{3}\.)?(youtube.com/watch\?v=|youtu.be/).{11}')

    return True if youtube.match(url) else False


def get_page():
    """ Read url input by the user and return the source code of the requested page.

    :return: string source code of the YouTube page specified by url
    """

    url = None

    while not url:

        url = input("\nEnter the YouTube address from which you want to download the thumbnail or 'q' to quit:\n")

        if url == 'q':
            sys.exit()

        if check_url(url):
            try:
                response = requests.get(url)
            except requests.exceptions.MissingSchema:  # catch if url doesn't have http(s):// at the beginning
                response = requests.get("https://" + url)

            return response.text
        else:
            print("The url doesn't seem to be a valid YouTube address.")
            url = None


def get_thumbnail_url():
    """ Get the url of the thumbnail image in max resolution.

    :return: string url to the thumbnail image
    """

    try:
        html = get_page()
    except ValueError:
        raise

    soup = BeautifulSoup(html, 'html.parser')

    thumbnail = soup.find("meta", property="og:image")

    if thumbnail:
        return thumbnail["content"]
    else:
        raise PropertyNotFoundError(get_page.__name__, "Property og:image not found.")


def save_thumbnail():
    """ Print the thumbnail url and save the image from thumbnail url to a local file.

    :return: None
    """

    try:
        thumb_url = get_thumbnail_url()
    except PropertyNotFoundError as error:
        print(error.message, "Check if the url loads in your browser and try again.")
        return None

    video_id = thumb_url.split('/')[-2]
    thumb_data = requests.get(thumb_url).content

    folder = './thumbnails/'
    makedirs(folder, exist_ok=True)  # make directory for saving thumbnails if it doesn't exist already
    filename = 'yt-thumb-{}.{}'.format(video_id,
                                       thumb_url[-3:])  # TODO file name should be the name of the video (?not unique?)

    file_path = path.join(folder, filename)

    with open(file_path, 'wb') as image:
        image.write(thumb_data)

    print("Thumbnail url: {}".format(thumb_url))
    print("Thumbnail saved to {}{}".format(folder, filename))


if __name__ == '__main__':
    while True:
        save_thumbnail()
