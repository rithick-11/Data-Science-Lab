#Univariate, Bivariate and Multiple Regression analysis on diabetes dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

# Read Diabetes data set
df = pd.read_csv('./diabetes.csv')
print(df.head())
print(df.shape)
print(df.dtypes)

# Convert Outcome to boolean
df['Outcome'] = df['Outcome'].astype('bool')
print(df.dtypes['Outcome'])
print(df.info())

# Pregnancy Propagation Visualizations
fig, axes = plt.subplots(nrows=3, ncols=2, dpi=120, figsize=(8, 6))
plot00 = sns.countplot(x='Pregnancies', data=df, ax=axes[0][0], color='green')
axes[0][0].set_title('Count', fontdict={'fontsize': 8})
axes[0][0].set_xlabel('Month of Preg.', fontdict={'fontsize': 7})
axes[0][0].set_ylabel('Count', fontdict={'fontsize': 7})
plt.tight_layout()

plot01 = sns.countplot(x='Pregnancies', data=df, hue='Outcome', ax=axes[0][1])
axes[0][1].set_title('Diab. VS Non-Diab.', fontdict={'fontsize': 8})
axes[0][1].set_xlabel('Month of Preg.', fontdict={'fontsize': 7})
axes[0][1].set_ylabel('Count', fontdict={'fontsize': 7})
plot01.axes.legend(loc=1)
plt.setp(axes[0][1].get_legend().get_texts(), fontsize='6')
plt.setp(axes[0][1].get_legend().get_title(), fontsize='6')
plt.tight_layout()

plot10 = sns.distplot(df['Pregnancies'], ax=axes[1][0])
axes[1][0].set_title('Pregnancies Distribution', fontdict={'fontsize': 8})
axes[1][0].set_xlabel('Pregnancy Class', fontdict={'fontsize': 7})
axes[1][0].set_ylabel('Freq/Dist', fontdict={'fontsize': 7})
plt.tight_layout()

plot11 = df[df['Outcome']==False]['Pregnancies'].plot.hist(ax=axes[1][1], label='Non-Diab.')
plot11_2 = df[df['Outcome']==True]['Pregnancies'].plot.hist(ax=axes[1][1], label='Diab.')
axes[1][1].set_title('Diab. VS Non-Diab.', fontdict={'fontsize': 8})
axes[1][1].set_xlabel('Pregnancy Class', fontdict={'fontsize': 7})
axes[1][1].set_ylabel('Freq/Dist', fontdict={'fontsize': 7})
plot11.axes.legend(loc=1)
plt.setp(axes[1][1].get_legend().get_texts(), fontsize='6')
plt.setp(axes[1][1].get_legend().get_title(), fontsize='6')
plt.tight_layout()

plot20 = sns.boxplot(df['Pregnancies'], ax=axes[2][0], orient='v')
axes[2][0].set_title('Pregnancies', fontdict={'fontsize': 8})
axes[2][0].set_xlabel('Pregnancy', fontdict={'fontsize': 7})
axes[2][0].set_ylabel('Five Point Summary', fontdict={'fontsize': 7})
plt.tight_layout()

plot21 = sns.boxplot(x='Outcome', y='Pregnancies', data=df, ax=axes[2][1])
axes[2][1].set_title('Diab. VS Non-Diab.', fontdict={'fontsize': 8})
axes[2][1].set_xlabel('Pregnancy', fontdict={'fontsize': 7})
axes[2][1].set_ylabel('Five Point Summary', fontdict={'fontsize': 7})
plt.xticks(ticks=[0,1], labels=['Non-Diab.', 'Diab.'], fontsize=7)
plt.tight_layout()
plt.show()

# Glucose Variable Analysis
print(df.Glucose.describe())

fig, axes = plt.subplots(nrows=2, ncols=2, dpi=120, figsize=(8, 6))
plot00 = sns.distplot(df['Glucose'], ax=axes[0][0], color='green')
axes[0][0].set_title('Distribution of Glucose', fontdict={'fontsize': 8})
axes[0][0].set_xlabel('Glucose Class', fontdict={'fontsize': 7})
axes[0][0].set_ylabel('Count/Dist.', fontdict={'fontsize': 7})
plt.tight_layout()

plot01 = sns.distplot(df[df['Outcome']==False]['Glucose'], ax=axes[0][1], color='green', label='Non Diab.')
sns.distplot(df[df.Outcome==True]['Glucose'], ax=axes[0][1], color='red', label='Diab')
axes[0][1].set_title('Distribution of Glucose', fontdict={'fontsize': 8})
axes[0][1].set_xlabel('Glucose Class', fontdict={'fontsize': 7})
axes[0][1].set_ylabel('Count/Dist.', fontdict={'fontsize': 7})
plot01.axes.legend(loc=1)
plt.setp(axes[0][1].get_legend().get_texts(), fontsize='6')
plt.setp(axes[0][1].get_legend().get_title(), fontsize='6')
plt.tight_layout()

plot10 = sns.boxplot(df['Glucose'], ax=axes[1][0], orient='v')
axes[1][0].set_title('Numerical Summary', fontdict={'fontsize': 8})
axes[1][0].set_xlabel('Glucose', fontdict={'fontsize': 7})
axes[1][0].set_ylabel(r'Five Point Summary(Glucose)', fontdict={'fontsize': 7})
plt.tight_layout()

plot11 = sns.boxplot(x='Outcome', y='Glucose', data=df, ax=axes[1][1])
axes[1][1].set_title(r'Numerical Summary (Outcome)', fontdict={'fontsize': 8})
axes[1][1].set_ylabel(r'Five Point Summary(Glucose)', fontdict={'fontsize': 7})
plt.xticks(ticks=[0,1], labels=['Non-Diab.', 'Diab.'], fontsize=7)
axes[1][1].set_xlabel('Category', fontdict={'fontsize': 7})
plt.tight_layout()
plt.show()

# Blood Pressure variable
print(df.BloodPressure.describe())

fig, axes = plt.subplots(nrows=2, ncols=2, dpi=120, figsize=(8, 6))
plot00 = sns.distplot(df['BloodPressure'], ax=axes[0][0], color='green')
axes[0][0].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
axes[0][0].set_title('Distribution of BP', fontdict={'fontsize': 8})
axes[0][0].set_xlabel('BP Class', fontdict={'fontsize': 7})
axes[0][0].set_ylabel('Count/Dist.', fontdict={'fontsize': 7})
plt.tight_layout()

plot01 = sns.distplot(df[df['Outcome']==False]['BloodPressure'], ax=axes[0][1], color='green', label='Non Diab.')
sns.distplot(df[df.Outcome==True]['BloodPressure'], ax=axes[0][1], color='red', label='Diab')
axes[0][1].set_title('Distribution of BP', fontdict={'fontsize': 8})
axes[0][1].set_xlabel('BP Class', fontdict={'fontsize': 7})
axes[0][1].set_ylabel('Count/Dist.', fontdict={'fontsize': 7})
axes[0][1].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
plot01.axes.legend(loc=1)
plt.setp(axes[0][1].get_legend().get_texts(), fontsize='6')
plt.setp(axes[0][1].get_legend().get_title(), fontsize='6')
plt.tight_layout()

plot10 = sns.boxplot(df['BloodPressure'], ax=axes[1][0], orient='v')
axes[1][0].set_title('Numerical Summary', fontdict={'fontsize': 8})
axes[1][0].set_xlabel('BP', fontdict={'fontsize': 7})
axes[1][0].set_ylabel(r'Five Point Summary(BP)', fontdict={'fontsize': 7})
plt.tight_layout()

plot11 = sns.boxplot(x='Outcome', y='BloodPressure', data=df, ax=axes[1][1])
axes[1][1].set_title(r'Numerical Summary (Outcome)', fontdict={'fontsize': 8})
axes[1][1].set_ylabel(r'Five Point Summary(BP)', fontdict={'fontsize': 7})
plt.xticks(ticks=[0,1], labels=['Non-Diab.', 'Diab.'], fontsize=7)
axes[1][1].set_xlabel('Category', fontdict={'fontsize': 7})
plt.tight_layout()
plt.show()

# Bivariate analysis and scatter plots
sns.scatterplot(df.DiabetesPedigreeFunction, df.Glucose)
plt.ylim(0, 20000)
plt.show()

sns.scatterplot(df.BMI, df.Age)
plt.ylim(0, 20000)
plt.show()

sns.scatterplot(df.BloodPressure, df.Glucose)
plt.ylim(0, 20000)
plt.show()

plt.figure(figsize=(12, 8))
sns.kdeplot(data=df, x=df.Glucose, hue=df.Outcome, fill=True)
plt.show()

# Multiple Regression analysis - data preprocessing
print(df.isnull().values.any())
print((df.Pregnancies == 0).sum(), (df.Glucose == 0).sum(), 
      (df.BloodPressure == 0).sum(), (df.SkinThickness == 0).sum(),
      (df.Insulin == 0).sum(), (df.BMI == 0).sum(), 
      (df.DiabetesPedigreeFunction == 0).sum(), (df.Age == 0).sum())

# Drop rows with zeros
drop_Glu = df.index[df.Glucose == 0].tolist()
drop_BP = df.index[df.BloodPressure == 0].tolist()
drop_Skin = df.index[df.SkinThickness == 0].tolist()
drop_Ins = df.index[df.Insulin == 0].tolist()
drop_BMI = df.index[df.BMI == 0].tolist()
c = drop_Glu + drop_BP + drop_Skin + drop_Ins + drop_BMI
dia = df.drop(df.index[c])
print(dia.info())

# Correlation analysis
cor = dia.corr(method='pearson')
print(cor)
sns.heatmap(cor)
plt.show()