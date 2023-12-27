'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-12-26 23:23:16
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-12-26 23:43:33
FilePath: \LLM_data\former\tester.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from transformers import AutoTokenizer
import pandas as pd

model_name = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# check one example can get how many tokens
data_path = "html2json.csv"
df = pd.read_csv(data_path)
prompt = df["prompt"][0]
text = df["text"][0]
rejected_text = df["rejected_text"][0]
print(df.isna().sum())
print(df.isnull().sum())
print("=====================================================")
print("prompt:", prompt)
print("text:", text)
print("rejected_text:", rejected_text)
print("prompt tokens:", tokenizer.tokenize(prompt))
print("text tokens:", tokenizer.tokenize(text))
print("rejected_text tokens:", tokenizer.tokenize(rejected_text))
print("prompt tokens length:", len(tokenizer.tokenize(prompt)))
print("text tokens length:", len(tokenizer.tokenize(text)))
print("rejected_text tokens length:", len(tokenizer.tokenize(rejected_text)))
print("=====================================================")
print("Total tokens length:", len(tokenizer.tokenize(prompt)) + len(tokenizer.tokenize(text)) + len(tokenizer.tokenize(rejected_text)))