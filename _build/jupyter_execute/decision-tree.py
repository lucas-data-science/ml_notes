#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Latex


# #  Decision tree
# 
# 
# ![](https://myst-parser.readthedocs.io/en/latest/_static/logo-wide.svg)
# 
# $
# 1+2
# $
# 
# \begin{gather*}
# a_1=b_1+c_1\\
# a_2=b_2+c_2-d_2+e_2
# \end{gather*}
# 
# \begin{align}
# a_{11}& =b_{11}&
#   a_{12}& =b_{12}\\
# a_{21}& =b_{21}&
#   a_{22}& =b_{22}+c_{22}
# \end{align}
#  
# 
# ## Contents
#  
# * Classification
# * Regression 
#  

# # Plot Test

# In[2]:


from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
x = [x for x in range (10)]
y= x
plt.plot(x,y)


# In[ ]:




