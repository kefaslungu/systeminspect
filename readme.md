## System Inspect
by [Kefas Lungu](https://github.com/kefaslungu).

System Inspect is a program that provides detailed information on several hardware and software on your system. It also gives you the ability to configure user and password settings, allows you to manage several built-in windows tools from the app.
This information is presented in a notebook interface with a tab for each category.

### System information:
information about a computer system. The program utilizes several functions to retrieve information on the following:
* Basic information such as operating system information, and hardware manufacturer.
* Detailed information on systems battery.
* computer's BIOS
* CPU
* Graphics cards information.
* Hard disks and USB devices connected to the machine.
* Motherboard
* Network cards.
* RAM.
* Sound cards.
* Startup items.

When a button for the respective item is clicked, a dialog box is displayed with the information, and an option to copy it to the clipboard.

### User and password management.
This Tab allows you to manage several settings that has to do with user accounts.
* Create a new user: When this button is clicked, it opens a dialog box for you to type in the new user’s name, and an optional password. There are 3 fields in total:
  * User name: the name of the new user.
  * Password: an optional password for the new user account to be created.
  * Confirm password: Retype the password to make sure all is going well.
When all fields are inputted, click on the okay button and you should get a success or an error message telling you the state of your operation. Same goes for most settings in this category, I will only mention when it is not needed.
* Change or create password rules: The settings allow you to change the following:
  * Input the maximum password age in days.
  * Input the minimum length of a password.
  * Input the minimum password age in days.
  * Input the number of unique passwords.
Note: all values must be integers. To learn more on password rules: checkout [This guide by ultimate windows security](https://www.ultimatewindowssecurity.com/wiki/page.aspx?spid=PasswordPolicy).
* Create password complexity: There are only 2 options here: you can only turn it on or off. [learn more](https://www.ultimatewindowssecurity.com/wiki/page.aspx?spid=PasswordComplexityRequirements).
* Enable your built-in administrator account: If you don't know what it is, [Read about it here](https://www.techtarget.com/searchwindowsserver/definition/built-in-administrator-account).
* Disabling the administrator account.
* Change the password for the current user: This setting allows you to create a new password, or change the password of the current login user.

### Built-in windows diagnostic tools:
This category is straight Forword. It provides a quicker way to call some built-in tools that comes with windows. Most of these tools are there for you to fix an issue with windows, or security related tools. They are:
  * Basic system scan: Uses the built-in SFC utility to check for issues.
  * Disk cleanup: remove junks from your computer.
  * Disk defragmenter: defrag your hard drive, not necessary for an SSD drive.
  * DirectX: a set of components in Windows that allows software, primarily and especially games, to work directly with your video and audio hardware.
  * Windows driver verifier: monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls.
  * Others include: Event viewer, Resource monitor, windows system config, Task manager, Windows Memory Diagnostics, uninstall a program, Windows malicious removal tool, Windows firewall, Windows advanced firewall, and an option to reset this PC

The goal of System Inspect is to provide users with an easy way to view important information about their computer system, To change settings that are a bit difficult to change, and put repair tools in one place for easy access. The program is designed to be user-friendly and accessible to users of all technical backgrounds.

more functionality will be added in future releases.
## Requirements.
note: this section is intended for those who want to compile from source, without using the [executable](https://github.com/kefaslungu/systeminspect/releases/download/V0.1.1/systeminspectV0.1.1.exe).

To run System Inspect, you must have Python 3 and the following libraries installed:

* wxPython: the graphical user interface used in the whole of the program.
* wmi: this is used to access the windows management instrumentation.
* psutil: [process and system utilities]. This module is used in several places.
* pyperclip: Used for copying the system information.

You can install all these modules by using pip.
Subprocess, threading and the os modules are built-in with python, no need to install them from pip.
Or better still, open a CMD window in the directory of the main program, then run
python -m pip install -r requirements.txt

## Usage:
To run System Inspect after all these modules are installed, simply execute the `systeminspect.py` file.

The program will open a notebook interface with tabs for each category of settings. Click on each tab to view the corresponding options.

Please note that the information presented by System Inspect may not be entirely accurate or up-to-date. Use this program at your own risk.
## Contributing:
If you would like to contribute to System Inspect, please feel free to submit a pull request or [contact the developer](jameskefaslungu@gmail.com).

Thank you for using System Inspect!

Copyright © 2023 kefaslungu.
