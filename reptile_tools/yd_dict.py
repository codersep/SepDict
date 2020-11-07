# 爬取有道词典数据模块
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


# 请求url获取html源码，并解析文档
def get_yd(word):
  url1 = 'http://dict.youdao.com/w/eng/'+ word +'/#keyfrom=dict2.index'
  url2 = 'http://dict.youdao.com/example/blng/eng/'+ word +'/#keyfrom=dict.main.moreblng'
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
  ret1 = urlopen(Request(url1, headers=headers)) #打开网站
  ret2 = urlopen(Request(url2, headers=headers))  
  contents1 = ret1.read() #读取网页
  contents2 = ret2.read()
  
  soup1 = BeautifulSoup(contents1, "html.parser")
  soup2 = BeautifulSoup(contents2, "html.parser")


# 获取音标  
  finalPhonetic = ''
  for i in range(len(soup1.select('span[class="pronounce"]'))):
    phonetic = soup1.select('span[class="pronounce"]')[i].get_text()
    ptc = ":".join(phonetic.split())
    if i!=0:
      finalPhonetic = finalPhonetic + "\n" + ptc
    else:
      finalPhonetic = ptc


# 获取译文
  finalMeaning = ''
  for i in range(len(soup1.select('div[id="phrsListTab"] > div[class="trans-container"] > ul > li'))):
    meaning = soup1.select('div[id="phrsListTab"] > div[class="trans-container"] > ul > li')[i].get_text() + '\n'
    mng = "".join(meaning.split())

    if i!=0:
      finalMeaning = finalMeaning + "\n" + mng
    else:
      finalMeaning = mng



# 获取单词表达形式：
  finalDistortion = ''
  if (soup1.select('div[id="phrsListTab"] > div[class="trans-container"] > p')):  #判断是否存在p元素
    mode = soup1.select('div[id="phrsListTab"] > div[class="trans-container"] > p')[0].get_text()
    finalDistortion = " ".join(mode.split())



# 获取例句
  finalSample = ""
  sp_lens = len(soup2.select('ul[class="ol"] p'))
  if sp_lens > 18:
    sp_lens = 18
  for i in range(sp_lens):
    sp = soup2.select('ul[class="ol"] p')[i].get_text()
    sample = " ".join(sp.split())
    if (i != 0):
      finalSample = finalSample + "\n" + sample
    else:
      finalSample = sample


  yd_result = []
  yd_result.append(finalPhonetic)
  yd_result.append(finalMeaning)
  yd_result.append(finalDistortion)
  yd_result.append(finalSample)
  return(yd_result)


if __name__ == "__main__":
  # parseYd("word")
  print(parse_yd('word')[0])
