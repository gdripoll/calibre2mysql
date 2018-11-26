#
# Saver
#
import logging
import logging.config

from .MySql import MySql


class Saver:
    def __init__(self, config):
        log = '<Saver:__init__> %s'
        self._config = config
        logging.debug(log, 'init')

    # def save_all(self, data):
    #     log = '<Saver:read_all> %s'
    #     logging.debug(log, '')
    #
    #     for cal, data in self._config.items():
    #         self._savers[cal] = MySql(data)

    def get_list(self):
        return self._config.keys()

    def saver(self, key):
        return MySql(key, self._config[key])
