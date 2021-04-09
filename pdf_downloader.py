#! /usr/bin/env python3

import requests
import time
import os.path
import sys
from os import path

def read_csv(file, name_starts_with = ''):
    data = []
    with open(file) as f:
        for line in f.read().split('\n'):
            if (line == ''): 
                continue
            row = line.split(',')
            if (len(row)) != 2:
                print(f"WARNING: Could not process this line {line}")
                continue
            
            filename = f"./pdfs/{row[1].replace('/', '_')}"
            if (filename.endswith('.pdf') != True):
                filename = f"{filename}.pdf"

            link = row[0]
            if (link.startswith("\ufeff")):
                link = link.lstrip("\ufeff")  # Remove the stupid prefxi excel puts in.  FFS!

            if (name_starts_with == ''):
                data.append({'filename': filename, 'link': link })
            else:
                if (row[1].upper().startswith(name_starts_with.upper())):
                   data.append({'filename': filename, 'link': link }) 
    return data


filter = ''
if (sys.argv[1]):
    filter = sys.argv[1]

for r in read_csv('links.csv', filter):
    if path.exists(r['filename']):
        print(f"Skipping {r['filename']}")
        continue

    resp = requests.get(r['link'] , verify = False)

    print(f"Writing file {r['filename']}")
    with open(r['filename'], 'wb') as f:
        f.write(resp.content)    
    print(f"Wrote file {r['filename']}")
