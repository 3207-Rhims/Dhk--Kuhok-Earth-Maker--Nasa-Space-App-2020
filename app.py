from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/gallery")
def graph():
    return render_template("galary.html")

#banglades
@app.route("/bd")
def bd():
    return render_template("bd.html")
#Afganistan
@app.route("/Afganistan")
def Afganistan():
    return render_template("Afganistan.html")
#Argentina
@app.route("/Argentina")
def Argentina():
    return render_template("Argentian.html")
#Bahrain
@app.route("/Bahrain")
def Bahrain():
    return render_template("Bahrain.html")
#Brazil
@app.route("/Brazil")
def Brazil():
    return render_template("Brazil.html")
#china
@app.route("/china")
def CHina():
    return render_template("china.html")
#Egypt
@app.route("/Egypt")
def Egypt():
    return render_template("Egypt.html")
#France
@app.route("/France")
def gallery():
    return render_template("France.html")
#Ghana
@app.route("/Ghana")
def Ghana():
    return render_template("Ghana.html")
#Honduras
@app.route("/honduras")
def honduras():
    return render_template("Honduras.html")
#India
@app.route("/India")
def India():
    return render_template("India.html")
#Indonesia
@app.route("/ndonesia")
def korea():
    return render_template("Indonesia.html")
#Korea
@app.route("/Korea")
def Korea():
    return render_template("Korea.html")
#Nigeria
@app.route("/Nigeria")
def Nigeria():
    return render_template("Nigeria.html")
#Pakistan
@app.route("/Pakistan")
def Pakistan():
    return render_template("Pakistan.html")
#Philipines
@app.route("/Philipines")
def Philipines():
    return render_template("Philipines.html")
#Russia
@app.route("/Russia")
def Russia():
    return render_template("Russia.html")
#Spain
@app.route("/Spain")
def Spain():
    return render_template("Spain.html")
#Srilanka
@app.route("/Srilanka")
def Srilanka():
    return render_template("Srilanka.html")
#Turkey
@app.route("/Turkey")
def Turkey():
    return render_template("Turkey.html")
#UAE
@app.route("/UAE")
def UAE():
    return render_template("UAE.html")
#Uganda
@app.route("/Uganda")
def Uganda():
    return render_template("Uganda.html")
#UK
@app.route("/UK")
def UK():
    return render_template("Uk.html")
#Ukrain
@app.route("/Ukrain")
def Ukrain():
    return render_template("Ukrain.html")
#USA
@app.route("/USA")
def USA():
    return render_template("USA.html")
#Vietnam
@app.route("/Vietnam")
def Vietnam():
    return render_template("Vietnam.html")


