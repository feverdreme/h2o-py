import argparse
import os
import json
from src.checks.check_existing_folder import check_existing_folder
from src.template import template_json
from src.argument_parser import get_args
from src.checks.check_empty_dir import check_empty_dir
from src.docs import needed_folders

command, args = get_args()

if command == "init":
    # checks
    check_existing_folder(args.directory)
    assert(check_empty_dir(args.directory))

    # make the stuff
    for file in needed_folders:
        os.makedirs(os.path.join(args.directory, file))

    with open(os.path.join(args.directory, "h2o.json"), 'w+') as f:
        json.dump(template_json, f, indent=4)
