#! /usr/bin python

#------------------------------------------------------------------------------
# PROGRAM: update-map-htmls.py
#------------------------------------------------------------------------------
# Version 0.1
# 28 November, 2023
# Michael Taylor
# michael DOT a DOT taylor AT uea DOT ac DOT uk 
#------------------------------------------------------------------------------

import csv
import re
import os
import glob

#------------------------------------------------------------------------------
# METHODS
#------------------------------------------------------------------------------

def replace_string(csv_file, html_file):

    # READ: look up table

    with open(csv_file, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        data = {row['id']: {'abbrev': row['abbrev'], 'name': row['name']} for row in csvreader}

    # EXTRACT: timescale variable from HTML filename

    timescale = html_file.split('-')[-1].split('.')[0]
        
    # READ: HTML file

    with open(html_file, 'r') as f:
        html_content = f.read()

    # REPLACE: string in HTML for each region to point to associated timescale HTML in region directory
    
    for id, info in data.items():
		
        #id = str(id).zfill(2)
        #replacement_string = f"ar6-land/{info['abbrev']}/{timescale}.html"
        #html_content = html_content.replace(f"figures/BA_Total-ipcc-ar6-land-region-timeseries-sum-{timescale}-region-{id}.png", replacement_string)
        html_content = html_content.replace(f'"Region {id}"', f"{info['abbrev']}")

    # WRITE: modified content back to the HTML file

    with open(html_file, 'w') as f:
        f.write(html_content)

#------------------------------------------------------------------------------
# RUN
#------------------------------------------------------------------------------

csv_file = 'ar6.land.csv'
html_filelist = glob.glob('*.html')

for html_file in html_filelist:

    print(html_file)
    replace_string(csv_file, html_file)

#------------------------------------------------------------------------------
print('** END')

