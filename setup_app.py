
# python version check
print('python version check\n')
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
print('copy config files & make data dir\n')
dest = Path('./data')
datafolder = Path('./ShareTitle/data')
if not dest.exists():
  dest.mkdir()
  copy(datafolder/'docker_config.json', dest/'config.json')
  copy(datafolder/'parseScript.json', dest)
if not datafolder.exists():
  raise Exception('Cannot find ShareTitle repository, please clone recursively')

# ask for change app port
print('update application port')
with open('.env', 'r', encoding='utf-8') as file:
  envraw = file.read()
env = dict( map(lambda i:i.split('='), envraw.splitlines()) )
print('Do you want to change your application port?')
print(f'Current application will be deployed on port:{env["APP_PORT"]}')
port = input('Enter new port number if you want to change it, otherwise enter \"n\": ')
port = port.lower()
if port != 'n':
  try:
    port = int(port)
    env['APP_PORT'] = port
    envupdate = '\n'.join( [f'{k}={v}' for (k,v) in env.items()] )
    with open('.env', 'w', encoding='utf-8') as file:
      file.write(envupdate)
    print(f'set application port to: {port}')
  except Exception as err:
    print(f'Invalid port number or failed to update port number, exception: {err}')

# run docker-compose
print('\nrun docker-compose\n')
system(' docker-compose up -d --build ')

