import os


# cdir = os.getcwd()
# WORKING_DIR = os.path.abspath(os.path.join(cdir, WORKING_DIR))

WORKING_DIR = os.getcwd()

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