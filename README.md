# Winter 2025 Assignment 2

User Management Script for Linux (assignment2.py)
=============================================
Description:
-------------
This script is designed manage users on a Linux system. It supports a variety of actions, such as creating and deleting users, listing human users, checking the current logged-in user, and more. The script requires root (**sudo**) privileges for certain actions.

Usage:
------
    python3 assignment2.py <action> [--username USERNAME] [--group GROUP]
s
    - <action>: The task to perform. Current available actions are:
        * create     - Create a new user. (Requires ‘sudo’)
        * delete     - Delete an existing user. (Requires ‘sudo’)
        * list       - List all human users on the Linux system.
        * locked     - Find locked or disabled accounts. (Requires ‘sudo’)
        * size       - Check the size of a user's home directory.
        * current    - Display the current logged-in user.
        * loggedin   - Show all users currently logged into the system.
        * group      - Change the group of a specific user. (Requires ‘sudo’)
        * password   - Change the password for a specific user. (Requires ‘sudo’)

    - [--username USERNAME]: Specify the username for actions that require a user. This option is mandatory for `create`, `delete`, `size`, `group`, and `password` actions.
    - [--group GROUP]: Specify the group name when using the `group` action.


Examples:
---------
1. Create a user:
    `python3 assignment2.py create --username gandalf`

2. Delete a user:
    `python3 assignment2.py delete --username gandalf`

3. List all human users:
    `python3 assignment2.py list`

4. Find locked or disabled accounts:
    `python3 assignment2.py locked`

5. Check the size of a user's home directory:
    `python3 assignment2.py size --username gandalf`

6. Check the current logged-in user:
    `python3 assignment2.py current`

7. Show all logged-in users:
    `python3 assignment2.py loggedin`

8. Change the group of a user:
   ` python3 assignment2.py group --username gandalf --group wizards`

9. Change the password for a user:
    `python3 assignment2.py password --username gandalf`

Permissions:
------------
- Most actions require **root** privileges. Run the script as root to ensure proper permissions:
    sudo python3 assignment2.py <action> [options]

Help:
-----
For help or to display usage instructions, run:
    `python3 assignment2.py -h`

Notes:
------
- Script requires Python 3 installed on your Linux system.

	Run `python -V` to check the version
    
    Get the latest version of python here
    <https://www.python.org/downloads/>

- Some actions, such as `create` and `delete`, will make changes to the system's user accounts. **Please use with caution**.
---
