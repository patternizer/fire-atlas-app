import csv

# Which version to make?
#iver = 0  # 0=yearly
#timescalestr = 'yearly'
#timescalestr = 'yearly_jj'
#timescalestr = 'monthly'
#timescalestr = 'seasonal_djf'
#timescalestr = 'seasonal_mam'
#timescalestr = 'seasonal_jja'
timescalestr = 'seasonal_son'

#fnhtml = 'table-for-fire-countries-yearly.html'
fnhtml = 'table-for-fire-countries-' + timescalestr + '.html'

# Read list of countries with continent indicators
fnlist = 'continents_table.csv'
print('Reading continents and countries from:')
print(fnlist)

with open(fnlist, 'r') as csvfile:
    reader = csv.reader(csvfile)
    cnthead = next(reader)  # Assuming the first row contains headers
    rawdat = {header: [] for header in cnthead}
    
    for row in reader:
        for i, header in enumerate(cnthead):
            rawdat[header].append(row[i])

# Extract continent names (skip first 3 field names)
cntnm = cnthead[3:]
ncnt = len(cntnm)

# Create html for a list of countries, grouped by continent
# This is not a complete html file, it is meant to be pasted into an existing
# html file that contains the rest of the webpage and the styles etc.

print('Writing to: ' + fnhtml)
with open(fnhtml, 'w') as f:
    # Process each continent in turn
    cntcount = [0] * ncnt  # count how many countries are associated with each continent

    for icnt in range(ncnt):

        # Find which countries are assigned to this continent
        flaglist = [int(x) if x.strip() != '' else 0 for x in rawdat[cntnm[icnt]]]
        gotlist = [i for i, flag in enumerate(flaglist) if flag > 0]
        print()
        print(cntnm[icnt], len(gotlist))

        # Extract fields for this subset of countries
        if gotlist:
            cysubsetno = [rawdat[cnthead[0]][i] for i in gotlist]  # country number
            cysubsetab = [rawdat[cnthead[1]][i] for i in gotlist]  # country abbreviation
            cysubsetnm = [rawdat[cnthead[2]][i] for i in gotlist]  # country name

            # Sort into alphabetical order by abbreviation
            isort = sorted(range(len(cysubsetab)), key=lambda k: cysubsetab[k])
            print([cysubsetab[i] for i in isort])
                    
            # Generate HTML entry for this continent, followed by 1-line per country
            f.write(f'<h4>{cntnm[icnt]}</h4>\n\n')
            f.write('<ol>\n')
            for i in range(len(gotlist)):
                j = isort[i]
                #urlname = f'{cysubsetab[j]}/yearly.html'
                #urlname = f'countries/{cysubsetab[j]}/yearly.html'
                urlname = f'countries/{cysubsetab[j]}/{timescalestr}.html'
                f.write(f'  <li><a href="{urlname}">{cysubsetab[j]} &nbsp;&nbsp;&nbsp; {cysubsetnm[j]}</a></li>\n')
            f.write('</ol>\n\n')

# end of script



                    
                    
                    