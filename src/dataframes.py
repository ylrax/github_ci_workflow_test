import pandas as pd


def create_empty_df():
	return pd.DataFrame([])
	
	
def create_simple_df():
	data = [10,20,30,40,50,60]
	return pd.DataFrame(data, columns=['Numbers'])
	
	
def create_full_df():
	df = pd.DataFrame({'a':pd.Series([10,20,30], dtype='int32'), 
			   'b':pd.Series([1.1,2.1,3.1], dtype='float32'),
			   'c':pd.Series(["a","b","c"], dtype='str'),
			   'd':pd.Series([1,0,0], dtype='bool'),
			   'e':pd.Series(['2019-01-03', '2010-01-03', '2000-01-10'], dtype='str'),})
	df['e'] = pd.to_datetime(df['e'], errors='coerce')
	return df

