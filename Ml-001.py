from sklearn import tree
#Horsepower, No. of seats
features_task=[[300,2],[450,2],[200,8],[150,9]]
#Sports car=0, minivan=1
label_task=[0,0,1,1]
clf.fit(features_task,label_task)
preds=clf.predict([[400,8]])
print(preds)
