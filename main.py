import requests
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

    # 郵便番号をもとに住所情報を取得
    url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode=" + zcode
    res = requests.get(url)
    resinfo = res.json()

    # 住所を抽出し値を戻す
    for info in resinfo["results"]:
        address = info["address1"] + info["address2"] + info["address3"]

    return f"{address}"

if __name__ == '__main__':
    main()