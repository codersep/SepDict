# 关闭sql连接
def close_db(conn,cur):
  try:
    cur.close()
    conn.close()
  except:
    print('断开连接失败')
  else:
    print('断开连接成功')
