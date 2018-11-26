#
# Reader
#
import logging
import logging.config

from .Calibre import Calibre


class Reader:
    def __init__(self, config):
        log = '<Reader:__init__> %s'
        self._config = config
        logging.debug(log, 'init')

    # def read_all(self):
    #     log = '<Reader:read_all> %s'
    #     logging.debug(log, '')
    #
    #     calibres = {}
    #     for cal, data in self._config.items():
    #         db = Calibre(data)
    #         calibres[cal] = db.read_data_books()
    #     return calibres

    def get_list(self):
        return self._config.keys()

    def reader(self, key):
        return Calibre(self._config[key])
