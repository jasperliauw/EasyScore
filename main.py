from flask import Flask, render_template

app = Flask(__name__, static_folder="CSSFiles", template_folder="HTMLFiles")

print("Remember to flush chrome sockets!")


@app.route("/")
def Index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
