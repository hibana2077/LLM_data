'''
Author: hibana2077 hibana2077@gmaill.com
Date: 2023-12-25 14:47:25
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-12-26 23:45:54
FilePath: /LLM_data/ptt.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
import json
import pandas as pd
import fake_useragent as fu
from bs4 import BeautifulSoup

url_template = "https://ithelp.ithome.com.tw/?&page={}"
FROM = 1
TO = 1000
TEMPLATE_PROMPT_PART1 = """Please parse the following HTML source code into JSON format
Example:

<code>
<h1>hello</h1>
<code>

<json>
{ "h1": "hello" }
<json>
"""

TEMPLATE_PROMPT_PART2 = """
<code>
{html}
</code>
"""

TEMPLATE_TEXT = """<json>
{json}
</json>
"""

fake_agent = fu.UserAgent()
page_urls = [url_template.format(i) for i in range(FROM, TO)]
data = {
    "prompt": [],
    "text": [],
    "rejected_text": []
}

for idx,page_url in enumerate(page_urls):
    print("page_url:", page_url)
    response = requests.get(page_url, headers={
        "user-agent": fake_agent.random
    })
    soup = BeautifulSoup(response.text, "html.parser")
    for question in soup.find_all("div", class_="qa-list"):
        question: BeautifulSoup
        temp = question.find_all("span", class_="qa-condition__count")
        likes, replies, views = list(map(lambda x: x.text, temp))
        title = question.find("a", class_="qa-list__title-link").text
        user = question.find("a", class_="qa-list__info-link")
        user = user.text if user else "不明"
        post_time = question.find("a", class_="qa-list__info-time").text
        temp_data = {
            "likes": likes,
            "replies": replies,
            "views": views,
            "title": title.strip(),
            "user": user.strip(),
            "post_time": post_time
        }
        data["prompt"].append(TEMPLATE_PROMPT_PART1 + TEMPLATE_PROMPT_PART2.format(html=question))
        data["text"].append(TEMPLATE_TEXT.format(json=json.dumps(temp_data, ensure_ascii=False)))
        data["rejected_text"].append("I don't know how to parse this HTML source code into JSON format")
        # print("title:", title)
    print(f"progress: {idx+1}/{len(page_urls)}")

print("saving...")
df = pd.DataFrame(data)
df.to_csv("html2json.csv", index=False)
print("done")