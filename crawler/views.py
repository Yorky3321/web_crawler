from django.shortcuts import render
from BeautifulSoup import BeautifulSoup
import requests
import Selenium

# Create your views here.
def crawl(request):
    url = "http://example.com"  # 替換為你想爬取的網站
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 假設我們想抓取所有的標題
    titles = soup.find_all('h1')
    title_list = [title.get_text() for title in titles]
    
    return render(request, 'crawler/your_template.html', {'titles': title_list})