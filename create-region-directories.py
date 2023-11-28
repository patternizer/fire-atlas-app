#! /usr/bin python

#------------------------------------------------------------------------------
# PROGRAM: create-region-directories.py
#------------------------------------------------------------------------------
# Version 0.1
# 28 November, 2023
# Michael Taylor
# michael DOT a DOT taylor AT uea DOT ac DOT uk 
#------------------------------------------------------------------------------

import pandas as pd
import os
import shutil
import fileinput
from bs4 import BeautifulSoup
import re

# DEFINE: source directory containing files to copy to all region directories

template_directory = "ar6-land/ESAF/"

# LOAD: IPCC AR6 land look-up table

df = pd.read_csv( 'ar6.land.csv' )

# LOOP: over rows

for index, row in df.iterrows():

    id_value = row['id']
    name_value = row['name']
    abbrev_value = row['abbrev']

    directory_path = os.path.join('.', abbrev_value)    
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

	# COPY: all files from the source directory to the created directory
	    
    for filename in os.listdir(template_directory):
		
        source_file_path = os.path.join(template_directory, filename)
        destination_file_path = os.path.join(directory_path, filename)

		# COPY: files into new directory

        shutil.copy(source_file_path, destination_file_path)

        # READ: each HTML file
        
        with open(destination_file_path, 'r') as file:
            file_content = file.read()

        # REPLACE: title line and figure names in each HTML file relative to the region directory
        
        modified_content = file_content.replace('<h1>E.Southern-Africa (ESAF)</h1>', f'<h1>{name_value} ({abbrev_value})</h1>')
        modified_content = modified_content.replace('-region-27', f'-region-{str(id_value).zfill(2)}')
                
        '''             
        # CONVERT: ordered list to HTML table
        
        soup = BeautifulSoup(modified_content, 'html.parser')
        ol_tags = soup.find_all('ol')
        for ol_tag in ol_tags:

            # EXTRACT: list items from ordered list

            list_items = ol_tag.find_all('li')

            # CREATE: HTML table

            table_tag = soup.new_tag('table')
            for li in list_items:

                tr_tag = soup.new_tag('tr')
                td_tag = soup.new_tag('td')
                td_tag.string = li.get_text()
                tr_tag.append(td_tag)
                table_tag.append(tr_tag)

            # REPLACE: ordered list with HTML table

            ol_tag.replace_with(table_tag)
        '''            
        # WRITE: modified content back to the file
                                        
        with open(destination_file_path, 'w') as file:
            #file.write(str(soup))
            file.write(modified_content)
                                                                            
#------------------------------------------------------------------------------
print('** END')    

