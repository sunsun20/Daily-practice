import pandas as pd

fina_df = pd.read_excel('/Users/sq/Downloads/gguf/updated_fina.xlsx')
two_df = pd.read_excel('/Users/sq/Downloads/gguf/2.xlsx')

# 确认列名
sys_s_col = '系统S编号'
current_status_col = '当前状态'  # 确保2.xlsx中也有此列名
team_col = '所属班组'  # 确保2.xlsx中也有此列名

# 去除2.xlsx中重复的系统S编号记录，假设我们只保留每个编号的第一次出现
two_df = two_df.drop_duplicates(subset=sys_s_col)

# 创建一个字典来存储2.xlsx中的系统S编号与当前状态和所属班组的映射
sys_to_info = two_df.set_index(sys_s_col)[[current_status_col, team_col]].to_dict(orient='index')

# 使用map函数填充updated_fina.xlsx的第二、三列
fina_df['当前状态'] = fina_df[sys_s_col].map(lambda x: sys_to_info.get(x, {}).get(current_status_col))
fina_df['所属班组'] = fina_df[sys_s_col].map(lambda x: sys_to_info.get(x, {}).get(team_col))

fina_df.to_excel('/Users/sq/Downloads/gguf/final_updated_fina.xlsx', index=False)