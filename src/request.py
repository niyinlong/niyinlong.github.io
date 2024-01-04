import requests
from bs4 import BeautifulSoup
import re
import os
import html2text

base_url = "https://github.com/haizlin/fe-interview/issues?page="
start_page = 1  # 起始页码
end_page = 1   # 结束页码224
list = []

# 定义issue类
class Issue:
  def __init__(self, category, url, title):
    self.category = category
    self.url = url
    self.title = title

def getIssueDetail(list):
  for issue in list:
    response = requests.get(f"https://github.com{issue.url}")
    if response.status_code == 200:
      html = BeautifulSoup(response.text, 'html.parser')
      markdown = html.find('div', class_='js-quote-selection-container').get_text(strip=True)
      ht = html2text.HTML2Text()
      ht.bypass_tables = False
      ht.mark_code = True
      ht.code = True
      markdown = ht.handle(f"# {issue.title}\n" + markdown + "\n\n")
      
      fileName = f"./src/docs/{issue.category}/{issue.title}.md"
      filePath = f"./src/docs/{issue.category}"
      # 如果文件不存在则创建文件夹
      if not os.path.exists(filePath):
        os.makedirs(filePath)
      # 文本存储
      with open(fileName, "w", encoding="utf-8") as file:
        file.write(markdown)
      # print(markdown)

def getIssueDetailUrls(html):
  list.clear() # 清空列表
  tags = html.find_all('a', {'class': 'Link--primary'})
  # 遍历每个链接标签，提取链接和文本内容
  for link_tag in tags:
      url = link_tag['href']
      title = link_tag.get_text(strip=True)
      pattern = re.compile(r'\[([^\]]+)\] 第(\d+)天 (.+)$')
      match = pattern.match(title)
      if (match):
        issue = Issue(match.group(1).strip(), url, match.group(3))
        list.append(issue)
  # getIssueDetail(list)

# 定义一个函数，用于 issues 列表
def fetchIssueList(base_url, start, end):
  for i in range(start, end + 1):
    url = f"{base_url}/{i}"  # 拼接具体的网页地址
    response = requests.get(url)
    if response.status_code == 200:
      html = BeautifulSoup(response.text, 'html.parser')
      getIssueDetailUrls(html)
    else:
      print(f"Failed to fetch content from {url}, status code: {response.status_code}")

# 调用爬虫接口
# fetchIssueList(base_url, start_page, end_page)
      
# 测试代码
issue = Issue('css', '/haizlin/fe-interview/issues/17', '用css创建一个三角形，并简述原理')
list.append(issue)
getIssueDetail(list)