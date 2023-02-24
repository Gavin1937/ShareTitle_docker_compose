
# python version check
try:
  from platform import python_version_tuple
  pyver = list(map(int, python_version_tuple()))
  if pyver[0] != 3 or pyver[1] <= 8:
    raise Exception('Please run this script with Python 3.8 or above')
except:
  raise
  exit(-1)


from pathlib import Path
from shutil import copy
from os import system

# copy config files & make data dir
dest = Path('./data')
datafolder = Path('./ShareTitle/data')
if not dest.exists():
  dest.mkdir()
  copy(datafolder/'docker_config.json', dest/'config.json')
  copy(datafolder/'parseScript.json', dest)
if not datafolder.exists():
  raise Exception('Cannot find ShareTitle repository, please clone recursively')

# run docker-compose
system(' docker-compose up -d --build ')

