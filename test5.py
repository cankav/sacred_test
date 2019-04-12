from sacred import Experiment
from sklearn import svm, datasets, model_selection

ex = Experiment("svm")

@ex.config
def cfg():
    C = 1.0
    gamma = 0.7
    kernel = "rbf"
    seed = 42

@ex.capture
def get_model(C, gamma, kernel):
    return svm.SVC(C=C, kernel=kernel, gamma=gamma)

@ex.automain  # Using automain to enable command line integration.
def run():
    X, y = datasets.load_breast_cancer(return_X_y=True)
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
    clf = get_model()  # Parameters are injected automatically.
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    ex.log_scalar('svm.score', score)
    return score
