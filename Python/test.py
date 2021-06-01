# from sklearn import preprocessing
# from sklearn import linear_model
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn import datasets
# from sklearn import neighbors
# import tensorflow as tf
# x = np.array([[7688, 32], [5788, 29], [4600, 25], [8900, 35]])
# # print(x)
#
#
# def a():
#     # 标准化
#     x_scaled = preprocessing.scale(x)
#     print(x_scaled)
#     # 均值
#     print(x_scaled.mean())
#     # 标准差
#     print(x_scaled.std())
#
#
# def b():
#     # 非线性转换
#     quantile = preprocessing.QuantileTransformer(random_state=0)
#     x_trans = quantile.fit_transform(x)
#     print(x_trans)
#
#
# def c():
#     # 归一化
#     x_norm = preprocessing.normalize(x, norm='l2')
#     print(x_norm)
#
#
# def d():
#     binary = preprocessing.Binarizer(threshold=100)
#     print(binary)
#
#
# def e():
#     iris = datasets.load_iris()
#     print(iris)
#     print(iris['data'].shape)
#     print(iris['target'].shape)
#     X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
#                                                         test_size=0.2, random_state=0)
#     print(X_train.shape)
#     print(X_test.shape)
#     print(y_train.shape)
#     print(y_test.shape)
#
#     knn = neighbors.KNeighborsClassifier(3)
#     print(knn.fit(X_train, y_train))
#     print(knn.score(X_test,y_test))
#
# def f():
#     reg= linear_model.LinearRegression()
#     print(reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2]))
#
#
# if __name__ == '__main__':
#     # a()
#     # b()
#     # c()
#     # d()
#     # e()
#     f()
#
#
#

