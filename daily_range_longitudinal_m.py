# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd

# <codecell>

!ls -la /Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/

# <markdowncell>

# import os
# path = '/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/'
# #path = r'/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/'  # remove the trailing '\'
# #data = {}
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
# #os.path.join()         

# <codecell>

# load the sf files
dfsf2004 = pd.read_csv("sf200405.csv")
dfsf2005 = pd.read_csv("sf200506.csv")
dfsf2006 = pd.read_csv("sf200607.csv")
dfsf2007 = pd.read_csv("sf200708.csv")
dfsf2008 = pd.read_csv("sf200809.csv")
dfsf2009 = pd.read_csv("sf200910.csv")
dfsf2010 = pd.read_csv("sf201011.csv")
dfsf2011 = pd.read_csv("sf201112.csv")
dfsf2012 = pd.read_csv("sf201213.csv")
dfsf2013 = pd.read_csv("sf201314.csv")

# <codecell>

# load the wc files
dfwc2004 = pd.read_csv("wc200405.csv")
dfwc2005 = pd.read_csv("wc200506.csv")
dfwc2006 = pd.read_csv("wc200607.csv")
dfwc2007 = pd.read_csv("wc200708.csv")
dfwc2008 = pd.read_csv("wc200809.csv")
dfwc2009 = pd.read_csv("wc200910.csv")
dfwc2010 = pd.read_csv("wc201011.csv")
dfwc2011 = pd.read_csv("wc201112.csv")
dfwc2012 = pd.read_csv("wc201213.csv")
dfwc2013 = pd.read_csv("wc201314.csv")

# <codecell>

# check the data 
dfsf2004.head(1)

# <codecell>

# check the data
dfsf2004.tail(1)

# <codecell>

# check the data
dfsf2013.tail(1)

# <codecell>

sf_files = [dfsf2004,dfsf2005,dfsf2006,dfsf2007,dfsf2008,dfsf2009,dfsf2010,dfsf2011,dfsf2012,dfsf2013]
wc_files = [dfwc2004,dfwc2005,dfwc2006,dfwc2007,dfwc2008,dfwc2009,dfwc2010,dfwc2011,dfwc2012,dfwc2013]

# <codecell>

#sf_filesDR = [df["Daily Range"] = df["Max TemperatureF"] - df["Min TemperatureF"] for df in sf_files]
#?? why didn't list comprehension work?

for df in sf_files: 
    df["Daily Range"] = df["Max TemperatureF"] - df["Min TemperatureF"]
    #print df.head(1)

# <codecell>

dfsf2004["Daily Range"].head()

# <codecell>

dfDR2004 = dfsf2004[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2005 = dfsf2005[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2006 = dfsf2006[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2007 = dfsf2007[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2008 = dfsf2008[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2009 = dfsf2009[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2010 = dfsf2010[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2011 = dfsf2011[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2012 = dfsf2012[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2013 = dfsf2013[["Daily Range", "PST", "Mean TemperatureF"]]
sfDRfiles = [dfDR2004,dfDR2005,dfDR2006,dfDR2007,dfDR2008,dfDR2009,dfDR2010,dfDR2011,dfDR2012,dfDR2013]

# <codecell>


    

# <codecell>

dfwcttemp2004 = dfwc2004[["PST", "Mean TemperatureF"]]
dfwcttemp2005 = dfwc2005[["PST", "Mean TemperatureF"]]
dfwcttemp2006 = dfwc2006[["PST", "Mean TemperatureF"]]
dfwcttemp2007 = dfwc2007[["PST", "Mean TemperatureF"]]
dfwcttemp2008 = dfwc2008[["PST", "Mean TemperatureF"]]
dfwcttemp2009 = dfwc2009[["PST", "Mean TemperatureF"]]
dfwcttemp2010 = dfwc2010[["PST", "Mean TemperatureF"]]
dfwcttemp2011 = dfwc2011[["PST", "Mean TemperatureF"]]
dfwcttemp2012 = dfwc2012[["PST", "Mean TemperatureF"]]
dfwcttemp2013 = dfwc2013[["PST", "Mean TemperatureF"]]
wctempfiles = [dfwcttemp2004,dfwcttemp2005,dfwcttemp2006,dfwcttemp2007,dfwcttemp2008,dfwcttemp2009,dfwcttemp2010,dfwcttemp2011,dfwcttemp2012,dfwcttemp2013]

# <codecell>

for df in sfDRfiles:
    df.set_index("PST")

# <codecell>

for df in wctempfiles:
    df.set_index("PST")

# <codecell>

#compare_list = [pd.merge(elem[x],elen[y],on="PST") for elem in sfDRfiles and for elen in wctempfiles]
#dfwcsfcompare = pd.merge(dfwctemp,dfDR, on="PST")
# the merged lists with SF mean temp, WC mean temp, and SF daily range year round
dfcompare2004one = pd.merge(dfDR2004,dfwcttemp2004,on="PST")
dfcompare2005one = pd.merge(dfDR2005,dfwcttemp2005,on="PST")
dfcompare2006one = pd.merge(dfDR2006,dfwcttemp2006,on="PST")
dfcompare2007one = pd.merge(dfDR2007,dfwcttemp2007,on="PST")
dfcompare2008one = pd.merge(dfDR2008,dfwcttemp2008,on="PST")
dfcompare2009one = pd.merge(dfDR2009,dfwcttemp2009,on="PST")
dfcompare2010one = pd.merge(dfDR2010,dfwcttemp2010,on="PST")
dfcompare2011one = pd.merge(dfDR2011,dfwcttemp2011,on="PST")
dfcompare2012one = pd.merge(dfDR2012,dfwcttemp2012,on="PST")
dfcompare2013one = pd.merge(dfDR2013,dfwcttemp2013,on="PST")
#dfcompare2004one.head()
# to compare over ten years, merge all ten files 

# <codecell>

comparetenyears = [dfcompare2004one,dfcompare2005one,dfcompare2006one,dfcompare2007one,dfcompare2008one,dfcompare2009one,dfcompare2010one,dfcompare2011one,dfcompare2012one,dfcompare2013one]

#for df in comparetenyears:
 #   dftenyeardata = pd.merge(df,on"PST")
  #  print dftenyeardata.head()

# <codecell>

dfwcttemp2004.head()

# <codecell>

dfcompare2004two = dfcompare2004one.drop(dfcompare2004one.index[0:147])
dfcompare2005two = dfcompare2005one.drop(dfcompare2005one.index[0:147])
dfcompare2006two = dfcompare2006one.drop(dfcompare2006one.index[0:147])
dfcompare2007two = dfcompare2007one.drop(dfcompare2007one.index[0:147])
dfcompare2008two = dfcompare2008one.drop(dfcompare2008one.index[0:147])
dfcompare2009two = dfcompare2009one.drop(dfcompare2009one.index[0:147])
dfcompare2010two = dfcompare2010one.drop(dfcompare2010one.index[0:147])
dfcompare2011two = dfcompare2011one.drop(dfcompare2011one.index[0:147])
dfcompare2012two = dfcompare2012one.drop(dfcompare2012one.index[0:147])
dfcompare2013two = dfcompare2013one.drop(dfcompare2013one.index[0:147])
dfcompare2004two.head()

# <codecell>

dfcompare2004one.columns

# <codecell>

dfcompare2004three = dfcompare2004two.drop(dfcompare2004two.index[92:219])
dfcompare2005three = dfcompare2005two.drop(dfcompare2005two.index[92:219])
dfcompare2006three = dfcompare2006two.drop(dfcompare2006two.index[92:219])
dfcompare2007three = dfcompare2007two.drop(dfcompare2007two.index[92:219])
dfcompare2008three = dfcompare2008two.drop(dfcompare2008two.index[92:219])
dfcompare2009three = dfcompare2009two.drop(dfcompare2009two.index[92:219])
dfcompare2010three = dfcompare2010two.drop(dfcompare2010two.index[92:219])
dfcompare2011three = dfcompare2011two.drop(dfcompare2011two.index[92:219])
dfcompare2012three = dfcompare2012two.drop(dfcompare2012two.index[92:219])
dfcompare2013three = dfcompare2013two.drop(dfcompare2013two.index[92:219])



# mean temp y is Walnut Creek
dfcompare2004.tail()

# <codecell>

dfcompare2004 = dfcompare2004three.drop(["Mean TemperatureF_x"],1)
dfcompare2005 = dfcompare2005three.drop(["Mean TemperatureF_x"],1)
dfcompare2006 = dfcompare2006three.drop(["Mean TemperatureF_x"],1)
dfcompare2007 = dfcompare2007three.drop(["Mean TemperatureF_x"],1)
dfcompare2008 = dfcompare2008three.drop(["Mean TemperatureF_x"],1)
dfcompare2009 = dfcompare2009three.drop(["Mean TemperatureF_x"],1)
dfcompare2010 = dfcompare2010three.drop(["Mean TemperatureF_x"],1)
dfcompare2011 = dfcompare2011three.drop(["Mean TemperatureF_x"],1)
dfcompare2012 = dfcompare2012three.drop(["Mean TemperatureF_x"],1)
dfcompare2013 = dfcompare2013three.drop(["Mean TemperatureF_x"],1)
comparelist = [dfcompare2004,dfcompare2005,dfcompare2006,dfcompare2007,dfcompare2008,dfcompare2009,dfcompare2010,dfcompare2011,
               dfcompare2012,dfcompare2013] 

# <codecell>

for df in comparelist:
    print df.corr()
    

# <codecell>

#for df in comparelist:
 #   print df.dtypes

#dfcompare2004.dtypes

# <codecell>

for df in comparelist:
    df["PST"] = pd.to_datetime(df["PST"])

# <rawcell>


# <codecell>

#import seaborn as sns
#sns.tsplot(comparelist)
#from pandas.tools.plotting import scatter_matrix
#import matplotlib
#from matplotlib import rcParams
#print(matplotlib.rcParams.find_all())
#rcParams['figure.max_num_figures'] = 50
#for df in comparelist: 
 #   scatter_matrix(df[['Mean TemperatureF_y','Daily Range']],alpha=0.3, figsize=(10, 10), diagonal='kde'); 
dfcompare2013.head()

# <codecell>

#import matplotlib.pyplot as pl
#print comparelist
#for df in comparelist:
   # plt.scatter(df["Mean TemperatureF_y"], df["Daily Range"])

# <codecell>

dfDR2004 = dfsf2004[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2005 = dfsf2005[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2006 = dfsf2006[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2007 = dfsf2007[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2008 = dfsf2008[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2009 = dfsf2009[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2010 = dfsf2010[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2011 = dfsf2011[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2012 = dfsf2012[["Daily Range", "PST", "Mean TemperatureF"]]
dfDR2013 = dfsf2013[["Daily Range", "PST", "Mean TemperatureF"]]
sfDRfiles = [dfDR2004,dfDR2005,dfDR2006,dfDR2007,dfDR2008,dfDR2009,dfDR2010,dfDR2011,dfDR2012,dfDR2013]

# <codecell>

dfSF10yr = pd.read_csv('/Users/jana/anaconda/eda-pandas/data/eda-pandas/data/csvs/sf200414.csv')

# <codecell>

dfSF10yr.head()

# <codecell>

dfSF10yr.tail()

# <codecell>

dfSF10yrmean = dfSF10yr[["PST","Mean TemperatureF"]]
dfSF10yrmean.head()

# <codecell>

#dfSF10yrmean.plot()

# <codecell>

dfSF10yrmean2 = dfSF10yrmean.set_index("PST")
#dfSF10yrmean["PST"] = pd.to_datetime(dfSF10yrmean["PST"])

# <codecell>

dfSF10yrmean["PST"] = pd.to_datetime(dfSF10yrmean["PST"])

# <codecell>

dfSF10yrmean3 = dfSF10yrmean.groupby(dfSF10yrmean["PST"].map(lambda x: x.month))

# <codecell>

dfSF10yrmean3.head()

# <codecell>

dfSF10yrmean3.mean()

# <codecell>

dfmeans = dfSF10yrmean3.mean()
dfmeans.head()

# <codecell>

%pylab inline
pylab.rcParams['figure.figsize'] = (15.0,8.0)

#plt.xlabel("Average Temperature per Month, San Francisco 2004-2014", fontsize=18)
#plt.hist(dfDR["Daily Range"], 10, alpha=.7)
dfmeans.plot()

# <codecell>

sns.kdeplot(dfmeans["Mean TemperatureF"], shade=True); 

# <codecell>


# <codecell>


