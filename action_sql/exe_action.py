# sql执行模块
from action_sql.conn_sql import link_sep_dict
from action_sql.close_sql import close_db
from action_sql.read_sql import read_word_tag
from reptile_tools.yd_dict import get_yd
from action_sql.insert_main_sql import keep_sql

# class ExeAction():
#   def exe_conn(self):
#     conn = link_sep_dict()
#     cur = conn.cursor()
#     db = [conn,cur]
#     return db
#
#   def exe_close(self,conn,cur):
#     close_db(conn,cur)


class ExeAction:
  # 建立数据库连接
  def sql_conn(self):
    self.conn = link_sep_dict()
    self.cur = self.conn.cursor()
    
  # 查询到word字段数据，并爬取到相应单词信息
  def trans_word(self):
    word_data = read_word_tag(self.cur)
    for i in range(len(word_data[0])):
      word = word_data[0][i]
      tag = word_data[1][i]
      dict_data = get_yd(word)
      keep_sql(self.cur,self.conn,word,dict_data[0],dict_data[1],dict_data[2],dict_data[3],tag)
      # print(word,dict_data[0],dict_data[1],dict_data[2],dict_data[3],tag)
      
      # print(word + ' ' + tag)
    
  # 断开数据库连接
  def sql_close(self):
    close_db(self.conn, self.cur)

  
if __name__ == '__main__':
  exe = ExeAction()
  exe.sql_conn()
  exe.trans_word()
  exe.sql_close()
