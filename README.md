# Universal_bruteforcer for all web pages with wordlist generator
 this python utility contains script to bruteforce any web site by providing credential field position and wordlist
# Bruteforcer

Bruteforcer is a tool that automates the process of guessing passwords or other credentials for various websites or applications. It has two modes: tab clicker and position clicker.

## Features

- Built-in wordlist generator: The tool can generate wordlists based on the given parameters, such as length, character set, pattern, etc.
- Works on HTTP and HTTPS site as it is just a HID automated bruteforcer
- Captcha detection and bypassing (planned)
- Multi-threading and parallel processing (planned)
- Customizable delay and timeout settings (planned)
- Proxy and VPN support (planned)
- User interface and documentation improvements (planned)
## Requirments
- Python 11+
- Pyautogui and pynput --pip-modules


Install all required pip modules by running this command in the tool's directory

     pip install -r requirments.txt
## Installation
- Clone this repository or download as zip
- install all the required python modules using pip
- Extract the zip
- Place all the wordlist in /Wordlists folder 
- Run Wordlist_gen.py to generate a custom Wordlist (or) Run Bruteforcer.py and follow the terminal wizard to attack
## Tab clicker mode

In this mode, the tool uses the tab key to navigate between the input fields and the submit button. It tries different combinations of usernames and passwords from a given list until it finds a match or reaches the end of the list.

## Position clicker mode

In this mode, the tool uses the mouse cursor to click on the input fields and the submit button. It tries different combinations of usernames and passwords from a given list until it finds a match or reaches the end of the list.

## Disclaimer

This tool is made only for educational purpose. Do not use it for any illegal or unethical activities. The developer is not responsible for any consequences of using this tool.

## Future development

The tool is still under development and may have some bugs or limitations. Some of the features that are planned for future updates are:

- Captcha detection and bypassing
- Multi-threading and parallel processing
- Customizable delay and timeout settings
- Proxy and VPN support
- User interface and documentation improvements
Feel free to Fork and develop or contribute to this repo
