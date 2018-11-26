#
# Mysql
#

# import mysql.connector
import pymysql
import logging
import logging.config


class MySql:
    def __init__(self, name, config):
        log = '<MySql:__init__> %s'
        self._config = config
        self._name = name
        self._conn = None
        self._cursor = None
        logging.debug(log, 'init')
        self._open()

    def _open(self):
        log = '<MySql:_open> %s'
        if self._conn is not None:
            self._close()
        try:
            self._conn = pymysql.connect(self._config['host'], self._config['user'], self._config['password'], self._config['database'])
            self._cursor = self._conn.cursor()
            logging.debug(log, 'connected to %s [%s] ' % (self._name, self._config['database']))
        except Exception as err:
            logging.error(log, "cannot connect to %s > %s" % ('%s/metadata.db' % self._config['path'], err))

    def _close(self):
        log = '<MySql:_close> %s'
        if self._conn is not None:
            try:
                self._conn.close()
            except Exception as err:
                logging.error(log, "cannot disconnect from %s > %s" % (self._config['path'], err))

    def drop_table(self):
        log = '<MySql:drop_table> %s'
        try:
            cmd = """
                DROP TABLE IF EXISTS {table};
            """.format(
                table=self._name
            )
            logging.debug(log, cmd)
            self._cursor.execute(cmd)
        except Exception as err:
            logging.error(log, err)

    def create(self):
        log = '<MySql:create> %s'
        try:
            self.drop_table()
            cmd = """
                CREATE TABLE `calibre2mysql`.`{table}` ( 
                    `cal_id` BIGINT NOT NULL AUTO_INCREMENT , 
                    `cal_timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , 
                    `cal_book_name` VARCHAR(500) NOT NULL , 
                    `cal_author_name` VARCHAR(500) NOT NULL , 
                    PRIMARY KEY (`cal_id`)
                ) ENGINE = MyISAM;
                """.format(
                table=self._name
            )
            logging.debug(log, cmd)
            self._cursor.execute(cmd)
        except Exception as err:
            logging.error(log, err)

    def save_rows(self, rows):
        log = '<MySql:save_rows> %s'

        logging.debug(log, "creating %s rows." % len(rows))
        cmd = """
            INSERT INTO `{table}` 
                (`cal_book_name`, `cal_author_name`) 
            VALUES 
                (%s, %s)
        """.format(
            table=self._name
        )
        data = []
        for r in rows:
            data.append((r['sort'], r['author_sort']))

        logging.debug(log, "saving %s rows." % len(rows))
        self._cursor.executemany(cmd, data)
        logging.debug(log, "%s rows saved." % len(rows))
