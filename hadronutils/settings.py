import os

import os
WORKING_DIR = '.'
cdir = os.path.dirname(__file__)
WORKING_DIR = os.path.abspath(os.path.join(cdir, WORKING_DIR))
DB_FILE = os.path.abspath(os.path.join(WORKING_DIR, 'directory.db'))
try:
    os.mkdir(WORKING_DIR)
except OSError as e:
    pass

def create_working_dir(dir):
	try:
		WORKING_DIR = dir
		DB_FILE = os.path.abspath(os.path.join(WORKING_DIR, 'directory.db'))
		try:
		    os.mkdir(WORKING_DIR)
		except OSError as e:
		    pass
	except Exception as e:
		raise e