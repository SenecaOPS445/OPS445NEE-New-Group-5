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
    try:
        # Using sudo to run the useradd command
        subprocess.check_call(["sudo", "useradd", username]) #  Subprocess.check_call() runs the command and waits for it to finish
        print(f'User {username} added successfully.') # Print the output
    except subprocess.CalledProcessError as e: # If the command fails, it will raise CalledProcessError if command returns a nonzero exit status
        print(f'Failed to add user {username}: {e}') # Save the error in e and print e
    except:
        print('Unknown error occured') # If it's not processerror then print here

#author: YuFan
def delete_user(username):    
    try:
        # Delete the user using userdel
        subprocess.check_call(["sudo", "userdel", username]) # Subprocess.check_call() runs the command and waits for it to finish
        print(f'User {username} deleted successfully.') # Print the output
    except subprocess.CalledProcessError as e: # If the command fails, it will raise CalledProcessError
        print(f'Failed to delete user {username}: {e}') # Save the error in e and print e
    except:
        print('Unknown error occured') # If it's not processerror then print here

#author: YuFan
def list_human_users():
    try:
        # Use subprocess.check_output() to execute the getent command, which grab the information from system password database.
        # The output is decoded from bytes into human readable string with .decode('utf-8').
        output = subprocess.check_output(["getent", "passwd"]).decode('utf-8')
        
        all_users=[]
        for line in output.splitlines(): # Grab the output from subprocess, root:x:0:0:root:/root:/bin/bash
            all_users.append(line.split(':')[0]) # Splitting each line by ":", and choose the index 0, which is username, save it in all_users list.
        for user in all_users:
            print(f'user_name: {user}') # Use for loop to print username one by one
    except subprocess.CalledProcessError: # If the system does not have getent, it will raise CalledProcessError
        print('Failed to list users') # Print the error
    except FileNotFoundError: # Catch multiple exceptions
        print('File not found')
    except:
        print('Unknown error occured')


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
