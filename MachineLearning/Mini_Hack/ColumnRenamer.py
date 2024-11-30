from sklearn.base import BaseEstimator, TransformerMixin

class ColumnRenamer(BaseEstimator, TransformerMixin):
    def __init__(self, rename_map):
        self.rename_map = rename_map

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.rename(columns=self.rename_map)

