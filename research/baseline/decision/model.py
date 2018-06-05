#!/usr/local/bin/python
# coding:utf-8

import math
# Linear Regression Classifier
def linear_regression_classifier():
    from sklearn import linear_model
    model = linear_model.LinearRegression()
    param_grid = dict()
    return model, param_grid
 
# Gaussian Naive Bayes Classifier
def gaussian_bayes_classifier():
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    param_grid = dict()
    return model,param_grid

# Multinomial Naive Bayes Classifier
def naive_bayes_classifier():
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB()
    param_grid = {'alpha': [math.pow(10,-i) for i in range(11)]}
    return model,param_grid
 
# KNN Classifier
def knn_classifier():
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()
    param_grid = {'n_neighbors': list(range(1,100))}
    return model
 
# Logistic Regression Classifier
def logistic_regression_classifier():
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression(penalty='l2')
    param_grid = dict()
    return model, param_grid
 
# Random Forest Classifier
def random_forest_classifier():
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    param_grid = {'n_estimators' : list(range(1,21)), 'max_depth' : list(range(1,6)), 'max_features' : list(range(1,500))}
    return model
 
# Decision Tree Classifier
def decision_tree_classifier(i):
    from sklearn.tree import DecisionTreeClassifier

    model = DecisionTreeClassifier(max_depth=i)
    # param_grid = {'max_depth' : list(range(1,11,2))}
    return model
 
# GBDT(Gradient Boosting Decision Tree) Classifier
def gradient_boosting_classifier():
    from sklearn.ensemble import GradientBoostingClassifier 
    model = GradientBoostingClassifier()
    param_grid = {'n_estimators': list(range(100,200,20))}
    return model, param_grid

# SVM Classifier
def svm_classifier():
    from sklearn.svm import SVC
    model = SVC(kernel="linear", C=0.025)
    param_grid = {'C': [1e-2, 1e-1, 1, 10]}
    return model, param_grid
 
# SVM Classifier using cross validation
def svm_cross_classifier():
    from sklearn.svm import SVC
    model = SVC(gamma=2, C=1)
    param_grid = {'C': [1e-1, 1, 10], 'gamma': [1,2,3,4,5]}
    return model, param_grid

# AdaBoost Classifier
def ada_boost_validation():
    from sklearn.ensemble import AdaBoostClassifier
    model = AdaBoostClassifier(n_estimators=100)
    param_grid = {'n_estimators' : [50, 100, 200]}
    return model

# LinearDiscriminantAnalysis Classifier
def linear_discriminant_analysis():
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    model = LinearDiscriminantAnalysis()
    param_grid = dict()
    return model, param_grid

# QuadraticDiscriminantAnalysis Classifier
def quadratic_discriminant_analysis():
    from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
    model = QuadraticDiscriminantAnalysis()
    param_grid = dict()
    return model, param_grid

# Extra Trees Classifier
def extra_trees_classifier():
    from sklearn.ensemble import ExtraTreesClassifier
    model = ExtraTreesClassifier(n_estimators=10, max_depth=None)
    param_grid = {'n_estimators' : list(range(1,21))}
    return model, param_grid

def neural_network_classifier():
    from sklearn.neural_network import MLPClassifier
    model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    param_grid = dict()
    return model

def xgboost_classifier():
    from xgboost import XGBClassifier
    model = XGBClassifier()
    param_grid = dict()
    return model, param_grid