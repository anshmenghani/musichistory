from flask import Flask, render_template

app = Flask(__name__, template_folder=r"C:\Users\RamKrishna\PycharmProjects\BandProject")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/interactive")
def interactive():
    return render_template("interactive.html")


@app.route("/video")
def mlesson():
    return render_template("video.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/pre-baroque")
def pbaroque():
    return render_template("pre_baroque/pre-baroque.html")


@app.route("/pre-baroque-wh")
def pbaroquewh():
    return render_template("pre_baroque/pre-baroque-wh.html")


@app.route("/pre-baroque-music")
def pbaroquemusic():
    return render_template("pre_baroque/pre-baroque-music.html")


@app.route("/pre-baroque-composers")
def pbaroquecomposers():
    return render_template("pre_baroque/pre-baroque-composers.html")


@app.route("/pre-baroque-pieces")
def pbaroquepieces():
    return render_template("pre_baroque/pre-baroque-pieces.html")


@app.route("/baroque")
def baroque():
    return render_template("baroque/baroque.html")


@app.route("/baroque-wh")
def baroquewh():
    return render_template("baroque/baroque-wh.html")


@app.route("/baroque-music")
def baroquemusic():
    return render_template("baroque/baroque-music.html")


@app.route("/baroque-composers")
def baroquecomposers():
    return render_template("baroque/baroque-composers.html")


@app.route("/baroque-pieces")
def baroquepieces():
    return render_template("baroque/baroque-pieces.html")


@app.route("/classical")
def classical():
    return render_template("classical/classical.html")


@app.route("/classical-wh")
def classicalwh():
    return render_template("classical/classical-wh.html")


@app.route("/classical-music")
def classicalmusic():
    return render_template("classical/classical-music.html")


@app.route("/classical-composers")
def classicalcomposers():
    return render_template("classical/classical-composers.html")


@app.route("/classical-pieces")
def classicalpieces():
    return render_template("classical/classical-pieces.html")


@app.route("/romantic")
def romantic():
    return render_template("romantic/romantic.html")


@app.route("/romantic-wh")
def romanticwh():
    return render_template("romantic/romantic-wh.html")


@app.route("/romantic-music")
def romanticmusic():
    return render_template("romantic/romantic-music.html")


@app.route("/romantic-composers")
def romanticcomposers():
    return render_template("romantic/romantic-composers.html")


@app.route("/romantic-pieces")
def romanticpieces():
    return render_template("romantic/romantic-pieces.html")


@app.route("/contemporary")
def contemporary():
    return render_template("contemporary/contemporary.html")


@app.route("/contemporary-wh")
def contemporarywh():
    return render_template("contemporary/contemporary-wh.html")


@app.route("/contemporary-music")
def contemporarymusic():
    return render_template("contemporary/contemporary-music.html")


@app.route("/contemporary-composers")
def contemporarycomposers():
    return render_template("contemporary/contemporary-composers.html")


@app.route("/contemporary-pieces")
def contemporarypieces():
    return render_template("contemporary/contemporary-pieces.html")


if __name__ == "__main__":
    app.run(debug=True)
