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
    #Sangeeth
    # This function uses passwd and shadow files in the system and will list all the locked human users.
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
        print("Error:", result.stderr)


def check_user_directory_size(username):
    #Darian
    pass

def check_current_user():
    #Darian
    pass

def check_logged_in_users():
    #Sangeeth
    # returns the name of the user currently logged into the system

    try:
        #Running the who command
        output = subprocess.check_output(['who'], text=True)
        print("Currently logged-in users:")
        print(output.strip())
    except:
        print("Error checking logged-in users")


def change_user_group(username, group):
    #Sangeeth
    # This function will change the group of the user
    # Both username and group need to be specified 

    try:
        subprocess.run(['sudo', 'usermod', '-g', group, username], check=True)

        # If the execution of the command was successful this message will print 
        print("User", username, "is now in the group", group + ".")

    except:
        print("Error changing group for user", username)

def change_user_password(username):
    #Darian
    pass

def validate_args(args):
    #Sangeeth
    #If any of the necessary arguments (either username or group) are missing, the function will raise a ValueError with message.
    #if there are no errors it will return true
    if args.action == 'create' or args.action == 'delete' or args.action == 'size' or args.action == 'group' or args.action == 'password':
        if not args.username:
            raise ValueError("The 'username' argument is required for the selected action.")
    if args.action == 'group':
        if not args.group:
            raise ValueError("The 'group' argument is required for the 'group' action.")
    return True

#Usage functions

def usage_create():
    print("Usage: python3 assignment2.py create --username USERNAME")
    print("Action: Creates a new user on the system.")
    print("Required Argument:")
    print("  --username USERNAME  add the name of the user to create.")

def usage_delete():
    print("Usage: python3 assignment2.py delete --username USERNAME")
    print("Action: Delete an existing user from the system")
    print("Required Argument:")
    print(" --username USERNAME  add the name of the user to delete.")

def usage_list():
    print("Usage: python3 assignment2.py list")
    print("Description: List all human users on the system.")
    print("No optional arguments are needed.")

def usage_locked():
    print("Usage: python3 assignment2.py locked")
    print("Description: Find all locked accounts on the system.")
    print("No optional arguments are needed.")

def usage_size():
    print("Usage: python3 assignment2.py size --username USERNAME")
    print("Action: Check the size of the user's home directory.")
    print("Required Argument:")
    print("  --username USERNAME  add the name of the user.")

def usage_current():
    print("Usage: python3 assignment2.py current")
    print("Description: Display the currently logged-in user.")
    print("No optional arguments are needed.")

def usage_loggedin():
    print("Usage: python3 assignment2.py loggedin")
    print("Description: Show all users currently logged into the system.")
    print("No optional arguments are needed.")

def usage_group():
    print("Usage: python3 assignment2.py group --username USERNAME --group GROUP")
    print("Action: Change the group of a user.")
    print("Required Arguments:")
    print("  --username USERNAME  add the name of the user.")
    print("  --group GROUP     add the new group.")

def usage_password():
    print("Usage: python3 assignment2.py password --username USERNAME")
    print("Action: Change the password of a user.")
    print("Required Argument:")
    print("  --username USERNAME  add the name of the user.")

def show_help(action=None):
    if action == 'create':
        usage_create()
    elif action == 'delete':
        usage_delete()
    elif action == 'list':
        usage_list()
    elif action == 'locked':
        usage_locked()
    elif action == 'size':
        usage_size()
    elif action == 'current':
        usage_current()
    elif action == 'loggedin':
        usage_loggedin()
    elif action == 'group':
        usage_group()
    elif action == 'password':
        usage_password()
    else:
        parser.print_help()


# ArgumentParser object named parser with a description for the script
parser = argparse.ArgumentParser(description="User Management Script for Linux Systems")

# Argument 'action' with a list of allowed user management choices
parser.add_argument(
    'action',
    choices=['create', 'delete', 'list', 'locked', 'size', 'current', 'loggedin', 'group', 'password'],
    help="Action to perform: create, delete, list, locked, size, current, loggedin, group, password"
)

# 2 Optional arguments '--username' and '--group' that expects a string input
parser.add_argument(
    '--username',
    type=str,
    help="Specify the username (Must for actions 'create', 'delete', 'size', 'group', 'password')"
)

parser.add_argument(
    '--group',
    type=str,
    help="Specify the group (Must for the 'group' action)"
)

args = parser.parse_args()

#If there are no arguments the script will call the show_help function 
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
        show_help(args.action)
