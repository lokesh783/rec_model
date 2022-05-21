# from urllib import request
from flask import Flask , render_template , request
import val

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", m='h')

@app.route("/recommend" , methods = ['POST','GET'])
def rec():
    if request.method =='GET':
        return render_template('index.html')
    # HTML -> .py
    if request.method== "POST":
        name = request.form["moviename"]
        recommend_movies = val.recommend(name)
        
    #  .py -> HTML
    return render_template("sub.html" , n =recommend_movies )

if __name__ == "__main__":
    app.run(debug=True)
    