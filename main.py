import argparse
import os
import json

from src.template import template_json

# going to be its own file
parser = argparse.ArgumentParser(description="h20 - flyd package manager")
parser.add_argument('init', help="init a flyd project")

args=parser.parse_args()

if args.init:
    os.makedirs("modules")

    with open("h20.json", 'w+') as f:
        json.dump(template_json, f, indent=4)