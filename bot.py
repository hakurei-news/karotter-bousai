import os
import requests
u = "https://api.p2pquake.net/v2/jma/quake?limit=1"
try:
    r = requests.get(u).json()
except:
    r = []
if r:
    l = r[0]
    if l.get('issue', {}).get('type') == 'ScalePrompt':
        h = l['earthquake']['hypocenter']['name']
        m = l['earthquake']['maxScale']
        s_map = {10:"1", 20:"2", 30:"3", 40:"4", 45:"5弱", 46:"5強", 50:"6弱", 55:"6強", 60:"7"}
        d = s_map.get(m, "不明")
        txt = f"【地震速報】震源地：{h} / 最大震度：{d}"
        tk = os.environ.get("KAROTTER_TOKEN")
        k_url = "https://karotter.com/api/v1/posts"
        hd = {"Authorization": f"Bearer {tk}"}
        pl = {"content": txt}
        try:
            requests.post(k_url, json=pl, headers=hd)
        except:
            pass
