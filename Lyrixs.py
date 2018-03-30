#! ./bin/python3.5
# -*- coding: utf-8 -*-

from PyLyrics import *
import dbus


def spotify_lyrics():
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                         "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(spotify_bus,
                                        "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player",
                                      "Metadata")

    # To just print the title
    title = (metadata['xesam:title'])
    artist = (metadata['xesam:artist'][0])

    # print artist

    def print_lyrics(song_title, song_singer):
        return PyLyrics.getLyrics(song_singer, song_title)

    try:
        lyrics = print_lyrics(title, artist)

    except ValueError:
        try:
            lyrics = print_lyrics(title.title(), artist.title())
        except ValueError:
            lyrics = 'Lyrics not found :('

    print()
    print(title)
    print(artist)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("")
    print(lyrics)
    print("")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("")
    input('Press Enter to quit')


def search_lyrics():
    title = input('Song Title: ')
    artist = input('Artist: ')

    def print_lyrics(song_title, song_singer):
        return PyLyrics.getLyrics(song_singer, song_title)

    try:
        lyrics = print_lyrics(title, artist)
    except ValueError:
        lyrics = 'Lyrics not found :('

    print()
    print(title)
    print(artist)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("")
    print(lyrics)
    print("")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("")
    input('Press Enter to quit')


def menu():
    print('          Lyrixs')
    print()
    print('1. Spotify Lyrics')
    print('2. Search any lyrics')
    print()

    def menu_action():
        option = input('Option: ')

        if option == '1':
            spotify_lyrics()
        elif option == '2':
            search_lyrics()
        else:
            print('Invalid Option')
            menu_action()

    menu_action()


menu()
