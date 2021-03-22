from flask import Flask #載入 Flask
from flask import request #載入 Request 物件
from flask import redirect #載入 Redirect 函式
from flask import session 
from flask import render_template #載入 render_template 函式

app = Flask( __name__) 
app.secret_key= "somesecretkeythatonlyishouldknow"

# 建立使用者資料
# class User:
#     def __init__(self, id, password):
#         self.id = id
#         self.password = password
# users = []
# users.append(User(id="test", password="test"))

# 處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("w_index.html")

# 處理路徑 /signin 的對應函式
@app.route("/signin", methods=["GET", "POST"])
def signin():
    # 確人使用POST方法連線，除此之外會導向回首頁
    if request.method =="POST":
        session.pop("user_id", None)
        userId=request.form["id"]
        userPw=request.form["pw"]
        
        #檢查user輸入的資料是否正確
        if userId == "test" :
            if userPw == "test":
                session["user_id"] = userId #會存在cookies
                return redirect("/member/")
            else :
                return redirect("/error/")
        else:
            return redirect("/error/")
    else:
        return render_template("w_index.html")

# 處理路徑 /member 的對應函式
@app.route("/member/")
def success():
    user = session.get("user_id")
    if user == None :
        return redirect('/')
    else:
        return render_template("w_success.html")

# 處理路徑 /error 的對應函式
@app.route("/error/")
def fail():
    return render_template("w_fail.html")

# 處理路徑 /signout 的對應函式
@app.route("/signout")
def signout():
    session.pop('user_id', None) #登出時一併消除儲存在cookies的資料
    return render_template("w_index.html")

#啟動網站伺服器，可透過 port 參數指定埠號
app.run(port=3000)
