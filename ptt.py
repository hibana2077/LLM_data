'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-12-25 14:47:25
LastEditors: hibana2077 hibana2077@gmaill.com
LastEditTime: 2023-12-25 18:03:53
FilePath: /LLM_data/ptt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup

page_urls = ["https://www.ptt.cc/bbs/C_Chat/index17527.html","https://www.ptt.cc/bbs/C_Chat/index17528.html","https://www.ptt.cc/bbs/C_Chat/index17529.html","https://www.ptt.cc/bbs/C_Chat/index17530.html","https://www.ptt.cc/bbs/C_Chat/index17531.html","https://www.ptt.cc/bbs/C_Chat/index17532.html"]
path = "https://www.ptt.cc/bbs/C_Chat/index.html"
data = {
    "prompt": [],
    "text": [],
    "rejected_text": []
}

for url in page_urls:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select('div[class="title"]')
    for title in titles:
        if title.a != None:
            # print(title.a.text)

            res2 = requests.get('https://www.ptt.cc'+title.a['href'])
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            content = soup2.select('div[id="main-content"]')[0].text.split('※ 發信站')[0]
            # remove first line
            content = content.split('\n', 1)[1]
            # remove all url (if in the line start with http)
            content = '\n'.join([i for i in content.split('\n') if not i.startswith('http')])
            # print(content)
            data['prompt'].append(title.a.text)
            data['text'].append(content)
            data['rejected_text'].append('I don\'t know what you are talking about.')
    print(f"progress: {page_urls.index(url)+1}/{len(page_urls)}")
    


# CSV
df = pd.DataFrame(data)
print(len(df))
# df.dropna(inplace=True)
df.to_csv('ptt.csv', index=False)

# JSON
with open('ptt.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
