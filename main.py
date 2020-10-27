import datasets
import regression
import importlib
importlib.reload(regression)
X,Y= datasets.load_linear_example1()
# print(X)
# print(X[0])
# print(Y)

model = regression.LinearRegression()
model.fit(X,Y)
model.theta
model.predict(X)

print(model.theta)
print(model.predict(X))
