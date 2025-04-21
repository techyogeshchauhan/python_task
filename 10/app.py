from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Prime Number Checker</title>
</head>
<body style="font-family: Arial; padding: 40px;">
    <h1>Prime Number Checker</h1>
    <form method="post">
        <label for="number">Enter a number:</label>
        <input type="number" name="number" min="0" required>
        <button type="submit">Check</button>
    </form>

    {% if result is not none %}
        <h2>Result:</h2>
        <p>The number <strong>{{ number }}</strong> is 
        <strong>{{ "a prime number ✅" if result else "not a prime number ❌" }}</strong>.</p>
    {% endif %}
</body>
</html>
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route("/", methods=["GET", "POST"])
def prime_check():
    result = None
    number = None

    if request.method == "POST":
        try:
            number = int(request.form["number"])
            result = is_prime(number)
        except ValueError:
            result = False

    return render_template_string(HTML_TEMPLATE, result=result, number=number)

if __name__ == "__main__":
    app.run(debug=True)
