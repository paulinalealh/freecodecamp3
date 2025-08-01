import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math

# 1
df = pd.read_csv("medical_examination.csv")
df = df.dropna()

# 2
df['overweight'] = (df["weight"]/(df["height"]/100)**2) > 25
df["overweight"] = df["overweight"].astype(int)


# 3
df["cholesterol"] = np.ceil((df["cholesterol"] - df["cholesterol"].min()) / (df["cholesterol"].max() - df["cholesterol"].min())).astype(int)
df["gluc"] = np.ceil((df["gluc"] - df["gluc"].min()) / (df["gluc"].max() - df["gluc"].min())).astype(int)

# 4
def draw_cat_plot():
    # 5
    #df_cat = df[["cardio", "cholesterol","gluc","smoke","alco","active","overweight"]]
    df_cat = pd.melt(df, id_vars = "cardio", value_vars = df[["cholesterol","gluc","smoke","alco","active","overweight"]])
    # 6
    #df_cat["variable"] = df_cat["variable"].astype("category")
    df_cat = df_cat.groupby(["variable","cardio"]).value_counts()
    
    print(df_cat)
    
    
    
    

    # 7



    # 8
    fig = sns.catplot()


    # 9
    #fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()