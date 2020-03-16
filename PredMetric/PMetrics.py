import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

class PredictionMetrics(object):
    def __init__(self, model, X_train, X_test, y_train, y_test, is_log=False):
        """
        TESTING 123
        :param model:
        :param X_train:
        :param X_test:
        :param y_train:
        :param y_test:
        :param is_log:
        """
        self.model = model
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.is_log = is_log
        self.metric_df = pd.DataFrame()
        self._fill_metrics()

    def _fill_metrics(self):
        ll = []
        y_hat_train = self.model.predict(self.X_train)
        y_hat_test = self.model.predict(self.X_test)

        if self.is_log:
            y_hat_train = np.exp(y_hat_train)
            y_hat_test = np.exp(y_hat_test)

        ll.append([self.model.score(self.X_train, self.y_train), self.model.score(self.X_test, self.y_test)])
        ll.append([r2_score(self.y_train, y_hat_train), r2_score(self.y_test, y_hat_test)])
        ll.append([cross_val_score(self.model, self.X_train, self.y_train, cv=5).mean(),
                        cross_val_score(self.model, self.X_test, self.y_test, cv=5).mean()])
        ll.append([mean_squared_error(self.y_train, y_hat_train), mean_squared_error(self.y_test, y_hat_test)])
        ll.append([np.sqrt(mean_squared_error(self.y_train, y_hat_train)),
                        np.sqrt(mean_squared_error(self.y_test, y_hat_test))])
        ll.append([abs(self.y_train - y_hat_train).mean(), abs(self.y_test - y_hat_test).mean()])
        ll.append([cross_val_score(self.model, self.X_train, self.y_train, cv=5).round(3),
                   cross_val_score(self.model, self.X_test, self.y_test, cv=5).round(3)])

        self.metric_df = pd.DataFrame(ll, columns=["Train", "Test"])
        self.metric_df["Scores"] = ["lr.score", "r2_score",  "mean cross_val_score", "mean_squared_error", "root mean squared error", "residual mean", "cross_val_score",]
        self.metric_df = self.metric_df.reindex(columns=["Scores", "Train", "Test"])

        new_df = self.metric_df.drop([6], axis=0)
        mask = new_df["Train"] > new_df["Test"]
        new_df.loc[mask, "Result"] = "Train > Test"
        mask = new_df["Train"] < new_df["Test"]
        new_df.loc[mask, "Result"] = "Train < Test"
        new_df["Percent"] = ((new_df["Train"] - new_df["Test"]) / new_df["Test"]) * 100
        new_df.loc[6, :] = self.metric_df.loc[6, :]
        self.metric_df = new_df




