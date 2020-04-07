import  pandas_gbq
import pandas as pd
from google.oauth2 import service_account
from sklearn.linear_model import LogisticRegression

credentials = service_account.Credentials.from_service_account_file('./pipeline/credentials.json')

class Model:
    def __init__(self, model):
        self.model = model() 
    
    def load_data(self):
        # sql = '''
        #         SELECT l.increment_id order_code
        #                                 , max(ward_sellerboom_score) ward_sellerboom_score
        #                                 , max(ward_reseller_score) ward_reseller_score
        #                                 , max(ward_other_score) ward_other_score
        #                                 , s.* except(order_code, ward_sellerboom_score, ward_reseller_score, ward_other_score)
        #         FROM `tiki-dwh.sherlock.fraud_label_2020405` l
        #         LEFT JOIN `tiki-dwh.sherlock.feature_summary_*` s 
        #           ON cast(l.increment_id as string) = s.order_code
        #         GROUP BY 1, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18,19,20,21,22,23,24,25,26,27,28,29
        #                 ,30,31,32,33,34,35,36,37,38,39,40,41,42, 43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59
        #         '''
        sql = 'select * from `tiki-dwh.consumer_product.fraud_raw_data`'
        raw = pandas_gbq.read_gbq(sql, project_id='tiki-dwh', credentials=credentials)
        return raw
    def read_csv(self):
        return pd.read_csv('./pipeline/fraud_raw_data.csv')

    def preprocess(self):
        raw = self.read_csv()
        return raw
    def train():
        pass

if __name__ == '__main__':
    test = Model(LogisticRegression)
    test = test.preprocess()
    print(test.head())