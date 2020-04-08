from collections import defaultdict
import pandas as pd 
import sys
import json
import pickle


class OrderScore():
	def __init__(self, data):
		self.data = data
		
	def data_validation(self):
		order_list = self.data
		df = []

		for order in order_list:
			feature = {}
			feature['order_code'] = order['order_code']
			feature['profile_score'] = order['customer_profile_score']
			feature['total_orders'] = order['customer_total_orders']
			feature['total_success_orders'] = order['customer_total_success_orders']
			feature['canceled_orders'] = order['customer_canceled_orders']
			feature['success_rate'] =order['customer_success_rate']
			feature['skuscore'] =order['customer_sku_score']
			feature['skuscore_non_gift'] =order['customer_non_gift_sku_score']
			feature['whitescore'] =order['customer_white_score']
			feature['fb_score'] =order['customer_fb_score']
			feature['gg_score'] =order['customer_gg_score']
			feature['avt_score'] =order['customer_avt_score']
			feature['demographicscore'] =order['customer_demographic_score']
			feature['register_to_date'] =order['customer_register_to_date']
			feature['customer_fraud_score'] =order['customer_fraud_score']
			feature['customer_fraud_score_non_gift'] =order['customer_non_gift_fraud_score']
			feature['product_key_score'] =order['product_scores']['product_key_score']
			feature['cate2_score'] =order['product_scores']['cate2_score']
			feature['product_fraud_score'] =order['product_scores']['product_fraud_score']
			feature['district_reseller'] =order['district_scores']['reseller']
			feature['district_sellerboom'] =order['district_scores']['sellerboom']
			feature['district_other'] =order['district_scores']['other']
			feature['ward_reseller'] = order['ward_scores'].get('reseller', 0)
			feature['ward_sellerboom'] = order['ward_scores'].get('sellerboom',0)
			feature['ward_other'] = order['ward_scores'].get('other', 0)
			feature['customer_email_4ml_1h_count'] = order['customer_email_4ml_1h_count']
			feature['customer_email_4ml_24h_count'] = order['customer_email_4ml_24h_count']
			feature['customer_email_4ml_48h_count'] = order['customer_email_4ml_48h_count']
			feature['customer_ip_4ml_1h_count'] = order['customer_ip_4ml_1h_count']
			feature['customer_ip_4ml_24h_count'] = order['customer_ip_4ml_24h_count']
			feature['customer_ip_4ml_48h_count'] = order['customer_ip_4ml_48h_count']
			feature['register_date_4ml_1h_count'] = order['register_date_4ml_1h_count']
			feature['register_date_4ml_24h_count'] = order['register_date_4ml_24h_count']
			feature['register_date_4ml_48h_count'] = order['register_date_4ml_48h_count']
			feature['region_4ml_1h_count'] = order['region_4ml_1h_count']
			feature['region_4ml_24h_count'] = order['region_4ml_24h_count']
			feature['fe_region_dist_4ml_1h_count'] = order['fe_region_dist_4ml_1h_count']
			feature['fe_region_dist_4ml_24h_count'] = order['fe_region_dist_4ml_24h_count']
			feature['fe_region_dist_4ml_48h_count'] = order['fe_region_dist_4ml_48h_count']
			feature['fe_dist_ward_4ml_1h_count'] = order['fe_dist_ward_4ml_1h_count']
			feature['fe_dist_ward_4ml_24h_count'] = order['fe_dist_ward_4ml_24h_count']
			feature['fe_dist_ward_4ml_48h_count'] = order['fe_dist_ward_4ml_48h_count']
			feature['fe_telephone_4ml_1h_count'] = order['fe_telephone_4ml_1h_count']
			feature['fe_telephone_4ml_24h_count'] = order['fe_telephone_4ml_24h_count']
			feature['fe_telephone_4ml_48h_count'] = order['fe_telephone_4ml_48h_count']
			feature['total_amount_48h'] = order['total_amount_48h']
			feature['total_amount_24h'] = order['total_amount_24h']
			feature['total_amount_1h'] = order['total_amount_1h']
			feature['wfp_customer_id_count'] = order['wfp_customer_id_count']
			feature['customer_ip_count'] = order['customer_ip_count']
			feature['new_user'] = order['new_user']
			feature['seller_customer_ip_1h_count'] = order['seller_customer_ip_1h_count'][0]['count']
			feature['seller_customer_id_count'] = order['seller_customer_id_count'][0]['count']
			feature['cate2_customer_id_count'] = order['cate2_customer_id_count'][0]['count']
			feature['sku_customer_id_count'] = order['sku_customer_id_count'][0]['count']

			df.append(feature)

		df1 = pd.DataFrame(df)
		df1.set_index('order_code', inplace=True)
		df2 = df1.fillna(0)
		return df2
	
	def _predict(self):
		with open('./pipeline/test_model.sav', 'rb') as f:
			model = pickle.load(f)
		
		raw = self.data_validation()
		scores = model.predict(raw)
		# prob = model.predict_proba(df)[:, 1]
		return scores