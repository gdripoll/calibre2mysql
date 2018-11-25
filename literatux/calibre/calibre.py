#
# Calibre
#
import sqlite3
import logging
import logging.config


class Calibre:
	def __init__(self, config):
		self._config = config
		print(self._config)
		self._conn = None
		self._conn = self._open()

	def _open(self):
		if self._conn is not None:
			self._close()
		print(self._config)
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
