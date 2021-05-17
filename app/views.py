from flask import render_template, request , redirect, url_for
from app import app
#sayfalarımı viewsta oluşturuyorum

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "hello world!"


@app.route("/ogrenci")
def ogrenci():
    return render_template("ogrenci.html")


@app.route("/sonuc",methods=["POST"])
def sonuc():
    if request.method == "POST":
        isim = request.form["in_isim"]
        return render_template("sonuc.html", htmlisim = isim)


#url_for :
#redirectr :
#render_template :



