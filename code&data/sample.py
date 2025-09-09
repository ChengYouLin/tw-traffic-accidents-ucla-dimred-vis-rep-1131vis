from sklearn import datasets, preprocessing
from ulca.ulca import ULCA
from ulca_ui.plot import Plot
from sklearn.utils import Bunch  
import pandas as pd
import os
import glob

# Specify the location of the folder containing the CSV files.
folder_path = './ulca_ui'
csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

dataframes = []
for file in csv_files:
    try:
        df = pd.read_csv(file)  
        dataframes.append(df) 
        print(f"Loaded {file} successfully.")
    except Exception as e:
        print(f"Failed to load {file}: {e}")

df = pd.concat(dataframes, ignore_index=True)

# Choose the features to be used in the analysis
selected_features = ['事故類型及型態子類別名稱', '發生時間',  '速限.第1當事者', '當事者事故發生時年齡']


df_selected = df[selected_features]

# Select the feature to be used as the target
target_values = ['追撞', '側撞']



# "Filter specific values"
df_filtered = df_selected[df_selected['事故類型及型態子類別名稱'].isin(target_values)].copy()  

# number mapping
value_mapping = {
    '追撞': 1,
    '側撞': 2,
}


df_filtered.loc[:, '事故類型及型態子類別名稱'] = df_filtered['事故類型及型態子類別名稱'].map(value_mapping)


X = df_filtered.iloc[:, 1:].values  
y = df_filtered.iloc[:, 0].values     

feat_names = df_filtered.columns[1:].tolist()  



# 2. prepare ULCA and parameters
ulca = ULCA(n_components=2)

w_tg = {0: 0, 1: 0, 2: 0}
w_bg = {0: 1, 1: 0, 2: 0}
w_bw = {0: 1, 1: 1, 2: 1}

# 3. apply ULCA
ulca = ulca.fit(X, y=y, w_tg=w_tg, w_bg=w_bg, w_bw=w_bw)

# 4. show the result in the interactive visual interface
# To call the interface from the command line, inline_mode need to be False
Plot().plot_emb(dr=ulca,
                X=X,
                y=y,
                w_tg=w_tg,
                w_bg=w_bg,
                w_bw=w_bw,
                feat_names=feat_names,
                inline_mode=False)
