#!/usr/bin/python3
#
# calibre2mysql
#

import argparse
import json
# import sys
import logging
import logging.config

from Literatux.Calibre.Reader import Reader
from Literatux.MySql.Saver import Saver


def main():
    log = '<Main:main> %s'
    logging.config.fileConfig('logging.conf')
    logging.debug(log % 'init')

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='1 - ...\n' '2 - ...\n' '3 - ...')
    parser.add_argument('config_file', type=argparse.FileType('r', encoding='UTF-8'), help='Archivo de configuración')
    # parser.add_argument('--dry-run', action="store_true", default=False, dest='dry_run', help='Usado para simulación')
    # parser.add_argument('--lote', nargs='+', type=int, required=True, dest='lote_id', help='Lote de procedure')
    # parser.add_argument('--from', type=int, required=False, default=0, dest='from_iteration', help='Número de registro de contingencia')
    parameters = parser.parse_args()

    logging.debug(log, 'config=%s' % parameters.config_file.name)
    config = json.load(parameters.config_file)
    logging.debug(log, config)

    # Reading
    print('#############################')
    reader = Reader(config['calibre'])
    saver = Saver(config['mysql'])
    origins = reader.get_list()
    destinations = saver.get_list()
    [saver.saver(dest).create() for dest in destinations] # cleans all tables and regenerate
    print(origins, destinations)
    for ori in origins:
        logging.debug(log, "origen = %s" % ori)
        r = reader.reader(ori).read_data_books()
        for dest in destinations:
            saver.saver(dest).save_rows(r)
    print('#############################')


if __name__ == '__main__':
    main()
