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
  items = soup.find_all('div', class_='TimelineItem js-comment-container')
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
  if list:
    return max(list, key=lambda x: x.star)
  else:
    return False

# 获取问题的详情并存到文件夹
def getIssueDetail(list):
  for issue in list:
    response = requests.get(f"https://github.com{issue.url}")
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
  getIssueDetail(list)

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
fetchIssueList(base_url, start_page, end_page)
      
# 测试代码
# issue = Issue('css', '/haizlin/fe-interview/issues/17', '用css创建一个三角形，并简述原理')
# list.append(issue)
# getIssueDetail(list)