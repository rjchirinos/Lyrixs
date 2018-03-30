# Lyrixs

A simple app that shows you the Lyrics from the song you're listening on Spotify. 
The songs come from the Lyrics Wikia database.
You can also search for specific lyrics by the title of the song and the artist.


### Prerequisites

```
Python 3.X
PyLyrics
dbus
```

### Installing

Clone the project directly from the GitHub Repo:

```
$ git clone https://github.com/rjchirinos/Lyrixs.git
```

Then install the requirements

```
$ pip3 install requirements.txt
```
and

```
$ sudo apt-get install python-dbus
```


### Running the tests

A menu will be displayed:

```
 Lyrixs

1. Spotify Lyrics
2. Search any lyrics

Option: 
```
If choose option 1 the app will automatically show the lyrics of the spotify currently playing song.
With option 2 you will asked to input the song's name and the artist (Capitals and lowercase recognized)


### Built With

* [PyLyrics](https://github.com/geekpradd/PyLyrics) - The Module used to get the Lyrics from LyricsWikia
