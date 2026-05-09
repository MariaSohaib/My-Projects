import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn import linear_model
df=pd.read_csv('StudentsFiles.csv')
features=['Study_Hours','Attendance','Marks']
k_model=KMeans(n_clusters=3)
k_clusters=k_model.fit_predict(df[features])
df['Cluster']=k_clusters
cluster_0=df[df['Cluster']==0]
cluster_1=df[df['Cluster']==1]
cluster_2=df[df['Cluster']==2]
plt.figure(figsize=(10,6))
plt.subplot(1,3,1)
plt.scatter(cluster_0['Attendance'],cluster_0['Marks'],label='1st Cluster',color='black')
plt.scatter(cluster_1['Attendance'],cluster_1['Marks'],label='2nd Cluster',color='red')
plt.scatter(cluster_2['Attendance'],cluster_2['Marks'],label='3rd Cluster',color='green')
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title('Clustering')
plt.legend()


plt.subplot(1,3,2)
t_model=DecisionTreeClassifier()
t_model.fit(df[features],df.Result)
plot_tree(t_model,feature_names=df[features].columns,filled=True)


x=df[['Attendance']]
y=df['Marks']
l_model=linear_model.LinearRegression()
l_model.fit(x,y)
plt.subplot(1,3,3)
plt.plot(x,l_model.predict(x),label="Regression Line")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.title('Relation Between Attendance and Marks')
plt.show()