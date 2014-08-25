# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

df = pd.read_csv("weatherdata.csv")
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

# <rawcell>

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
plt.xlabel("Daily Temperature Range, San Francisco Jan 2013 - Feb 2014", fontsize=18)
plt.hist(dfDR["Daily Range"], 10, alpha=.7)
plt.hist(dfDR["Mean TemperatureF"], 10, alpha=.7);

# <codecell>

sns.jointplot(dfDR["Daily Range"], dfDR["Mean TemperatureF"], kind="hex", ylim=[40,75],xlim=[2.5,35]);

# <rawcell>

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

dfwc = pd.read_csv("weather_walnut_creek.csv")
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
    
dfwcbyDate = dfwc.set_index("PST")
dfbyDate = dfDR.set_index("PST")

dfnew = pd.merge(dfwcbyDate,dfbyDate)

dfwcbyDate

#dfnew.plot(figsize=(15,15));

# <codecell>


