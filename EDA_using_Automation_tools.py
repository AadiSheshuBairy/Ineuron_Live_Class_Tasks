#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''EDA task using automation tools.
1. dtale
2. sweetviz
3. pandas profiling
'''


# In[1]:


import dtale
import pandas as pd
df = pd.read_csv(r"C:\Users\Shivanand\Downloads\Dataset\Dataset\data0\hr_imputed.csv")
d = dtale.show(df)
dtale.show(df)


# In[2]:


import pandas_profiling
df1 = pd.read_csv(r"C:\Users\Shivanand\Downloads\Dataset\Dataset\data0\hr_imputed.csv")
pandas_profiling.ProfileReport(df1)


# In[12]:


import sweetviz
import pandas as pd
df2 = pd.read_csv(r"C:\Users\Shivanand\Downloads\Dataset\Dataset\data0\hr_imputed.csv")
d2 = sweetviz.analyze(df2)
d2.show_html('FinalReport.html')


# In[ ]:




