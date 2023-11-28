![image](https://github.com/patternizer/fire-atlas-app/blob/main/PLOTS/ar6.land_ocean.png)

# fire-atlas-app
UEA impact study app (dev)

## Contents

* `global-wildfire-atlas-yearly.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (yearly: JAN-DEC)
* `global-wildfire-atlas-yearly_jj.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (yearly: JUL-JUN)
* `global-wildfire-atlas-seasonal_djf.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: DJF)
* `global-wildfire-atlas-seasonal_mam.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: MAM)
* `global-wildfire-atlas-seasonal_jja.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: JJA)
* `global-wildfire-atlas-seasonal_son.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (seasonal: SON)
* `global-wildfire-atlas-monthly.html` - HTML script to generate an interactive IPCC AR6 land region world map with radio button timescales that link to a page that displays associated variables (monthly)
* `create-region-directories.py` - Python script to generate a directory per IPCC AR6 land region containing timescale HTML files
* `ar6.land.csv` - Look up table for IPCC AR6 land region abbreviations and descriptive names

The first step is to clone the latest fire-atlas-app repo and step into the check out directory: 

    $ git clone https://github.com/patternizer/fire-atlas-app.git
    $ cd fire-atlas-app

### Usage

The code was tested locally in a Python 3.8.16 virtual environment.

    $ firefox global-wildfire-atlas-yearly.html (or any of the other HTML map files as they're interlinked)
        
## License

The code is distributed under terms and conditions of the [Open Government License](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

## Contact information

* [Michael Taylor](michael.a.taylor@uea.ac.uk)

