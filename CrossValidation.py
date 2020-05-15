import pandas as pd

veriler = pd.read_csv('veri.xlsx',sep=',') 
X=veriler.iloc[:,1:7])
y=veriler.iloc[:,7]


from sklearn.preprocessing import LabelEncoder 
le=LabelEncoder() 
y_le=le.fit_transform(y)

from sklearn import tree
clf = tree.DecisionTreeClassifier()#Karar ağacı ile sınıflandırma
from sklearn.model_selection import cross_val_score

score=cross_val_score(clf, X, y, cv=4)#Hangi algoritmayı kullanacağı ilk parametre X, y değerleri ve kfold değeri
print(score) #Her aşamadaki başarılı sonuçlar
print(score.mean()) #Değerlerin ortalaması

from sklearn.ensemble import RandomForestClassifier #Random forest ile sınıflandırma

rf = RandomForestClassifier(n_estimators=100, max_depth=45, random_state=0)
score=cross_val_score(rf, X, y, cv=4)


print(score)
print(score.mean())