import argparse
import sys

parser = argparse.ArgumentParser(description="h20 - flyd package manager")
parser.add_argument("command", choices=['init', 'install', 'uninstall'])

command_choice = parser.parse_args([sys.argv[1]]).command

init_parser = argparse.ArgumentParser("init")
install_parser = argparse.ArgumentParser("install")
uninstall_parser = argparse.ArgumentParser("uninstall")

init_parser.add_argument("directory", nargs="?", type=str, default=".")

install_parser.add_argument("package", nargs="?", type=str, default="*")

if command_choice == "init":
    args = init_parser.parse_args(sys.argv[2:])

elif command_choice == "install":
    args = install_parser.parse_args(sys.argv[2:])

elif command_choice == "uninstall":
    args = uninstall_parser.parse_args(sys.argv[2:])

def get_args():
    return [command_choice, args]
