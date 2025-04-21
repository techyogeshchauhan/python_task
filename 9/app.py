from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Email Validator</title>
</head>
<body style="font-family: Arial; padding: 40px;">
    <h1>Email Validator</h1>
    <form method="post">
        <label for="email">Enter your email:</label>
        <input type="email" name="email" required>
        <button type="submit">Validate</button>
    </form>

    {% if result is not none %}
        <h2>Result:</h2>
        <p>The email <strong>"{{ email }}"</strong> is 
        <strong>{{ "valid ✅" if result else "invalid ❌" }}</strong>.</p>
    {% endif %}
</body>
</html>
"""

# Regular expression pattern for validating emails
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route("/", methods=["GET", "POST"])
def validate_email():
    result = None
    email = ""

    if request.method == "POST":
        email = request.form["email"]
        result = re.match(EMAIL_REGEX, email) is not None

    return render_template_string(HTML_TEMPLATE, result=result, email=email)

if __name__ == "__main__":
    app.run(debug=True)
