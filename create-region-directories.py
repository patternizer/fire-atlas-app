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

#template_directory = "ar6-land/ESAF/"

# LOAD: IPCC AR6 land look-up table

df = pd.read_csv( 'ar6.land.csv' )

# LOOP: over rows

for index, row in df.iterrows():

    id_value = row['id']
    name_value = row['name']
    abbrev_value = row['abbrev']

    template_directory = "ar6-land/" + abbrev_value + "/"

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

            # EXTRACT: timescale from file name

        timescale = filename.split('-')[-1].split('.')[0]

        # UPDATE: region HTML files with modifications
        
        modified_content = file_content.replace('<h1>E.Southern-Africa (ESAF)</h1>', f'<h1>{name_value} ({abbrev_value})</h1>')
        modified_content = modified_content.replace('-region-27', f'-region-{str(id_value).zfill(2)}')
        
        modified_content = modified_content.replace('"../../figures/BA_Total-ipcc-ar6-land-region-timeseries-sum-yearly-region-27.png"', f'"../../figures/BA_Total-ipcc-ar6-land-region-timeseries-sum-{timescale}-region-{str(id_value).zfill(2)}.png"')
        modified_content = modified_content.replace('"../../formatted_data/BA_Total-timeseries-yearly-region-27.csv"', f'"../../formatted_data/BA_Total-timeseries-{timescale}-region-{str(id_value).zfill(2)}.csv"')
        modified_content = modified_content.replace('"../../formatted_data/BA_Total-stats-yearly-region-27.csv"', f'"../../formatted_data/BA_Total-stats-{timescale}-region-{str(id_value).zfill(2)}.csv"')                

        modified_content = modified_content.replace('"../../figures/BA_Total_Forest_NonForest-ipcc-ar6-land-region-timeseries-sum-yearly-region-27.png"', f'"../../figures/BA_Total_Forest_NonForest-ipcc-ar6-land-region-timeseries-sum-{timescale}-region-{str(id_value).zfill(2)}.png"')
        modified_content = modified_content.replace('"../../formatted_data/BA_Total_Forest_NonForest-timeseries-yearly-region-27.csv"', f'"../../formatted_data/BA_Total_Forest_NonForest-timeseries-{timescale}-region-{str(id_value).zfill(2)}.csv"')
        modified_content = modified_content.replace('"../../formatted_data/BA_Total_Forest_NonForest-stats-yearly-region-27.csv"', f'"../../formatted_data/BA_Total_Forest_NonForest-stats-{timescale}-region-{str(id_value).zfill(2)}.csv"')                

        modified_content = modified_content.replace('"../../figures/Cem_Total-ipcc-ar6-land-region-timeseries-sum-yearly-region-27.png"', f'"../../figures/Cem_Total-ipcc-ar6-land-region-timeseries-sum-{timescale}-region-{str(id_value).zfill(2)}.png"')
        modified_content = modified_content.replace('"../../formatted_data/Cem_Total-timeseries-yearly-region-27.csv"', f'"../../formatted_data/Cem_Total-timeseries-{timescale}-region-{str(id_value).zfill(2)}.csv"')
        modified_content = modified_content.replace('"../../formatted_data/Cem_Total-stats-yearly-region-27.csv"', f'"../../formatted_data/Cem_Total-stats-{timescale}-region-{str(id_value).zfill(2)}.csv"')                

        modified_content = modified_content.replace('"../../figures/Cem_Total_Forest_NonForest-ipcc-ar6-land-region-timeseries-sum-yearly-region-27.png"', f'"../../figures/Cem_Total_Forest_NonForest-ipcc-ar6-land-region-timeseries-sum-{timescale}-region-{str(id_value).zfill(2)}.png"')
        modified_content = modified_content.replace('"../../formatted_data/Cem_Total_Forest_NonForest-timeseries-yearly-region-27.csv"', f'"../../formatted_data/Cem_Total_Forest_NonForest-timeseries-{timescale}-region-{str(id_value).zfill(2)}.csv"')
        modified_content = modified_content.replace('"../../formatted_data/Cem_Total_Forest_NonForest-stats-yearly-region-27.csv"', f'"../../formatted_data/Cem_Total_Forest_NonForest-stats-{timescale}-region-{str(id_value).zfill(2)}.csv"')                

        modified_content = modified_content.replace('csv">csv</a>', 'csv" target="_self">csv</a>')
        modified_content = modified_content.replace('target="_blank"', 'target="_self"')
                                                                    
        # WRITE: modified content back to the file
                                        
        with open(destination_file_path, 'w') as file:
            file.write(modified_content)
                                                                            
#------------------------------------------------------------------------------
print('** END')    

