## 臺灣各縣市交通事故記錄之視覺化呈現

111304019 統計三 林承佑
107703027 資科四 崔賢燮


Setup
-----

### Requirements
* Python3 (latest)

### Setup

* Install manopt_dr, ulca, and ulca_ui

  * If using Python3.12 (otherwise, skip this step), need to edit and directly install pymanopt as follows because pymanopt installer only supports Python3.11 or older.

    - Download and move to the latest `pymanopt` repo: https://github.com/pymanopt/pymanopt.
    
    - Edit "pyproject.toml"

      - Line 2: `requires = ["pip>=22.3.1", "setuptools>=65.6.3"]`
      
      - Line 40: `"scipy>=1.0",`

    - Create "_version.py" in "src/pymanopt/" and write down a following line:

      - `__version__ = "2.2.0"`

    - Install `pymanopt`

      - `pip3 install .`

  * Download/Clone this repository

  * Move to the downloaded repository, then:

    `pip3 install .`

  

### Usage
- In the sample.py file, set the folder_path variable to the path of the folder containing the CSV files to be analyzed. Once set, all CSV files in the specified path will be automatically loaded and merged.

- In the selected_features variable, choose the features from the CSV files to be used in the analysis. These selected features will be utilized for the analysis.

- In the target_values variable, specify the target feature from the selected_features list.

* See sample.py
  - To run sample.py from the command line, use -i option:

    `python3 -i sample.py` or `python -i sample.py`

  - If you cannot see the visualized results, try a hard refresh (e.g., when Mac + Chrome, Ctrl + Shift + R) at the jupyter notebook you are using.


### 備註

- 若只開啟第一目錄下的 index.html （即使用助教課所教的node.js 的server.js，則會無法使用降維的功能）。
- 只有以`python3 -i sample.py`的方式開啟本網站時，主畫面中的降維視覺化才會具有連結，並可點擊前往使用降維功能。
