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
			logging.debug(log, 'reading %s.' % self._config['name'])
			cmd = """
			SELECT * from books_authors_link as ba
			LEFT JOIN books b on ba.book = b.id
			LEFT JOIN data d on ba.book = d.book 
			order by sort, format
			"""
			self._db.execute(cmd)
			sal = {}
			for row in self._db:
				r = self.dict_factory(self._db, row)
				if r['book'] in sal:
					sal[r['book']]['formats'].append(r['format'])
				else:
					sal[r['book']] = {
						"collection": self._config['name'],
						"book_id"   : r['book'],
						"auth_id"   : r['author'],
						"title"     : r['sort'],
						"author"    : r['author_sort'],
						"path"      : r['path'],
						"name"      : r['name'],
						"formats"   : [r['format']]
					}
			logging.debug(log, 'read %s rows.' % len(sal))
			# for s in sal:
			# 	print(s, sal[s])
			return sal
		except Exception as err:
			logging.error("cannot read from %s > %s" % (self._config, err))

	@staticmethod
	def dict_factory(cursor, row):
		d = {}
		for idx, col in enumerate(cursor.description):
			d[col[0]] = row[idx]
		return d
