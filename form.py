from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html>
  <body>
    <h2>Submit a Message</h2>
    <form method="POST" action="/submit">
      Name: <input type="text" name="name"><br><br>
      Message: <input type="email" name="message"><br><br>
      <input type="submit" value="Submit">
    </form>
    <p>See all messages at <a href="/messages">/messages</a></p>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(form_html)

@app.route("/submit", methods=["POST"])
def submit():
    # TODO: Get form data from request.form
    name = request.form.get("name")
    message = request.form.get("message")
    # TODO: Save it to a file (append mode - make sure you are appending to the file, not overwriting the whole thing)
    with open("messages.txt", "a") as file:
        file.write(f"Name: {name}, Message: {message}")
        
    return redirect("/messages")

@app.route("/messages", methods=["GET"])
def messages():
    # TODO: Read file content and return as plain text or HTML
    with open("messages.txt", "r") as file:
      file.read()
    return "All submitted messages go here"

if __name__ == "__main__":
    app.run(debug=True)
