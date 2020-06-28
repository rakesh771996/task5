
import pandas as pd

df=pd.read_csv("C:\\Users\\Rakesh\\Desktop\\access_log.csv")

from sklearn.cluster import KMeans


# In[158]:


model=KMeans()


# In[159]:


df


# In[160]:


df.drop('Unnamed: 0',inplace=True,axis=1)


# In[161]:


df


# In[162]:


freq = {} 
for item in df['IP']: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1


# In[163]:


print(key_list)


# In[164]:


import matplotlib.pyplot as plt
key_list = list(freq.keys()) 
val_list = list(freq.values()) 
plt.scatter(key_list,val_list)


# In[165]:


from sklearn.cluster import KMeans
# df1[0][0]


# In[166]:


key_list


# In[172]:


j=0
for i in key_list:
   print(i)
   i=i.strip("[ -]")
   if i.split(".")[-1]=='':
    i+="0"
   df['IP'][j]=(str_ip2_int(i))
   j=j+1


# In[169]:


df1=pd.DataFrame({'IP':key_list})
df2=pd.DataFrame({'freq':val_list})
df=pd.concat([df1,df2],axis=1)


# In[173]:


df


# In[171]:


def str_ip2_int(s_ip):
    lst = [int(item) for item in s_ip.split('.')]
    # [192, 168, 1, 100]
    int_ip = lst[3] | lst[2] << 8 | lst[1] << 16 | lst[0] << 24
    return int_ip


# In[174]:


kmeans = KMeans(n_clusters=2)
kmeans.fit(df)


# In[175]:


kmeans.cluster_centers_


# In[186]:


import matplotlib.pyplot as plt
import ipaddress
import os
j=0
for i in df['freq']:
    if int(i)>=300:
        ip=ipaddress.ip_address(df['IP'][j]).__str__()
        with open('blocked_ip.txt','a+') as file:
            file.write(""+ip+"\n")
        file.close()
        plt.scatter(df['IP'][j],i,c='red')
    else:
        plt.scatter(df['IP'][j],i,c='green')
        j+=1
plt.show()


# In[ ]:




