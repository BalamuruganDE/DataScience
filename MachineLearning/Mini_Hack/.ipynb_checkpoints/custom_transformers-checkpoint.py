from sklearn.base import BaseEstimator, TransformerMixin

class ColumnRenamer(BaseEstimator, TransformerMixin):
    def __init__(self, rename_map):
        self.rename_map = rename_map

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.rename(columns=self.rename_map)

    def get_feature_names_out(self, input_features=None):
        # Map the input feature names to the new names using the rename_map
        return [self.rename_map.get(col, col) for col in input_features]
