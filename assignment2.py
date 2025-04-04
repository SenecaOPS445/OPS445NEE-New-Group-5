#!/usr/bin/env python3

'''
User Management script for Linux systems
OPS 445 NEE - Group 05 (Winter 2025)

'''

import os
import pwd
import argparse
import subprocess

#author: YuFan
def create_user(username):
    print("user created here")

    try:
        # Using sudo to run the useradd command
        subprocess.run(["sudo", "useradd", username], check=True)
        print(f'User {username} added successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Failed to add user {username}: {e}')

#author: YuFan
def delete_user(username):    
    print("user deleted here")
    try:
        # Delete the user using userdel
        subprocess.check_call(["sudo", "userdel", username])
        print(f'User {username} deleted successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Failed to delete user {username}: {e}')

#author: YuFan
def list_human_users():
    print("user listed here")
    try:
        # List users by reading the passwd database (getent is more portable)
        output = subprocess.check_output(["getent", "passwd"]).decode('utf-8')
        # get the output from subprocess, root:x:0:0:root:/root:/bin/tcsh
        # we can separate the results by ":", and always choose index 0, save it as a list of data type
        all_users=[]
        for line in output.splitlines():
            all_users.append(line.split(':')[0])
        for user in all_users:
            print(f'user_name: {user}')
    except subprocess.CalledProcessError as e:
        print(f'Failed to list users: {e}')



def find_locked_or_disabled_accounts():
    pass

def check_user_directory_size(username):
    pass

def check_current_user():
    pass

def check_logged_in_users():
    pass

def change_user_group(username, group):
    pass

def change_user_password(username):
    pass

def validate_args(args):
    pass

def show_help():
    pass

#Test argparse module
# parser = argparse.ArgumentParser()
# parser.add_argument("echo123", help="echo the string you use here", type=int, choices=[1, 2, 3])
# args = parser.parse_args()
# print(args.echo123)


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
