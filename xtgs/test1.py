import pandas as pd

fina_df = pd.read_excel('/Users/sq/Downloads/gguf/2.xlsx')

print("列名列表:", fina_df.columns.tolist())