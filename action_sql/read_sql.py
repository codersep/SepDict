# 查询word数据
# 并解析后传入爬虫程序

def read_word_tag(cur):
  try:
    sql = "select word,tags from cet4_dict_list;" #sql语句
    cur.execute(sql)  # 执行sql语句，默认不返回查询结果集，只返回数据记录数。
    info = cur.fetchall()     # 读取所有的word结果
  except:
    print('查询语句执行失败')
  else:
    print('查询语句执行成功')
    words = []   #单词表
    tags = []  #标签表
    # 解析获取出来的word数据
    for i in range(len(info)):
      word = "".join(info[i][0].split())
      tag = "".join(info[i][1].split())
      words.append(word)  #解析出来的单词加入单词表中
      tags.append(tag)
    read_data = [words,tags]
    return read_data
  
  
  




