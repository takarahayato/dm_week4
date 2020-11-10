import datasets
import regression
import importlib
importlib.reload(regression)

X,Y = datasets.load_nonlinear_example1()
ex_X = datasets.polynomial3_features(X)

model = regression.RidgeRegression()
model.fit(ex_X,Y)
print(model.theta)
# print(model.alpha)


# print(X)
# print(ex_X)
# print(Y)
# importlib.reload(regression)
# X,Y= datasets.load_linear_example1()
# print(X)
# print(X[0])
# print(Y)

# model = regression.LinearRegression()
# model.fit(X,Y)
# model.theta
# model.predict(X)
# model.score(X,Y)
# print(model.theta)
# print(model.predict(X))
# print(model.score(X,Y))