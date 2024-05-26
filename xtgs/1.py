import pandas as pd


fina_df = pd.read_excel('/Users/sq/Downloads/gguf/fina.xlsx')
three_df = pd.read_excel('/Users/sq/Downloads/gguf/3.xlsx')


ip_col_fina = '私有IP地址'  # fina.xlsx中私有IP地址的列名
resource_name_col = '资源集名称'  # 3.xlsx中资源集名称的列名
ip_col_three = '私有IP地址'  # 3.xlsx中私有IP地址的列名


ip_to_resource = dict(zip(three_df[ip_col_three], three_df[resource_name_col]))

fina_df['系统S编号'] = fina_df[ip_col_fina].map(ip_to_resource)

fina_df['系统S编号'] = fina_df['系统S编号'].astype(str)
fina_df['系统S编号'] = fina_df['系统S编号'].str.extract(r'^([A-Za-z]+\d+)', expand=False)

fina_df.to_excel('/Users/sq/Downloads/gguf/updated_fina.xlsx', index=False)
