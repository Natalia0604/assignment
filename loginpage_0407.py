from flask import (Flask,request,redirect,session,render_template,jsonify)
import json
import mysql.connector
from mysql.connector import Error

app = Flask( __name__) 
app.secret_key= "somesecretkeythatonlyishouldknow"
app.config["DEBUG"] = True #顯示錯誤訊息
app.config['JSON_AS_ASCII'] = False #指示不要用ascii編碼處理中文(jsonify的處理方式)

#連接MYSQL資料庫
try:
    #主機名稱、帳號、密碼、選擇的資料庫
    connection = mysql.connector.connect(host="localhost",user="root",password="0604",database="website")
except Error as e:
    print("資料庫連接失敗: ", e)

# 建立查詢會員API
@app.route("/api/users",methods=["GET"])
def restAPI():
    #取得url上要求字串(Querrystring)欲查詢的會員帳號
    searchUsername=request.args.get("username"," ")
    #查詢 getQuerrystring 的會員帳號是否在mySQL user中
    mycursor = connection.cursor()
    mycursor.execute("SELECT username FROM user WHERE username = (%s)",(searchUsername,))
    conditionalData=mycursor.fetchall()  
    #判斷式:是否成功取得資料
    if (searchUsername,) in conditionalData:
        #取id、name、username的資料
        mycursor = connection.cursor()
        mycursor.execute("SELECT username FROM user WHERE username = (%s)",(searchUsername,))
        username = mycursor.fetchone()  #取username第一筆資料
        mycursor.execute("SELECT id FROM user WHERE username = (%s)",(searchUsername,))
        id = mycursor.fetchone()  #取id第一筆資料
        mycursor.execute("SELECT name FROM user WHERE username = (%s)",(searchUsername,))
        name = mycursor.fetchone()  #取name第一筆資料
        data={
        "data":{
            "id":id[0],
            "name":name[0],
            "username":username[0]
            }
        }
        return jsonify(data)
    else:
        wrongdata={"data":None} 
        return jsonify(wrongdata)

# 處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("w_index.html")

# 處理路徑 /signup 的對應函式 
@app.route("/signup", methods=["POST"])
def signup():
    # 確認使用POST方法連線，除此之外會導向回首頁
    if request.method =="POST":
        #接收前端註冊資料
        signupName=request.form["name"]
        signupUsername=request.form["username"]
        signupPassword=request.form["password"]

        #查詢user資料表中的username資料
        mycursor = connection.cursor()
        mycursor.execute("SELECT username FROM user WHERE username = (%s)",(signupUsername,))
        #取回全部的資料
        myuserdata = mycursor.fetchall()
        #檢查user資料表是否有重複的帳號: 
        # 重複→失敗頁網址(帳號已經被註冊)， 無重複→新增到資料表，註冊成功，導回首頁
        if (signupUsername,) in myuserdata:
            return render_template("w_fail.html",fail="帳號已經被註冊")
        else:
            newData = "INSERT INTO user (name,username,password) VALUES (%s,%s,%s)"
            newValues = (signupName, signupUsername,signupPassword)
            mycursor.execute(newData, newValues)
            connection.commit()
            return render_template("w_index.html")
    else:
        return render_template("w_index.html")

# 處理路徑 /signin 的對應函式
@app.route("/signin", methods=["GET", "POST"])
def signin():
    # 確認使用POST方法連線，除此之外會導向回首頁
    if request.method =="POST":
        #接收前端登入資料
        userId=request.form["id"]
        userPw=request.form["pw"]

        #查詢user資料表中的資料
        mycursor = connection.cursor()
        mycursor.execute("SELECT username,password FROM user WHERE username= (%s) AND password = (%s)",(userId,userPw))
        myuserdata = mycursor.fetchall()
        #檢查是否有對應的帳號、密碼
        #有→將name加入session，導向會員頁 ， 無→導向失敗頁(帳號或密碼錯誤)
        if (userId,userPw) in myuserdata:   
            session["user_id"] = userId #會存在cookies
            #欲從user資料表中取得使用者姓名
            mycursor.execute("SELECT name FROM user WHERE username = (%s)",(userId,)) #配合MYSQL格式
            myresult= mycursor.fetchall()
            session["name"] = myresult[0][0] #mysql回傳的值是tuple所以要加[0][0]才會只印出string
            return redirect("/member/")
        else:
            return redirect("/error/")
    else:
        return render_template("w_index.html")

# 處理路徑 /member 的對應函式
@app.route("/member/", methods=["GET", "POST"])
def success():
    user = session.get("user_id")
    getName = session.get("name")
    if user == None :
        return redirect('/')
    else:
        return render_template("w_success.html",signin=getName)

# 處理路徑 /error 的對應函式
@app.route("/error/")
def fail():
    #取得url的要求字串(Querrystring)
    message=request.args.get("message","帳號或密碼輸入錯誤")
    return render_template("w_fail.html",wrongMessage=message)
# 處理路徑 /signout 的對應函式
@app.route("/signout")
def signout():
    session.pop('user_id', None) #登出時一併消除儲存在cookies的資料
    session.pop('name', None) #登出時一併消除儲存在cookies的資料
    return redirect('/')

#啟動網站伺服器，可透過 port 參數指定埠號
app.run(port=3000)
