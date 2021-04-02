from flask import Flask #載入 Flask
from flask import request #載入 Request 物件
from flask import redirect #載入 Redirect 函式
from flask import session 
from flask import render_template #載入 render_template 函式
import mysql.connector
from mysql.connector import Error

app = Flask( __name__) 
app.secret_key= "somesecretkeythatonlyishouldknow"

#連接MYSQL資料庫
try:
    #主機名稱、帳號、密碼、選擇的資料庫
    connection = mysql.connector.connect(host="localhost",user="root",password="0604",database="website")
except Error as e:
    print("資料庫連接失敗: ", e)

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
        mycursor.execute("SELECT username FROM user")
        #取回全部的資料
        myuserdata = mycursor.fetchall()

        #檢查user資料表是否有重複的帳號: 
        # 重複→失敗頁網址(帳號已經被註冊)， 無重複→新增到資料表，註冊成功，導回首頁
        if (signupUsername,) in myuserdata:
            return render_template("w_fail.html",fail="帳號已經被註冊")
        else:
            newData = "INSERT INTO user (name,username,password) VALUES (%s,%s,%s);"
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
        mycursor.execute("SELECT username,password FROM user ")
        myuserdata = mycursor.fetchall()

        #檢查是否有對應的帳號、密碼
        #有→將name加入session，導向會員頁 ， 無→導向失敗頁(帳號或密碼錯誤)
        if (userId,userPw) in myuserdata:   
            session["user_id"] = userId #會存在cookies
            #欲從user資料表中取得使用者姓名
            command= "SELECT name FROM user WHERE username = %s"
            adjectName =(userId,) #配合MYSQL格式
            mycursor.execute(command,adjectName)
            myresult= mycursor.fetchall()
            session["name"] = myresult[0][0] #mysql回傳的值是tuple所以要加[0][0]才會只印出string
            return redirect("/member/")
        else:
            return redirect("/error/")
    else:
        return render_template("w_index.html")

# 處理路徑 /member 的對應函式
@app.route("/member/")
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
