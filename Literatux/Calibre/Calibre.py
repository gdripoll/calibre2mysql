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
		self._conn = self._open()
		logging.debug(log, 'connected to %s' % self._config['name'])

	def _open(self):
		log = '<Calibre:__init__> %s'
		if self._conn is not None:
			self._close()
		if 'path' in self._config.keys():
			try:
				return sqlite3.connect('%s/metadata.db' % self._config['path'])
			except Exception as err:
				logging.error("cannot connect to %s > %s" % ('%s/metadata.db' % self._config['path'], err))

	def _close(self):
		if self._conn is not None:
			try:
				self._conn.close()
			except Exception as err:
				logging.error("cannot disconnect from %s > %s" % (self._config.path, err))
