![image](https://github.com/patternizer/fire-atlas-app/blob/main/PLOTS/ar6.land_ocean.png)

# fire-atlas-app
UEA impact study app (dev)

## Contents

* `global-fire-dashboard-yearly.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (yearly: JAN-DEC)
* `global-fire-dashboard-yearly_jj.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (yearly: JUL-JUN)
* `global-fire-dashboard-seasonal_djf.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: DJF)
* `global-fire-dashboard-seasonal_mam.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: MAM)
* `global-fire-dashboard-seasonal_jja.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: JJA)
* `global-fire-dashboard-seasonal_son.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: SON)
* `global-fire-dashboard-monthly.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (monthly)
* `create-region-directories.py` - Python script to generate a directory per IPCC AR6 land region containing timescale HTML files
* `update-map-htmls.py` - Python script to re-point map HTMLs to region directory HTML at the corresponding timescale
* `ar6.land.csv` - Look up table for IPCC AR6 land region abbreviations and descriptive names
* `natural_earth_v5_0_0.countries_110.csv` - Look up table for the country list aligned with regionmask output but with country abbreviations replaced with ISO 3166 alpha-3 codes.
* `continents_table.csv` - Look up table for assignment of countries to continents (Tim Osborn)
* `mkhtml_continents.pro` - IDL code to generate HTML continent-country links for country level landing pages (Tim Osborn)
* `mkhtml_continents.py` - python translation of IDL code to generate HTML continent-country links for country level landing pages

The first step is to clone the latest fire-atlas-app repo and step into the check out directory: 

    $ git clone https://github.com/patternizer/fire-atlas-app.git
    $ cd fire-atlas-app

### Usage

The code was tested locally in a Python 3.8.16 virtual environment.

    $ firefox global-fire-dashboard-yearly.html (or any of the other HTML map files as they're interlinked)
        
The country level interactive dashboard landing pages and integrated structure is coded. The image and stats files are being re-generated for each country.        
        
## License

The code is distributed under terms and conditions of the [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Contact information

* [Michael Taylor](michael.a.taylor@uea.ac.uk)

