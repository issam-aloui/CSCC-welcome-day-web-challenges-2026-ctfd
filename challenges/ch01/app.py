from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 01 - Look Closer</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
    </style>
</head>
<body>
    <div class="card">
        <h1>👀 Look Closer</h1>
        <p>Welcome to the University Cybersecurity Club portal!</p>
        <p>The developer was working on this site and left some notes behind in the source code.</p>
        <p>Can you find what was left behind?</p>
        <!-- FLAG{VIEW_SOURCE_IS_POWER} -->
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
