import schedule
import os.path
import yaml
import time
import subprocess

if os.path.exists('config.yaml'):
    configfile = 'config.yaml'
    print("found custom config")
else:
    configfile = 'defaultconfig.yaml'
    print("no custom config found, load default")

with open(configfile, 'r') as f:
    try:
        config = yaml.safe_load(f)
        print("config loaded")
    except yaml.YAMLError as exc:
        print(exc)

sync_down = "rclone sync {rname}:{rpath}/finance.ledger data/".format(rname=config['remotename'], rpath=config['remotepath'])
sync_up = "rclone sync data/finance.ledger {rname}:{rpath}".format(rname=config['remotename'], rpath=config['remotepath'])

