from flask import Flask #仔入 Flask
from flask import request #載入 Request 物件
from flask import redirect #載入 Redirect 函式
from flask import render_template #載入 render_template 函式
app = Flask( __name__,static_folder="static", static_url_path="/static") 
# 所有在 static 資料夾底下的檔案，都對應到網址路徑 /static/檔案名稱

#建立路徑/ 對應的處理函式
# 處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("w_index.html")

@app.route("/signin", methods=["POST"])
def signin():
    userId=request.form["id"]
    userPw=request.form["pw"]
    if userId == "test":
        if userPw == "test":
            return redirect("/member/")
        else:
            return redirect("/error/")
    else:
        return redirect("/error/")

@app.route("/member/")
def success():
    return render_template("w_success.html")

@app.route("/error/")
def fail():
    return render_template("w_fail.html")
#啟動網站伺服器，可透過 port 參數指定埠號
app.run(port=3000)