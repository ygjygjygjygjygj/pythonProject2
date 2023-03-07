import numpy as np
import pandas as pd
data = pd.read_csv('D:\\xzDate\\data\\.ipynb_checkpoints\\train-checkpoint.csv', dtype={48: str, 51: str, 52: str})
data.head() # 查看前几行数据
data.describe() # 查看数据的统计信息
data.fillna(0, inplace=True)
data.drop_duplicates(inplace=True)
data = data.apply(lambda x: x * 2)
    data.to_csv('D:\\xzDate\\data\\cleaned_data.csv', index=False)