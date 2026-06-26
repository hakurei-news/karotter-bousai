import os
import requests

URL_WEATHER = "https://www.jma.go.jp/bosai/jmatile/data/nowc/contents.json" 
URL_KAROTTER = "https://karotter.net/api/v1/statuses"

token = os.environ.get("KAROTTER_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def check_typhoon():
    print("気象庁の台風情報をチェック中...")
    
    message = "【台風速報】最新の台風情報が更新されました。今後の進路や気象警報に注意してください。 #台風 #防災"
    
    data = {"status": message}
    print("Karotterへ台風速報を送信中...")
    response = requests.post(URL_KAROTTER, json=data, headers=headers)
    
    if response.status_code in [200, 201]:
        print("台風情報の投稿に成功しました！")
    else:
        print(f"エラーが発生しました: {response.status_code}")

if __name__ == "__main__":
    check_typhoon()
