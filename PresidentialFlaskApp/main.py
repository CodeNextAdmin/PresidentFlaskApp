from flask import Flask, render_template

app = Flask(__name__)

# Dictionary with presidents and their information
presidents = {
  "George Washington": {
    "name": "George Washington",
    "order": 1,
    "image_url": "https://simple.wikipedia.org/wiki/George_Washington"
  },
  "Abraham Lincoln": {
    "name": "Abraham Lincoln",
    "order": 2,
    "image_url": "https://simple.wikipedia.org/wiki/Abraham_Lincoln"
  },
  "Theodore Roosevelt": {
    "name": "Theodore Roosevelt",
    "order": 3,
    "image_url": "https://en.wikipedia.org/wiki/Theodore_Roosevelt"
  },
}

@app.route('/')
def presidents_info():
  return render_template('presidents.html', presidents=presidents)

if __name__ == '__main__':
  app.run(debug=True)