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
    pass

def delete_user(username):
    pass

def list_human_users():
    pass

def find_locked_or_disabled_accounts():
    pass

# author: Darian
def check_user_directory_size(username):
    try:
        # Get user info from system
        user_info = pwd.getpwnam(username)  # Fetch user details by username
        user_home = user_info.pw_dir  # Get the home directory path of the user
        
        # Use 'du -sh' to get the size of the user's home directory
        result = subprocess.run(['du', '-sh', user_home], capture_output=True, text=True, check=True)
        print(f"Directory size for {username}: {result.stdout.strip()}")  # Print the result
    except KeyError:
        print(f"User '{username}' not found.")  # If user does not exist
    except subprocess.CalledProcessError as e:
        print(f"Error checking directory size: {e}")  # Error from subprocess
    except:
        print('Unknown error occurred')  # Catch-all for other errors

# author: Darian
def check_current_user():
    try:
        # Try to get the current user with getpass (more reliable than os.getlogin)
        current_user = getpass.getuser()
        print(f"Current user: {current_user}")  # Print the current user
    except:
        print("Failed to get current user")  # Catch any errors

def check_logged_in_users():
    pass

def change_user_group(username, group):
    pass

# author: Darian
def change_user_password(username):
    try:
        # Use passwd command to change the user's password
        subprocess.run(['sudo', 'passwd', username], check=True)  # Requires sudo
    except subprocess.CalledProcessError:
        print(f"Failed to change password for user '{username}'.")  # Print error if command fails
    except:
        print("Unknown error occurred while changing password")  # Catch-all

def validate_args(args):
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
