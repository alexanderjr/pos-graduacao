
# coding: utf-8

# In[95]:


from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC


# In[57]:


iris = datasets.load_iris()
x = iris.data[:, :2]
y = iris.target


# In[58]:


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)


# In[118]:


rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
y_pred = rfc.predict(X_test)


# In[119]:


rfc_acc = round(accuracy_score(y_test, y_pred), 6)
rfc_recall = round(recall_score(y_test, y_pred, average='weighted'), 6)
rfc_precision = round(precision_score(y_test, y_pred, average='weighted'), 6)


# In[120]:


knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)


# In[121]:


knn_acc = round(accuracy_score(y_test, y_pred), 6)
knn_recall = round(recall_score(y_test, y_pred, average='weighted'), 6)
knn_precision = round(precision_score(y_test, y_pred, average='weighted'), 6)


# In[122]:


clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)


# In[123]:


clf_acc = round(accuracy_score(y_test, y_pred), 6)
clf_recall = round(recall_score(y_test, y_pred, average='weighted'), 6)
clf_precision = round(precision_score(y_test, y_pred, average='weighted'), 6)


# In[124]:


svc = SVC()
svc.fit(x, y)
y_pred = rfc.predict(X_test)


# In[116]:


svc_acc = round(accuracy_score(y_test, y_pred), 6)
svc_recall = round(recall_score(y_test, y_pred, average='weighted'), 6)
svc_precision = round(precision_score(y_test, y_pred, average='weighted'), 6)


# In[125]:


print("Random Forests\n vs KNeighborsClassifier\n vs DecisionTreeClassifier\n vs SVC")
print("Classes: {0}\n".format(iris.target_names))


# In[130]:


print("Acurácia: {0} vs {1} vs {2} vs {3}".format(rfc_acc, knn_acc, clf_acc, svc_acc))
print("Recall:  {0} vs {1} vs {2} vs {3}".format(rfc_recall, knn_recall,  clf_recall, svc_recall))
print("Precisão: {0} vs {1} vs {2} vs {3}".format(rfc_precision, knn_precision,  clf_precision, svc_precision))


# In[139]:


from sklearn.model_selection import cross_val_score
cv_rfc = cross_val_score(rfc, x, y, cv=5)
cv_knn = cross_val_score(knn, x, y, cv=5)
cv_svc = cross_val_score(svc, x, y, cv=5)
cv_clf = cross_val_score(clf, x, y, cv=5)

 
print("\nValidação cruzada:\n {0} vs\n {1} vs\n {2} vs\n {3}".format(cv_knn, cv_rfc, cv_svc, cv_clf))

exit()


# In[149]:


parameters = {'min_samples_split':(2,6)}
rfc_hps = GridSearchCV(rfc, parameters)
rfc_hps.fit(x, y)
print("Melhor valor para o parâmetro min_samples_split: {0}".format(rfc_hps.best_params_['min_samples_split']))


# In[150]:


#KNN
parameters = {'n_neighbors':(1,20)}
knn_hps = GridSearchCV(knn, parameters)
knn_hps.fit(x, y)
knn_hps.best_params_['n_neighbors']
print("Melhor valor para o parâmetro n_neighbors: {0}".format(knn_hps.best_params_['n_neighbors']))


# In[156]:


parameters = {'min_samples_split':(2,6)}
clf_hps = GridSearchCV(clf, parameters)
clf_hps.fit(x, y)
print("Melhor valor para o parâmetro min_samples_split: {0}".format(clf.best_params_['min_samples_split']))


# In[155]:


parameters = {'C':(1, 10)}
svc_hps = GridSearchCV(svc, parameters)
svc_hps.fit(x, y)
print("Melhor valor para o parâmetro min_samples_split: {0}".format(svc_hps.best_params_['C']))


# In[85]:


# parameters = {'n_neighbors':(1,20)}
# knn_hps = GridSearchCV(knn, parameters)
# knn_hps.fit(x, y)
# knn_hps.best_params_['n_neighbors']
# print("Melhor valor para o parâmetro n_neighbors: {0}".format(knn_hps.best_params_['n_neighbors']))

