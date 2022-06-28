#Using Tree model of Sklearn

from sklearn import tree

#[Height, weight, shoe size]

X = [[175, 78, 34], [145, 68, 44], [175, 78, 42], [125, 68, 24], [165, 58, 44], [
    125, 48, 24], [145, 45, 33], [135, 88, 44], [129, 45, 22], [175, 78, 34]]

Y = ['male', 'female', 'female', 'male', 'female',
     'female', 'male', 'female', 'male', 'female']

DTC = tree.DecisionTreeClassifier()

DTC = DTC.fit(X, Y)

prediction = DTC.predict([[190, 70, 43]])

print(prediction)
