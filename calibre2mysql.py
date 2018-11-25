#
# calibre2mysql
#
import argparse
import json
import sys
import logging
import logging.config

from Literatux.Calibre.Reader import Reader


def main(command_line):
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

	calibres = Reader(config['calibre']).read_all()


if __name__ == '__main__':
	main(sys.argv)
