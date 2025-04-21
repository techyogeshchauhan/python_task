from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Palindrome Checker</title>
</head>
<body style="font-family: Arial; padding: 40px;">
    <h1>Palindrome Checker</h1>
    <form method="post">
        <label for="text">Enter a string:</label>
        <input type="text" name="text" required>
        <button type="submit">Check</button>
    </form>

    {% if result is not none %}
        <h2>Result:</h2>
        <p>"{{ text }}" is 
            <strong>{{ "a palindrome" if result else "not a palindrome" }}</strong>.
        </p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def check_palindrome():
    result = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        cleaned = ''.join(c.lower() for c in text if c.isalnum())  # remove non-alphanumeric chars
        result = cleaned == cleaned[::-1]

    return render_template_string(HTML_TEMPLATE, result=result, text=text)

if __name__ == "__main__":
    app.run(debug=True)
