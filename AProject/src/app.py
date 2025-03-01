from flask import Flask, render_template, current_app, request
import os
from flask_dotenv import DotEnv
from dotenv import load_dotenv
from model.db import get_db_connection

environment = os.getenv("Flask_Env", "development")
app = Flask(__name__)
if environment == "development":
	load_dotenv(".env.dev")
	env = DotEnv()
	env.init_app(app, env_file = ".env.dev", verbose_mode = True)
else:
	load_dotenv(".env.prod")
	env = DotEnv()
	env.init_app(app, env_file = ".env.prod", verbose_mode = True)




@app.route("/")
@app.route("/index")
def index():
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM users")
	users = cursor.fetchall()
	conn.close()
	return render_template("index.html", users=users)

@app.post("/translate")
def translate():
	text = request.form["text"]
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM translations WHERE text = ?", (text,))
	translations = cursor.fetchall()
	conn.close()
	return render_template("translate.html", text=text, translations=translations)

if __name__ == '__main__':
	app.run( "0.0.0.0", debug=True)
