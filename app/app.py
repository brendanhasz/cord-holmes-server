from flask import Flask, request
from holmes_manager import HolmesManager


app = Flask(__name__)

manager = HolmesManager(n_workers=4)


@app.route("/holmes_search", methods=["POST"])
def holmes_search():
    if request.method == "POST":
        return {
            'response': manager.search(
                request.form.to_dict()['query']
            )
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
