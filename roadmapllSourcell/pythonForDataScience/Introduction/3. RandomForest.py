#Using Random Forest model of Sklearn

from sklearn.ensemble import RandomForestClassifier

#[Height, weight, shoe size]

X = [[175,78,34], [145,68,44], [175,78,42],[125,68,24], [165,58,44], [125,48,24], [145,45,33], [135,88,44], [129,45,22], [175,78,34]]

Y = ['male', 'female', 'female', 'male', 'female', 'female', 'male', 'female', 'male', 'female']

RF = RandomForestClassifier(n_estimators = 2)

RF = RF.fit(X,Y)

prediction = RF.predict ([[190,70,43]])

print (prediction)