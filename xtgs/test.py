import pandas as pd

df = pd.read_excel('/Users/sq/Downloads/gguf/2.xlsx')

duplicates = df['系统S编号'].duplicated(keep=False)

if duplicates.any():
    print("存在重复的系统S编号:")
    print(df[duplicates])
    print(f"共有 {duplicates.sum()} 个重复项")
else:
    print("没有发现重复的系统S编号")