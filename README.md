# Jupyter notebooks
My notes.

## Installation
1. Install Python 3 & pip
2. Install dependencies
2. Install Jupyter `pip install jupyter`
3. Add to path, see fixes.
4. Start with `jupyter notebook`.

## Fixes
### jupyter not recognized as command
Add to path:

`C:\Users\DarkEclipz\AppData\Roaming\Python\Python35\Scripts`

### error with plottings (iopub\_data\_rate_limit)
Start notebook with additional parameter:

`jupyter notebook --NotebookApp.iopub_data_rate_limit=2147483647`

## Style

**Custom style:**

`%%html <style>#notebook-container{font-size: 13pt;} div.text_cell{max-width: 104ex;}</style>`

# Dependencies
## Python (3)

**Packages:**
Install dependencies with `pip install --user <dependency>`:

`plotly`, `requests`, `numpy`

# Licence
Public Domain, unless otherwise stated.
