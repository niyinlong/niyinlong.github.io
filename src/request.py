import requests
from bs4 import BeautifulSoup
import re
import os
import html2text
import time
import random
import logging

base_url = "https://github.com/haizlin/fe-interview/issues?page="
start_page = 1  # 起始页码
end_page = 10   # 结束页码224
list = []

# 配置日志记录
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

# 定义issue类
class Issue:
  def __init__(self, category, url, title):
    self.category = category
    self.url = url
    self.title = title.replace("?.", "？.") # ?. 不能作为文件名
class Comment:
  def __init__(self, author, host, avatar, content, star):
    self.author = author if author else '无名'
    self.authorHost = host if host else ''
    self.avatar = avatar if avatar else ''
    self.content = content if content else '无'
    self.star = star if star else 0

# html 转 markdown
def html2Markdown(html):
  html = str(html)
  h = html2text.HTML2Text()
  h.body_width = 0  # 禁止自动换行
  h.mark_code = True
  h.emphasis_mark = ''
  h.ignore_links = True
  h.ignore_images = False
  markdown = h.handle(html)
  markdown = markdown.replace("[code]", "```").replace("[/code]", "```")
  return markdown

# 找出最优解
def getBeastAnswer(text):
  soup = BeautifulSoup(text, 'html.parser')
  items = soup.find_all('div', class_='js-comment-container')
  list = []
  for item in items:
    star = 0
    author = item.find('a', class_='author')
    avatar = item.find('img', class_='avatar')
    markdown = item.find('td', class_='markdown-body')
    starSpans = item.find_all('span', class_='js-discussion-reaction-group-count')
    for span in starSpans:
      star += int(span.get_text(strip=True))
    comment = Comment(author.get_text(strip=True), f"https://github"+author["href"], avatar["src"], html2Markdown(markdown), star)
    list.append(comment)
  if len(list) > 0:
    beast = max(list, key=lambda x: x.star)
    # 如果 只有一个答案，且点赞数少于5，则不认为答案有效
    if len(list) == 1 and beast.star < 5:
      return False
    else:
      return beast
  else:
    return False

# 获取问题的详情并存到文件夹
def getIssueDetail(list):
  for issue in list:
    url = f"https://github.com{issue.url}"
    response = requests.get(url)
    logging.info(f"开始抓取详情页：{url}")
    if response.status_code == 200:
      answer = getBeastAnswer(response.text)
      if answer:
        markdown = ""
        markdown = f"# {issue.title}\n\n作者：[{answer.author}]({answer.authorHost})\n\n"
        markdown += f"\n\n{answer.content}"
        
        fileName = f"./src/docs/{issue.category}/{issue.title}.md"
        filePath = f"./src/docs/{issue.category}"
        # 如果文件不存在则创建文件夹
        if not os.path.exists(filePath):
          os.makedirs(filePath)
        # 文本存储
        with open(fileName, "w", encoding="utf-8") as file:
          file.write(markdown)
        logging.info(f"{fileName}文件写入成功！")
        print(f"{fileName}文件写入成功！")
      else:
        print(f"{issue.title}没有找到答案")
    else:
      print(f"详情页抓取失败：{url}, status code: {response.status_code}")
    time.sleep(random.uniform(1, 3)) # 一个随机的延时，避免访问频繁被限制

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
  if list:
    getIssueDetail(list)

# 定义一个函数，用于 issues 列表
def fetchIssueList(base_url, start, end):
  for i in range(start, end + 1):
    url = f"{base_url}{i}"  # 拼接具体的网页地址
    print(f"开始抓取列表第{i}页：{url}")
    logging.info(f"开始抓取列表第{i}页：{url}")
    response = requests.get(url)
    if response.status_code == 200:
      html = BeautifulSoup(response.text, 'html.parser')
      getIssueDetailUrls(html)
    else:
      print(f"抓取失败：{url}, status code: {response.status_code}")

# 调用爬虫接口
fetchIssueList(base_url, start_page, end_page)