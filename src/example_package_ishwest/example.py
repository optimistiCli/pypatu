#!/usr/bin/env python3

import sys
import json
import requests

def add_one(number):
    return number + 1

def main():
    if len(sys.argv) < 2:
        print('No URL', file=sys.stderr)
        return 1
    r = requests.get(sys.argv[1], stream=True)
    chunk_size = 128
    headers = None
    counter = 0
    with open('aaa.svg', 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if not headers:
                headers = r.headers
                print(json.dumps(dict(headers), indent=4))
            print('.', end='')
            counter += 1
            fd.write(chunk)
    print(f'\n{counter * chunk_size}')
    return 0

#if __name__ == '__main__':
#    sys.exit(main())
