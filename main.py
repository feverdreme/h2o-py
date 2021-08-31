import argparse
import os
import json
from src.checks.check_existing_folder import check_existing_folder
from src.template import template_json
from src.argument_parser import get_args
from src.checks.check_empty_dir import check_empty_dir
from src.docs import needed_folders
from src.checks.check_initted_dir import check_initted_dir

command, args = get_args()

if command == "init":
    # checks
    check_existing_folder(args.directory)
    assert(check_empty_dir(args.directory))

    # make the stuff
    for file in needed_folders:
        os.makedirs(os.path.join(args.directory, file))

    with open(os.path.join(args.directory, "h2o.json"), 'w') as f:
        json.dump(template_json, f, indent=4)

if command == "install":
    check_initted_dir()

    # add the thing
    with open("h2o.json", "r") as f:
        h2o_json = json.load(f)
    
    if args.package == "*":
        # install all of the packages
        dependencies = h2o_json["dependencies"]

    else: # install the package as usual
        if args.package in h2o_json["dependencies"]:
            pass

        else:
            h2o_json["dependencies"][args.package] = "latest"
        
        with open("h2o.json", 'w') as f:
            json.dump(h2o_json, f, indent=4)