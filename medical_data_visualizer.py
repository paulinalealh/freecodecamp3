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
    df_cat = df_cat.rename("total").reset_index()

    # 7
    sns.catplot(data= df_cat, x ="variable", y="total", col="cardio", kind= "bar", hue= "value", legend="brief")
    # 8
    
    fig = sns.catplot(data= df_cat, x ="variable", y="total", col="cardio", kind= "bar", hue= "value", legend="brief")
    
    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df["ap_lo"] <= df["ap_hi"]) & 
                (df["height"] >= df["height"].quantile(0.025)) & 
                (df["height"] <= df["height"].quantile(0.975)) &
                (df["weight"] >= df["weight"].quantile(0.025)) &
                (df["weight"] <= df["weight"].quantile(0.975))]
    
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype= bool))


    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, annot = True, vmin=-0.1, vmax=0.3, fmt=".1f", linewidths=.5, linecolor = "white",mask=mask, center= 0, square = True, annot_kws={"size":6})

    # 16
    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()