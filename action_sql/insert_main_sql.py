# 将爬取到的数据存储到数据库
def keep_sql(cur,conn,word,phonetic,translate,distortion,samples,tags):
  sql = "insert into cet4_dict_main (\
                                    cet4_word,\
                                    cet4_phonetic,\
                                    cet4_translate,\
                                    cet4_distortion,\
                                    cet4_samples,\
                                    cet4_tags\
                                    ) VALUES (%s, %s, %s, %s, %s, %s)"
  
  try:
    cur.execute(sql, (word, phonetic, translate, distortion, samples, tags))  # 执行sql插入语句
    conn.commit()  # 插入语句执行后需提交
  except:
    print()
    # conn.rollback() #报错则回滚到上一操作
    # return e.args  # 如果报错，返回错误信息
  else:
    print('插入数据成功')
  
