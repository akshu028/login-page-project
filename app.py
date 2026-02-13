from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

EMAIL = "user@test.com"
PASSWORD = "1234"

@app.route("/")
def login():
  return render_template("login.html")

@app.route("/login", methods=["POST"])
def handle_login():
  email = request.form.get("email")
  password = request.form.get("password")

  if email and password :
    return redirect(url_for("dashboard", user=email))
  else:
    return render_template("login.html",
error="Invalid email or password. Please try again.")

@app.route("/dashboard")
def dashboard():
  user = request.args.get("user")
  return render_template("dashboard.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)