import configparser
import mutagen
import logging
import sys
import sqlite3
import os
import enum


def main():
    # Init Logger
    log = logging.getLogger('Aero-Stat')
    log.info('Started')

    # Init Config
    config = configparser.ConfigParser()
    try:
        config.read('aero-stat.conf')
    except IOError as e:
        log.error('Error while opening config file')
        log.error(e)
    except:
        log.error('Unknown error: ', sys.exc_info()[0])
        raise

    # Init DB
    try:
        db_conn = sqlite3.connect(config['db']['db_path'])
        cursor = db_conn.cursor()
    except sqlite3.Error as e:
        log.error('Error while opening database: ', e)
    except:
        log.error('Unknown error: ', sys.exc_info()[0])\
        raise


    episodes = {}


    # Lookup over folder
    try:
        subdirs = os.walk(config['files']['src_path'])
        for subdir in subdirs:
            index, episode = Episode.parse_folder(subdir)
    except IOError:
        log.error('Error while folder lookup')
        log.error(e)
    except:
        log.error('Unknown error: ', sys.exc_info()[0])
        raise


class Episode:
    def __init__(self, folder, index, name, fragments, date):
        self.folder = folder
        self.index = index
        self.name = name
        self.fragments = fragments
        self.date = date

    @staticmethod
    def parse_folder(folder: str) -> (int, Episode):
        return 1, Episode()


class FragmentKind(enum.Enum):
    jingle = ()
    comment = ()
    song = ()


class Fragment:
    def __init__(self, file, index, artist, name, kind: FragmentKind, duration):
        self.file = file
        self.index = index
        self.artist = artist
        self.name = name
        self.kind = kind
        self.duration = duration


