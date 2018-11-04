# YouTube thumbnail download
Download the highest available resolution thumbnail image from a YouTube video specified by url.

## Using the compiled app
* Download archive __exe.win-amd64-3.6.rar__ from the __build__ folder and unpack it to your desired location.
* Run __downloadThumbnail.exe__ to open a console instance of the application.
* After prompted, provide a link to a YouTube video from which you want to extract the thumbnail in one of the following forms:
  * https://www.youtube.com/watch?v=k9kcgdP8aLY
  * www.youtube.com/watch?v=k9kcgdP8aLY
  * <a href='https://youtube.com/watch?v=k9kcgdP8aLY'>youtube.com/watch?v=k9kcgdP8aLY</a>
  * https://youtu.be/k9kcgdP8aLY
  * <a href='https://youtu.be/k9kcgdP8aLY'>youtu.be/k9kcgdP8aLY</a>
* If the adress is valid, the direct url (e.g. https://i.ytimg.com/vi/k9kcgdP8aLY/maxresdefault.jpg) as well as the relative local path (e.g. __./thumbnails/yt-thumb-aircAruvnKk.jpg__) to the image will be displayed 
* You will then be prompted for url to another video from which to extract a thumbnail until you quit the app.
* To quit the app, simply press _q_ or close the console window.

## Requirements for running the Python script
To run the Python script (__downloadThumbnail.py__) you need to have a __Python 3.6__ or newer environment with the following modules installed:
* <a href='http://docs.python-requests.org/en/master/user/install/#install'>Requests</a>
* <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup'>Beautiful Soup</a>

### Building the app into executable
The app was compiled (frozen) to a concole executable using the <a href='https://cx-freeze.readthedocs.io/en/latest/index.html'>cx_Freeze</a> library.
If you have properly set-up cx_Freeze, just run the following command in console (while in the root directory of the app):

```python
python setup.py build
```

To freeze the app with different parameters, edit __setup.py__ (for help refer to cx_Freeze  <a href='https://cx-freeze.readthedocs.io/en/latest/index.html'>documentation</a>).

## License
The content of this repository is licensed under the <a href='https://choosealicense.com/licenses/mit/'>MIT License</a>.
