import tushare as ts

ts.set_token('7766ffa92840e6d1b5f9777f9ea947941e847ab1216414f42f8b4491')
pro = ts.pro_api()

df = ts.pro_bar(ts_code='000001.SH', asset='I', freq='1min', start_date='20190425', end_date='20190426')
# df = ts.get_tick_data('600848',date='2019-04-29',src='tt')
print df
