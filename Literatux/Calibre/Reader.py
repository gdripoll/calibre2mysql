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

	def read_all(self):
		log = '<Reader:read_all> %s'
		logging.debug(log, '')

		for cal, data in self._config.items():
			db = Calibre(data)
		pass
