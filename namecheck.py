#!/usr/bin/env python3

import argparse
import subprocess
from shutil import which


"" if which('whois') else exit("Missing dependency: whois")


def domain_available(domain):
    output = subprocess.run(['whois', domain], stdout=subprocess.PIPE)
    output = output.stdout.decode('utf-8')
    if output.find("Domain not found") != -1 or output.find("No match for domain") != -1:
        return True
    else:
        return False


def check_domain(domain):
    if domain_available(domain):
        print(f"\033[92m [o] \033[00m {domain}")
    else:
        print(f"\033[91m [x] \033[00m {domain}")


def check_domain_file(filename):
    f = open(filename, 'r')
    domains = f.readlines()
    f.close()
    for domain in domains:
        check_domain(domain.strip())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='namecheck.py',
        description='Check domain availability.')
    parser.add_argument('-d',
                        '--domain',
                        type=str,
                        help="domain name to check")
    parser.add_argument('-f',
                        '--filename',
                        type=str,
                        help="list of domains one per line")
    args = parser.parse_args()

    if args.domain:
        check_domain(args.domain)
    elif args.filename:
        check_domain_file(args.filename)
    else:
        parser.print_help()
