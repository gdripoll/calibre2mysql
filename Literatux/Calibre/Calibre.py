#
# Calibre
#
import sqlite3
import logging
import logging.config


class Calibre:
    def __init__(self, config):
        log = '<Calibre:__init__> %s'
        self._config = config
        self._conn = None
        logging.debug(log, 'init')
        self._open()

    def _open(self):
        log = '<Calibre:__init__> %s'
        if self._conn is not None:
            self._close()
        if 'path' in self._config.keys():
            try:
                self._conn = sqlite3.connect('%s/metadata.db' % self._config['path'])
                self._db = self._conn.cursor()
                logging.debug(log, 'connected to %s' % self._config['name'])
            except Exception as err:
                logging.error("cannot connect to %s > %s" % ('%s/metadata.db' % self._config['path'], err))

    def _close(self):
        if self._conn is not None:
            try:
                self._conn.close()
            except Exception as err:
                logging.error("cannot disconnect from %s > %s" % (self._config.path, err))

    def read_data_books(self):
        log = '<Calibre:read_data_books> %s'
        try:
            self._db.execute("""select * from books order by sort""")
            sal = []
            for row in self._db:
                sal.append(self.dict_factory(self._db, row))
            logging.debug(log, 'read %s rows.' % len(sal))
            return sal
        except Exception as err:
            logging.error("cannot read from %s > %s" % (self._config, err))

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
