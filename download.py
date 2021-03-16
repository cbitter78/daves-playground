#! /usr/bin/env python3

import requests


pdf_id = "01685273-4260742"



url = f"https://businesssearch.sos.ca.gov/Document/RetrievePDF?Id={pdf_id}"
r = requests.get(url, verify=False)  
with open(f"pdfs/{pdf_id}.pdf", 'wb') as f:
    f.write(r.content)
