"""Cross validation interface and functionalities"""
from sklearn.model_selection import KFold


def generate_folds(X, n_folds=5):
    kfolds = KFold(n_splits=n_folds, random_state=42, shuffle=True)
    for train_index, test_index in kfolds.split(X):
        X_train, X_test = X[train_index], X[test_index]
        yield X_train, X_test
