from flask import Flask, jsonify
from flask import request
from action_sql.conn_sql import link_sep_dict
from action_sql.close_sql import close_db
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
  print('请求方式为------->', request.method)
  args = request.args.get("word") or "args没有参数"
  print('args参数是------->', args)
  # form = request.form.get('name') or 'form 没有参数'
  # print('form参数是------->', form)
  # return jsonify(args=args, form=form)
  # dict = {'word':'a','num':[1,2,3,4,5]}
  # if args == 'a':
  #   # result = jsonify(dict)
  #   result = json.dumps(dict)
  # return result
  if request.method == "GET":

    conn = link_sep_dict()  #实例化sql连接对象
    cur = conn.cursor()    #创建游标
    sql = "select * from cet4_dict_main where cet4_word= '%s'"% args  #sql语句
    cur.execute(sql)
    info = cur.fetchall()[0]

    word = info[1]
    phonetic = info[2].split('\n')
    translate = info[3].split('\n')
    distortion = info[4]
    sample = info[5].split('\n')
    print(sample)
    print(len(sample))
    sp1 = []
    sp2 = []
    sp3 = []
    sp4 = []
    sp5 = []
    sp6 = []
    samples = []


    for i in range(len(sample)):
      if i < 3:
        sp1.append(sample[i])
      elif i < 6 and i >= 3:
        sp2.append(sample[i])
      elif i < 9 and i >= 6:
        sp3.append(sample[i])
      elif i < 12 and i >= 9:
        sp4.append(sample[i])
      elif i < 15 and i >= 12:
        sp5.append(sample[i])
      else:
        sp6.append(sample[i])


    samples.append(sp1)
    samples.append(sp2)
    samples.append(sp3)
    samples.append(sp4)
    samples.append(sp5)
    samples.append(sp6)

    print(word)
    print(phonetic)
    print(translate)
    print(distortion)
    print(samples)

    dict = {'word':word,'phonetic':phonetic,'translate':translate,'distortion':distortion,'samples':samples}
    return json.dumps(dict)





if __name__ == '__main__':
  app.run(debug=True,host='192.168.1.3',port=88)