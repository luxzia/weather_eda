# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
df = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/weatherdata.csv")
df.head()

# <codecell>

df.dtypes

# <codecell>

df.describe()

# <codecell>

df.mode()

# <codecell>

df.median()

# <codecell>

df.count()

# <markdowncell>

# Temperature in San Francisco is generally felt to be the same year round.  The close values of the mean, median, and mode of the max, average, and min of temperature would seem to agree with that.
# 
# However, what is the daily variation with temperature?  (create daily range column and look at it). Also, is there a relation between humidity, temperature, visibility (and what is the visibility when 'Fog' is recorded as an Event?)

# <codecell>

df["Daily Range"] = df["Max TemperatureF"] - df["Min TemperatureF"]
df.head()

# <codecell>

%pylab inline
import seaborn as sns

# <codecell>

dfDR = df[["Daily Range", "PST", "Mean TemperatureF"]]
pylab.rcParams['figure.figsize'] = (15.0,8.0)
plt.xlabel("Daily Temperature Range, San Francisco Jan 2013 - Feb 2014", fontsize=18)
#plt.hist(dfDR["Daily Range"], 10, alpha=.7)
plt.hist(dfDR["Mean TemperatureF"], 10, alpha=.7);

# <codecell>

sns.jointplot(dfDR["Daily Range"], dfDR["Mean TemperatureF"], kind="hex", ylim=[40,75],xlim=[2.5,35]);

# <markdowncell>

# The mean temperature distribution is somewhat bimodal - there is one peak at about 60 degrees and another at about 55 degrees. 

# <codecell>

#dfFog = df[["PST", "Daily Range"," Mean VisibilityMiles"]]
#sns.jointplot(dfFog["Daily Range"], dfFog[" Mean VisibilityMiles"], kind="hex");
#plt.hist(dfFog[" Mean VisibilityMiles"], 10, alpha=.7);
#plt.hist(dfFog["Daily Range"], 10, alpha=.7);
#dfFog.dtypes

# <codecell>

df.head()

# <codecell>

dates = pd.date_range('20130106', periods=397)
dates

# <codecell>

df.columns

# <codecell>

dfwc = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/weather_walnut_creek.csv")
dfwc.head()

# <codecell>

dfwc = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/weather_walnut_creek.csv")
dfwc.head()

# <codecell>

#templst = df["Mean TemperatureF"]
#templst
#templst = templst.T
#templst
#dfixDate = pd.DataFrame(df["Mean TemperatureF"], index=dates)
#dfixDate = dfixDate.T
#dfbyDate = pd.DataFrame({'Date': dates,
                         #'Mean Temperature'
    
#dfwcbyDate = dfwc.set_index("PST")
#dfbyDate = dfDR.set_index("PST")

#dfnew = pd.merge(dfwcbyDate,dfbyDate)

#dfwcbyDate
        
#dfnew.plot(figsize=(15,15));

# <codecell>

#dfwc.columns()

# <codecell>

#dfwctemp = dfwcbyDate["PST", ]
# take out dfwctemp with PST and mean temperature, merge with the date range data frame and chart the mean temp on that,
# after dropping the date range coludfwcbyDate = dfwc.set_index("PST"
dfDR.set_index("PST")

# <codecell>

df

# <codecell>

#dfwctemp = dfwcbyDate["PST", ]
# take out dfwctemp with PST and mean temperature, merge with the date range data frame and chart the mean temp on that,
# after dropping the date range coludfwcbyDate = dfwc.set_index("PST"
dfwctemp = dfwc[["PST", "Mean TemperatureF"]]
dfwctemp.head()

# <codecell>

dfwc.set_index("PST")

# <codecell>

dfwcsfcompare = pd.merge(dfwctemp,dfDR, on="PST")
dfwcsfcompare.head()

# <codecell>

dfwcsfcomparedrop1 = dfwcsfcompare.drop(dfwcsfcompare.index[0:146])

# <codecell>

dfwcsfcomparedrop2 = dfwcsfcomparedrop1.drop(dfwcsfcomparedrop1.index[92:252])
dfwcsfcomparedrop2.head()

# <codecell>

dftheory = dfwcsfcomparedrop2.drop(["Mean TemperatureF_y"],1)
dftheory.head()

# <codecell>

dftheory.corr()

# <codecell>

sns.kdeplot(dftheory["Daily Range"], shade=True); 

# <codecell>

pylab.rcParams['figure.figsize'] = (15.0,8.0)
plt.xlabel("Daily Temperature in Walnut Creek", fontsize=20 )
plt.ylabel("Daily Range of Temperature in San Francisco", fontsize=18)
plt.scatter(dftheory["Mean TemperatureF_x"], dftheory["Daily Range"])
#write regression line?

# <codecell>

from pandas.tools.plotting import scatter_matrix
scatter_matrix(dftheory[['Mean TemperatureF_x','Daily Range']], alpha=0.3, figsize=(10, 10), diagonal='kde');

# <codecell>

sns.tsplot(dftheory['Daily Range']);

# <markdowncell>

# import os
# path = r'/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/'  # remove the trailing '\'
# # data = {}
# for dir_entry in os.listdir(path):
#     #DIRENTRYNAME = 'FILENAME'
#     dir_entry_path = os.path.join(path, dir_entry)
#     if os.path.isfile(dir_entry_path):
#         #with open(dir_entry_path, 'r') as my_file: #do I need to read the file in and write it out?
#          my_file = open(dir_entry_path, 'r')
#          print dir_entry
#          s = dir_entry.split('.')[0]
#          outfile = open(s, 'w')
#          s = pd.read_csv(dir_entry)
#             #str(dir_entry_path) = pd.read_csv(my_file)
#             #data[dir_entry] = pd.read_csv()
# # os.path.join()            

# <codecell>

dfsf2004 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf200405.csv)
dfsf2005 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf200506.csv)
dfsf2006 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf200607.csv)
dfsf2007 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf200708.csv)
dfsf2008 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf200809.csv)
dfsf2009 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf200910.csv)
dfsf2010 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf201011.csv)
dfsf2012 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf201112.csv)
dfsf2013 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf201213.csv)
dfsf2014 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf201314.csv)

# <codecell>

dfsf2004.head()

# <codecell>

dfwc2004 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc200405.csv)
dfwc2005 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc200506.csv)
dfwc2006 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc200607.csv)
dfwc2007 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc200708.csv)
dfwc2008 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc200809.csv)
dfwc2009 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc200910.csv)
dfwc2010 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc201011.csv)
dfwc2012 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc201112.csv)
dfwc2013 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc201213.csv)
dfwc2014 = pd.read_csv("/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/wc201314.csv)

# <markdowncell>

# 1. we looked at data sets - some were not presents on sites where they were supposed to be via Open Prism
# 2. we went for weather data, looked at local sf data and played with it, talked about doing then take the main data frame, take the PST, mean temperature, mean visibility, mean humidity columns and see what those look over the course of a year (histogram, is there a way to look at weather with maps over the course of a year?) 
# 3. then

# <codecell>

# add daily range to dfSF files
# make a new df file with PST and daily range, set index to PST
# take the dfWC files and and make new df files, with PST set to index and mean temperature
# merge the yearly files of walnut creek's mean temperature and sf's daily range
# drop indicies so that we are looking only at June to August data
# run correlations by year
# make fun data plots with sns, etc.

# <codecell>

#dfcompare = dfwcsfcompare.drop(["Daily Range"],1)
#dfcompare.head()

# <codecell>

# write script to read in files
# write script to build ten? data structures? or one?
# how do you show ten years of weather data and a correlation each year?

# <codecell>

#dfcompare.head()
#dfcompare.plot(figsize=(15,15))

# <codecell>

#dfcompare.corr()

# <codecell>

#dfcompare.count()
#dfcomparedrop1 = dfcompare.drop(dfcompare.index[0:146])
#dfcomparedrop1.head()
#dfsummercompare = dfcompare.ix([150:])

# <codecell>

#dfcompare.head()
#dfcompare2 = dfcomparedrop1.drop(dfcomparedrop1.index[92:252])
#dfcompare2.head()
#dfcompare2.tail()

# <codecell>

#dfcompare.corr()
#dfcompare2.plot()

# <codecell>

#then take the main data frame, take the PST, mean temperature, mean visibility, mean humidity columns and see what those look 
# over the course of a year (histogram, is there a way to look at weather with maps over the course of a year?)

