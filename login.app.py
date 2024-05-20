from flask import Flask, render_template, request

app = Flask(__name__)

# Route for login page (GET request to display the form)
@app.route("/login")
def login():
  return render_template("login.html")

# Route for handling login form submission (POST request)
@app.route("/login", methods=["POST"])
def handle_login():
  username = request.form.get("username")
  password = request.form.get("password")

  # Implement login logic here (e.g., authenticate against a database)
  # This is a placeholder for now, assuming successful login
  if username == "admin" and password == "secret":
    return "Login successful!"
  else:
    return "Invalid username or password. Please try again."

if __name__ == "__main__":
  app.run(debug=True)
