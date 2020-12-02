from flask import Flask

app = Flask(__name__)


@app.route("/")
def top():
    return "郵便番号(半角数字7桁)をもとに住所を検索します。ハイフンなしで入力してください。"

def main():
    app.run(debug=True)

@app.route("/address_search_app/<string:zcode>")
def address_search_app(zcode:str):
    return

if __name__ == '__main__':
    main()