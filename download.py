#! /usr/bin/env python3

import requests
import re

pattern = re.compile(r'value=\'([\d-]*)\' name="Id" class="btn btn-link docImage')

# you get the web page guts


for (pdf_id) in re.findall(pattern, web_page_guts):
    url = f"https://businesssearch.sos.ca.gov/Document/RetrievePDF?Id={pdf_id}"
    r = requests.get(url, verify=False)  
    with open(f"pdfs/{pdf_id}.pdf", 'wb') as f:
        f.write(r.content)
