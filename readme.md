# Project_Module_1
CryptoBOT Analytics Buy &amp; Sell Triggers

## INITIAL SETUP
> Run: `pip install -r requirements.txt` from the `blockchainbot/` folder

### At the start of every Notebook
* Add the following code in the first cell of any notebook you start
```
import sys

sys.path.append('../SourceCode/')
```

### local_settings.py (file structure)
    data_storage_path='/Users/charlotte/Data'
    source_code_path='/Users/charlotte/UofT/blockchainbot/SourceCode'
    
    
    * create the file (if not exist in the repo) `SourceCode/` (Where README.md file exists)
    * set the following variables:
        * data_storage_paht='/absolute/path/to/the/shared/google/drive/folder/for/data'
        * source_code_path= 'absolute/path/to/the/`SourceCode`/folder'
        * polygon_api_key='your_polygon_api_key'

### .env (file structure)
    api_key='your_polygon_api_key'
    polygon_api_key='your_polygon_api_key'

**NOTE: To get absoute path of a file or a folder, use the terminal. Drag the file or the folder onto the terminal. The absolute path will be revealed**

### Pattern Recognition:
* installation >> `conda install -c conda-forge ta-lib`
___
## References:

* Polygon API Documentation for Stocks Crypto and Forex API
    > polygon.io/docs/crypto/getting-started
* Dependencies