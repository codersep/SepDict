# 连接数据库模块

import pymysql

# 连接mysql数据库
def link_sep_dict():
  try:
    conn = pymysql.connect(
      host='47.98.96.69',
      user='root',
      password='991118',
      port=3306, 
      db='sep_dict',
      charset='utf8',
      # autocommit=True,  # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。   
    )
  except:
    print('sep_dict连接失败')
  else:
    print('sep_dict连接成功')
    return conn

    
