from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 05 - Client JS</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        input, button { padding: 8px 12px; margin-top: 10px; border-radius: 4px; border: 1px solid #3A86FF; background: #0B132B; color: #E0FBFC; }
        button { background: #3A86FF; cursor: pointer; font-weight: bold; }
        .flag { background: #0B132B; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🧠 The Client Knows Everything</h1>
        <p>This portal has a password-protected verification check implemented entirely in client-side JavaScript.</p>
        <input type="text" id="passInput" placeholder="Enter secret code...">
        <br>
        <button onclick="checkPass()">Verify</button>
        <div id="result"></div>
    </div>
    <script>
        // Secret validation logic is right here in the source!
        function checkPass() {
            const val = document.getElementById('passInput').value;
            const secretKey = "cyber_welcome_2026";
            if (val === secretKey) {
                document.getElementById('result').innerHTML = '<div class="flag">FLAG{CLIENT_SIDE_VALIDATION_IS_DEAD}</div>';
            } else {
                document.getElementById('result').innerText = 'Incorrect access code!';
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
