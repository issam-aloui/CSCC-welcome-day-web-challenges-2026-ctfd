from flask import Flask, render_template_string, Response

app = Flask(__name__)

INDEX = """
<!DOCTYPE html>
<html>
<head>
    <title>CSCC Challenge 02 - Robots Don't Lie</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        a { color: #4EA8DE; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🤖 Robots Don't Lie</h1>
        <p>We are building a secure member directory for the club.</p>
        <p>We don't want search engines crawling our administrative areas. How do websites tell web crawlers where not to go?</p>
        <p><a href="/robots.txt" target="_blank">Check our configuration</a></p>
    </div>
</body>
</html>
"""

SECRET = """
<!DOCTYPE html>
<html>
<head>
    <title>Secret Area</title>
    <style>
        body { font-family: sans-serif; background: #0B132B; color: #E0FBFC; padding: 40px; }
        .card { background: #1C2541; padding: 30px; border-radius: 8px; border: 1px solid #3A86FF; max-width: 600px; margin: auto; }
        h1 { color: #4EA8DE; }
        .flag { background: #0B132B; padding: 10px; border: 1px dashed #3A86FF; font-family: monospace; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔒 Restricted Admin Directory</h1>
        <p>You found the hidden administrative path!</p>
        <div class="flag">FLAG{ROBOTS_DONT_PROTECT_SECRETS}</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(INDEX)

@app.route('/robots.txt')
def robots():
    return Response("User-agent: *\nDisallow: /secret-admin-area/\n", mimetype="text/plain")

@app.route('/secret-admin-area/')
def secret():
    return render_template_string(SECRET)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
