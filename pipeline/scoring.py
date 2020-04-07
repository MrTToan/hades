from collections import defaultdict
import pandas as pd 
import sys
import json
import pickle


class OrderScore():
	def __init__(self, data):
		self.data = data
		

	def data_validation(self):
	# try:
		order_list = json.loads(self.data)
		df = []
		print('Order list {}'.format(order_list))

		for order in order_list:
			# try:
			feature = {}
			feature['cust_score'] = order['cust_score']
			feature['product_score'] = order['product_score']
			feature['location_score'] = order['location_score']
			print(feature)
				
			# finally:
			df.append(feature)

		df1 = pd.DataFrame(df)
		df2 = df1.fillna(0)
	# except:
		print(f"Error here: {sys.exc_info()[0]}")
	# finally:
		return df2
	
	def _predict(self):
		with open('./pipeline/test_model.sav', 'rb') as f:
			model = pickle.load(f)
		
		raw = self.data_validation()
		scores = model.predict(raw)
		# prob = model.predict_proba(df)[:, 1]
		return scores


# feature['order_code'] = order['order_code']
					# feature['profile_score'] = 
					# feature['total_orders'] = 
					# feature['total_success_orders'] = 
					# feature['canceled_orders'] =
					# feature['success_rate'] =
					# feature['skuscore'] =
					# feature['skuscore_non_gift'] =
					# feature['whitescore'] =
					# feature['fb_score'] =
					# feature['gg_score'] =
					# feature['avt_score'] =
					# feature['demographicscore'] =
					# feature['register_to_date'] =
					# feature['customer_fraud_score'] =
					# feature['customer_fraud_score_non_gift'] =
					# feature['product_key_score'] =
					# feature['cate2_score'] =
					# feature['product_fraud_score'] =
					# feature['district_reseller'] =
					# feature['district_sellerboom'] =
					# feature['district_other'] =
					# feature['ward_reseller'] = 
					# feature['ward_sellerboom'] = 
					# feature['ward_other'] = 
					# feature['customer_email_4ml_1h_count'] = 
					# feature['customer_email_4ml_24h_count'] = 
					# feature['customer_email_4ml_48h_count'] = 
					# feature['customer_ip_4ml_1h_count'] = 
					# feature['customer_ip_4ml_24h_count'] = 
					# feature['customer_ip_4ml_48h_count'] = 
					# feature['register_date_4ml_1h_count'] = 
					# feature['register_date_4ml_24h_count'] = 
					# feature['register_date_4ml_48h_count'] = 
					# feature['region_4ml_1h_count'] = 
					# feature['region_4ml_24h_count'] = 
					# feature['fe_region_dist_4ml_1h_count'] = 
					# feature['fe_region_dist_4ml_24h_count'] = 
					# feature['fe_region_dist_4ml_48h_count'] = 
					# feature['fe_dist_ward_4ml_1h_count'] = 
					# feature['fe_dist_ward_4ml_24h_count'] = 
					# feature['fe_dist_ward_4ml_48h_count'] = 
					# feature['fe_telephone_4ml_1h_count'] = 
					# feature['fe_telephone_4ml_24h_count'] = 
					# feature['fe_telephone_4ml_48h_count'] = 
					# feature['total_amount_48h'] = 
					# feature['total_amount_24h'] = 
					# feature['total_amount_1h'] = 
					# feature['wfp_customer_id_count'] = 
					# feature['customer_ip_count'] = 
					# feature['new_user'] = 
					# feature['seller_customer_ip_1h_count'] = 
					# feature['seller_customer_id_count'] = 
					# feature['cate2_customer_id_count'] = 
					# feature['sku_customer_id_count'] = 
r = '''
	{
		"cust_score": 5,
		"product_score": 7,
		"location_score": 8
	}
'''
# test = Or
# derScore(r)
# # # df = test.data_validation()
# sc = test._predict()
# print(sc)