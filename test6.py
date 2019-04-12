from sacred import Experiment
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import cross_val_score

ex = Experiment("svm")

@ex.config
def linear_cfg():
    kernel='linear'
    test_size=0.4
    random_state=0

@ex.named_config
def rbf_cfg():
    kernel='rbf'
    test_size=0.4
    random_state=0

@ex.capture
def run_cross_val(kernel, test_size, random_state):
    X, y = datasets.load_breast_cancer(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size,
        random_state=random_state)

    clf = svm.SVC(kernel=kernel, C=1)
    scores = cross_val_score(clf, X_train, y_train, cv=5)
    print(scores)
    for score in scores:
        ex.log_scalar('svm.cv.scores', score)

@ex.automain
def automain():
    run_cross_val()
