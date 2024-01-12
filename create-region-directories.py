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
import re

# DEFINE: source directory containing files to copy to all region directories

template_directory = "countries/ARG/"

# LOAD: IPCC AR6 land look-up table

#df = pd.read_csv( 'ar6.land.csv' )
df = pd.read_csv( 'natural_earth_v5_0_0.countries_110.csv' )

# LOOP: over rows

for index, row in df.iterrows():

    id_value = row['id']
    name_value = row['name']
    abbrev_value = row['abbrev']

    #template_directory = "countries/" + abbrev_value + "/"

    directory_path = os.path.join('.', abbrev_value)    
    print(index, directory_path)
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

            # EXTRACT: timescale from file name

        timescale = filename.split('-')[-1].split('.')[0]

        # UPDATE: region HTML files with modifications

        modified_content = file_content.replace('<h1>Argentina (ARG)</h1>', f'<h1>{name_value} ({abbrev_value})</h1>')       
        modified_content = modified_content.replace(f'{timescale}-ARG', f'{timescale}-{abbrev_value}')
        modified_content = modified_content.replace('-ipcc-ar6-land-region-', '-country-')
                                				
        #modified_content = file_content.replace(f'-region-{str(id_value).zfill(2)}', f'-{abbrev_value}')       
        #modified_content = modified_content.replace('csv">csv</a>', 'csv" target="_self">csv</a>')

        #modified_content = modified_content.replace('target="_blank"', 'target="_self"')
        #modified_content = modified_content.replace('"width=device-width, initial-scale=1"', '"width=device-width, initial-scale=1.0"')                
        #modified_content = modified_content.replace('"width=auto height=450px"', '"style="max-width:100%"; height=auto;"')                

        #modified_content = file_content.replace('../../figures', '../figures')
        #modified_content = modified_content.replace('../../formatted_data', '../formatted_data')
        #modified_content = modified_content.replace('Global Wildfire Atlas', 'Global Fire Dashboard')
        #modified_content = modified_content.replace('global-wildfire-atlas', 'global-fire-dashboard')

                                                                    
        # WRITE: modified content back to the file
                                        
        with open(destination_file_path, 'w') as file:
            file.write(modified_content)
                                                                                
#------------------------------------------------------------------------------
print('** END')    

