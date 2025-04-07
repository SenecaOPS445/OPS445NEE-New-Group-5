#!/usr/bin/env python3

'''
User Management script for Linux systems
OPS 445 NEE - Group 05 (Winter 2025)

'''

import os
import pwd
import argparse
import subprocess

def create_user(username):
    #Yufan
    pass

def delete_user(username):
    #Yufan
    pass

def list_human_users():
    #Yufan
    pass

def find_locked_or_disabled_accounts():
    # This function will list all the locked human users in the system
    # If there are no locked accounts found it will print an appropriate message to the screen 

    #command to execute in the shell so it would only list users with uid range 1000 to 65534
    command = "sudo awk -F: 'NR==FNR && $3>=1000 && $3<65534 {u[$1]; next} $1 in u && $2 ~ /^[!*]/ {print $1}' /etc/passwd /etc/shadow"

    #Capturing the string output of this command to the variable result
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    # Check if there was any output and print the results 
    if result.returncode == 0:
        if result.stdout:
            print("Locked human users:")
            print(result.stdout)
        else:
            print("No locked human users found.")
    else:
        print(f"Error: {result.stderr}")


def check_user_directory_size(username):
    #Darian
    pass

def check_current_user():
    #Darian
    pass

def check_logged_in_users():
    #Sangeeth
    pass

def change_user_group(username, group):
    #Sangeeth
    pass

def change_user_password(username):
    #Darian
    pass

def validate_args(args):
    #Sangeeth
    pass

def show_help():
    pass

parser = argparse.ArgumentParser(description="User Management Script for Linux Systems")
parser.add_argument(
    'action',
    choices=['create', 'delete', 'list', 'locked', 'size', 'current', 'loggedin', 'group', 'password'],
    help="Action to perform: create, delete, list, locked, size, current, loggedin, group, password"
)
parser.add_argument(
    '--username',
    type=str,
    help="Specify the username (required for actions 'create', 'delete', 'size', 'group', 'password')"
)
parser.add_argument(
    '--group',
    type=str,
    help="Specify the group (required for the 'group' action)"
)

args = parser.parse_args()

if len(vars(args)) == 0:
    show_help()
else:
    try:
        validate_args(args)
        if args.action == 'create':
            create_user(args.username)
        elif args.action == 'delete':
            delete_user(args.username)
        elif args.action == 'list':
            list_human_users()
        elif args.action == 'locked':
            find_locked_or_disabled_accounts()
        elif args.action == 'size':
            check_user_directory_size(args.username)
        elif args.action == 'current':
            check_current_user()
        elif args.action == 'loggedin':
            check_logged_in_users()
        elif args.action == 'group':
            change_user_group(args.username, args.group)
        elif args.action == 'password':
            change_user_password(args.username)
    except ValueError as e:
        print(f"Argument error: {e}")
        show_help()
