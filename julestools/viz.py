# DATA MANIPULATION
import pandas as pd
import numpy as np

# DATA VISUALISATION
import matplotlib.pyplot as plt
import seaborn as sns

# STATISTICS
from statsmodels.graphics.gofplots import qqplot

def num_feat_viz(df):
    num_feat = df.select_dtypes(include = np.number)

    for numerical_feature in num_feat.columns:

        fig, ax = plt.subplots(1,3, figsize = (15,5))

        ax[0].set_title(f"Distribution of {numerical_feature}")
        sns.histplot(x = num_feat[numerical_feature], kde = True, ax = ax[0])

        ax[1].set_title(f"Boxplot of {numerical_feature}")
        sns.boxplot(x = num_feat[numerical_feature], ax = ax[1])

        ax[2].set_title(f"QQplot of {numerical_feature}")
        qqplot(num_feat[numerical_feature], line='s', ax = ax[2])
