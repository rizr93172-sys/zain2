from distutils.log import debug
from fileinput import filename
from flask import *
import requests
#requests.get("https://zain.app/ar/contract-payment?contract=")
def ocean(file):

  from os import replace

  import pandas as pd
  import mechanize
  br = mechanize.Browser()
  br.set_handle_robots(False)


# read by default 1st sheet of an excel file
  dataframe1 = pd.read_excel(file)

  p1 = (dataframe1["رقم الحساب"])
  p2 = (dataframe1["متبقي سداد موثق"])
  p0 = (dataframe1["اسم العميل"])
  print(len(p1))
#print(p2[i])


  on = 0

  f = []
  while 1 :
    o  = open("total.txt","w")
    o.write(" ")
    o.close()
    xc = 0
    for i in range(60,len(p1)):
      on = on+1
      response = br.open("https://zain.app/ar/contract-payment?contract="+str(p1[i]))
      p  = (response.read())
      p22 = str(p).find("amount")
      p3 =str(p[p22:p22+100]).find("value")
      p4 = p[p22:][p3:p3+100]
      p5 = str(p4).find('"')
      p6 = str(p4).find("/")
      p7 = (str(p4)[p5:p6]).replace('"',"")
      a = str(p2[i]).replace(",","")
      b = p7.replace(",","")
      pr2 = int(b.find("."))

      try:
        pr1 = (int(a.replace(".","")))
        pr2 = (int(b.replace(".","")))

        if p1[i] in f:

          z = int(pr1) + int(f[1])
          pr1 = z
          f = []
          print(str(on)+"- "+str(pr1)+" , "+str(pr2)+" = ",pr1-pr2)
          if pr1-pr2 > 0:
            print(p0[i])
            print("done..")
            o1 = open("Capture0 (1).html","r")
            o1 = o1.read()
            o = open("Capture0 (1).html","w")
            o.write("<p>"+str(o1)+"\n"+"<p style = 'color:white;'>"+str(p0[i])+"</p>"+"\n"+"<p style = 'color:gray;'>"+"- "+str(p1[i])+" -- "+str(p7)+"</p>\n\n")
            o.close()

          print(p1[i])
        else:
          print(str(on)+"- "+str(pr1)+" , "+str(pr2)+" = ",pr1-pr2)
          print(p1[i])
          if pr1-pr2 > 0:
            print(p0[i])
            print("done..")
            o1 = open("Capture0 (1).html","r")
            o1 = o1.read()
            o = open("Capture0 (1).html","w")
            o.write("<p>"+str(o1)+"\n"+"<p style = 'color:white;'>"+str(p0[i])+"</p>"+"\n"+"<p style = 'color:gray;'>"+"- "+str(p1[i])+" -- "+str(p7)+"</p>\n\n")
            o.close()
          f = []
        f.append(p1[i])
        f.append(pr1)

        if pr1 > pr2 :
          print(p1[i])
          print("done")
          xc = xc +1
      except:
       pass
    print(" total: "+str(xc))
    o1 = open("Capture0 (1).html","r")
    o1 = o1.read()
    o = open("total.html","w")
    o.write(str(o1)+"\n"+"<\body> <\html>")
    o.close()
    return 1
    print("\n ---------------------------------")
    break



app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        user_input = request.form.get('num')
        print(user_input)
        f.save(str(user_input))

      #  name = str(f.filename)
      #  end = ocean(name)

        return render_template("end.html")




      #  return render_template("acknowledgement.html", name = p)

if __name__ == '__main__':
    app.run(debug=True)






















