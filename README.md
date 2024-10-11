# Domain-Checker
Script to check if a domain name is available

## Requirements
python3 and whois

## Installation
Make sure you have whois installed on your system. Move namecheck.py into a directory on your path like `~/bin` and make the script executable with `chmod +x namecheck.py`

### Linux (Debian)

`sudo apt install whois`

### MacOS

`xcode-select --install`

## Usage
```
usage: namecheck.py [-h] [-d DOMAIN] [-f FILENAME]

Check domain availability.

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        domain name to check
  -f FILENAME, --filename FILENAME
                        list of domains one per line
```
Example 1: `namecheck.py -d example.com` check a single domain name

Example 2: `namecheck.py -f domains.txt` check each domain in domains.txt (one domain per line).
