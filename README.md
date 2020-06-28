https://www.linkedin.com/pulse/task5-mlsecops-integration-ml-security-rakesh-manwani

Create an automated system which will be useful for a server in terms of the following features:-

1. This system will keep a log of the information about the clients hit or request to the server, for example, we can get log file of a webserver at location /var/log/httpd/

2. This log data of clients will be used for finding the unusual pattern of a client request for example if a client is sending requests repeatedly. for this purpose, we can use here clustering to make clusters of different patterns of client request and to identify which cluster of client requests can cause some security and performance issue in the server

3. If any kind of unusual pattern we got then we can use Jenkins to perform a certain task for example it can run some command to block that IP which is causing this trouble.

I hope you got an Idea about this task So now lets jump on to the implementation part.

First, let's see the access_log file present at /var/log/httpd/ which stores the complete information about each Ip with their timing and content which they are getting.

In my case, I am using the server log file which was generated in the year 2015 which I have downloaded from the internet to do this practical with a large dataset.

No alt text provided for this image
If you see this file closely then we will get to know that all the fields are not required for us to make clustering because we only want to block those Ip's which are trying to do DOS ( Denial Of Service ) attack on our Httpd server so in that case we only require Ip's with their frequency which will be enough for us to find uncertain pattern.

So for this purpose we have removed unnecessary columns and did feature selection.

import pandas as pd

df=pd.read_csv("C:\\Users\\Rakesh\\Desktop\\access_log.csv")

df=df[['IP','Time']]
Here Ip and Time both the features are of type String but every machine learning model works on numeric data thus we need to convert these features to numeric values.

### calculated frequency of each Ip address

freq = {} 

for item in df['IP']: 

    if (item in freq): 

        freq[item] += 1

    else: 

        freq[item] = 1

key_list = list(freq.keys())   #### list of all Ips

val_list = list(freq.values()) #### frequency list of each Ip


### method to convert into numeric value

def str_ip2_int(s_ip):

    lst = [int(item) for item in s_ip.split('.')]

    int_ip = lst[3] | lst[2] << 8 | lst[1] << 16 | lst[0] << 24

    return int_ip

### converting each of the Ip into numeric value


j=0

for i in key_list:

   i=i.strip("[ -]")

   if i.split(".")[-1]=='':

   df['IP'][j]=(str_ip2_int(i))

   j=j+1


#### plotting frequency on graph 


import matplotlib.pyplot as plt

plt.scatter(key_list,val_list)

In addition to just convert into a numeric value, there were some Ip that was not in proper formate thus I have to make them in proper format using the strip method. And this is how scatter plot shows frequencies of Ip addresses.

No alt text provided for this image
After this, I have used the KMeans cluster to identify those Ip which is doing some DOS attack on our HTTP server.

from sklearn.cluster import KMeans


kmeans = KMeans(n_clusters=2)
kmeans.fit(df)

kmeans.cluster_centers_
After this, I have created another scatter plot that will show us actually which Ips are trying to do DOS attack and also I am storing those IP's into one file named "blocked_ip.txt" so that our Jenkins job can block all those IP's.

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

Now let's see Jenkins's job configuration to conclude this task5.

Job1(KMeans):- It will run my python file which will create the KMeans model and figure out all those IP's which are trying to do DOS attack. (complete Code is mentioned Above)

Job2:- this job will read blocked_ip.txt file to block all IP's listed in this file.


I hope you might have got some idea about this task5.

Thank you.................
