from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    # This looks for index.html in your folder
    return render_template('index.html')

if __name__ == "__main__":
    # Render uses a specific port, this helps it find it
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
