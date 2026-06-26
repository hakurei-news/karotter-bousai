import os
import requests

token = os.environ.get("KAROTTER_TOKEN")
url = "https://karotter.net/api/v1/statuses"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data = {
    "status": "【自動テスト】防災ボットの接続テストに成功しました！"
}

print("テスト投稿を送信中...")
response = requests.post(url, json=data, headers=headers)

if response.status_code in [200, 201]:
    print("投稿成功！")
else:
    print(f"エラーが発生しました: {response.status_code}")
    print(response.text)
