from flask import Flask

# 创建一个应用对象
app = Flask(__name__)

@app.route("/login",method=["POST"])

