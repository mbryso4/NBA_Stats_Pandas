#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas
import csv
import pandas as pd


# In[3]:


NB20 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2020_totals.html')
NB19 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2019_totals.html')
NB18 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2018_totals.html')
NB17 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2017_totals.html')
NB16 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2016_totals.html')
NB15 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')
NB15 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2015_totals.html')
NB14 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2014_totals.html')
NB13 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2013_totals.html')
NB12 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2012_totals.html')
NB11 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2011_totals.html')
NB10 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2010_totals.html')
NB09 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2009_totals.html')
NB08 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2008_totals.html')
NB07 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2007_totals.html')
NB06 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2006_totals.html')
NB05 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2005_totals.html')
NB04 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2004_totals.html')
NB03 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2003_totals.html')
NB02 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2002_totals.html')
NB01 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2001_totals.html')
NB00 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_2000_totals.html')
NB99 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_1999_totals.html')
NB98 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_1998_totals.html')
NB97 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_1997_totals.html')
NB96 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_1996_totals.html')
NB95 = pandas.read_html('https://www.basketball-reference.com/leagues/NBA_1995_totals.html')


# In[4]:


NB20 = NB20[0].dropna(axis=0, thresh=4)
NB19 = NB19[0].dropna(axis=0, thresh=4)
NB18 = NB18[0].dropna(axis=0, thresh=4)
NB17 = NB17[0].dropna(axis=0, thresh=4)
NB16 = NB16[0].dropna(axis=0, thresh=4)
NB15 = NB15[0].dropna(axis=0, thresh=4)
NB14 = NB14[0].dropna(axis=0, thresh=4)
NB13 = NB13[0].dropna(axis=0, thresh=4)
NB12 = NB12[0].dropna(axis=0, thresh=4)
NB11 = NB11[0].dropna(axis=0, thresh=4)
NB10 = NB10[0].dropna(axis=0, thresh=4)
NB09 = NB09[0].dropna(axis=0, thresh=4)
NB08 = NB08[0].dropna(axis=0, thresh=4)
NB07 = NB07[0].dropna(axis=0, thresh=4)
NB06 = NB06[0].dropna(axis=0, thresh=4)
NB05 = NB05[0].dropna(axis=0, thresh=4)
NB04 = NB04[0].dropna(axis=0, thresh=4)
NB03 = NB03[0].dropna(axis=0, thresh=4)
NB02 = NB02[0].dropna(axis=0, thresh=4)
NB01 = NB01[0].dropna(axis=0, thresh=4)
NB00 = NB00[0].dropna(axis=0, thresh=4)
NB99 = NB99[0].dropna(axis=0, thresh=4)
NB98 = NB98[0].dropna(axis=0, thresh=4)
NB97 = NB97[0].dropna(axis=0, thresh=4)
NB96 = NB96[0].dropna(axis=0, thresh=4)
NB95 = NB95[0].dropna(axis=0, thresh=4)


# In[5]:


NB20['Season'] = 2020
NB19['Season'] = 2019
NB18['Season'] = 2018
NB17['Season'] = 2017
NB16['Season'] = 2016
NB15['Season'] = 2015
NB14['Season'] = 2014
NB13['Season'] = 2013
NB12['Season'] = 2012
NB11['Season'] = 2011
NB10['Season'] = 2010
NB09['Season'] = 2009
NB08['Season'] = 2008
NB07['Season'] = 2007
NB06['Season'] = 2006
NB05['Season'] = 2005
NB04['Season'] = 2004
NB03['Season'] = 2003
NB02['Season'] = 2002
NB01['Season'] = 2001
NB00['Season'] = 2000
NB99['Season'] = 1999
NB98['Season'] = 1998
NB97['Season'] = 1997
NB96['Season'] = 1996
NB95['Season'] = 1995


# In[6]:


frames = [NB20, NB19, NB18, NB17, NB16, NB15, NB14, NB13, NB12, NB11, NB10, NB09, NB08, NB07, NB06, NB05, NB04, NB03, NB02, NB01, NB00, NB99, NB98, NB97, NB96, NB95]
data = pd.concat(frames, axis = 0)
data


# In[7]:


data.to_csv (r'NBAStats95to20Totals.csv', index = False, header=True)


# In[ ]:




