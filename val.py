'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-12-25 17:16:37
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-12-25 17:17:44
FilePath: /LLM_data/val.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd

path = "./ptt.csv"

df = pd.read_csv(path)

for index, row in df.iterrows():
    if row["text"] == None:
        print(index)