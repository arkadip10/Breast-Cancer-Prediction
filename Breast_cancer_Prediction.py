"""
Created on Mon Feb  5 01:54:28 2018

@author: ARKADIP GHOSH & AISHWARJYAMOY MUKHERJEE
"""


import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
data_set=pd.read_csv("Breast_cancer.csv")
x=data_set.iloc[:,:-1].values
y=data_set.iloc[:,-1].values
#split data set into training and testing sets
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=100)





#logistic regression model fitted on training set
from sklearn.linear_model import LogisticRegression
logic=LogisticRegression()
logic.fit(x_train,y_train)
predicted_value=logic.predict(x_test)
logic.score(x_test,y_test)#94.73%accuracy
#logic.score(x_train,y_train)#95.60%accuracy



from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predicted_value))
from sklearn.svm import SVC
clf1=SVC()#linear kernal
clf1.fit(x_train,y_train)
pre_value=clf1.predict(x_test)
print(accuracy_score(y_test,pre_value))#65.78%accuracy
#clf1.score(x_train,y_train)#100% accuracy




from sklearn.svm import SVC
clf2=SVC(kernel='poly',degree=2,probability=True)
clf2.fit(x_train,y_train)
clf2.score(x_test,y_test)#95.6% accuracy
#clf2.score(x_train,y_train)#97.8% acccuracy




def give_value(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,b1,c1,d1):
    l1=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,a1,b1,c1,d1]
    l2=np.array([l1])
    l2.reshape(-1,1)  
    print([logic.predict(l2),clf1.predict(l2)])






from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
dt.score(x_test,y_test)#95.61% accuracy
#dt.score(x_train,y_train)#training accuracy is 100% so the model is overfitting





from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=20)
rf.fit(x_train,y_train)
rf.score(x_test,y_test)#92.98% accuracy
#rf.score(x_train,y_train)#training accuracy is 99.7%



#bagging
from sklearn.ensemble import BaggingClassifier
bg=BaggingClassifier(DecisionTreeClassifier(),max_samples=0.8,max_features=1,n_estimators=20)
bg.fit(x_train,y_train)
bg.score(x_test,y_test)#accuracy 80.70%
#bg.score(x_train,y_train)#accuracy 98.24%




#Adaboost
from sklearn.ensemble import AdaBoostClassifier
adb=AdaBoostClassifier(DecisionTreeClassifier(),n_estimators=20,learning_rate=1)
adb.fit(x_train,y_train)
adb.score(x_test,y_test)#92.98% accuracy
#adb.score(x_train,y_train)#100% accuracy



#voting classifier
from sklearn.ensemble import VotingClassifier
evc=VotingClassifier(estimators=[('logic',logic),('clf1',clf1),('dt',dt)],voting='hard')
evc.fit(x_train,y_train)
evc.score(x_test,y_test)#93.73% accuracy
#evc.score(x_train,y_train)#100% accuracy



   
"""from sklearn import metrics
# calculate the fpr and tpr for all thresholds of the classification
probs = rf.predict_proba(x_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds,pos_label='B')
roc_auc = metrics.auc(fpr, tpr)
# method I: plt
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()







from sklearn import metrics
# calculate the fpr and tpr for all thresholds of the classification
clf2.probability=True
probs = clf2.predict_proba(x_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds,pos_label='B')
roc_auc = metrics.auc(fpr, tpr)

# method I: plt
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()"""




















