from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def top():
    return "郵便番号(半角数字7桁)をもとに住所を検索します。ハイフンなしで入力してください。"

def main():
    app.run(debug=True)

@app.route("/address_search_app")
def address_search_app():
    zcode = request.args.get("zipcode")

    return f"住所検索 {zcode=}"

if __name__ == '__main__':
    main()