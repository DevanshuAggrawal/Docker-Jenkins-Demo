from flask import Flask

PORT = 8000
MESSAGE = "Congrats Devanshu!! Your 1st project got completed \n This is the new build done on 23rd May 2021"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
