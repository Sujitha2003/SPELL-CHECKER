from flask import Flask,render_template,request
from textblob import TextBlob
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/page/<page1>")
def page(page1):
    return render_template("index.html")


@app.route('/correct', methods=['POST'])
def correct():
    if request.method == 'POST':
        input = request.form['input']
        text = TextBlob(input)
    return render_template('index.html', input=text, output=text.correct())

   

if  __name__=="__main__":
    app.run(debug=True)