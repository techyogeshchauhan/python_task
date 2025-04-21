from flask import Flask, request, render_template_string
import math

app = Flask(__name__)

# HTML template with embedded placeholders
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Factorial Calculator</title>
</head>
<body style="font-family: Arial; padding: 40px;">
    <h1>Factorial Calculator</h1>
    <form method="post">
        <label for="number">Enter a non-negative integer:</label>
        <input type="number" name="number" min="0" required>
        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h2>Result:</h2>
        <p>Factorial of {{ number }} is <strong>{{ result }}</strong></p>
    {% elif error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def factorial():
    result = None
    error = None
    number = None

    if request.method == "POST":
        try:
            number = int(request.form["number"])
            if number < 0:
                error = "Please enter a non-negative integer."
            else:
                result = math.factorial(number)
        except ValueError:
            error = "Invalid input. Please enter a valid number."

    return render_template_string(HTML_TEMPLATE, result=result, error=error, number=number)

if __name__ == "__main__":
    app.run(debug=True)
