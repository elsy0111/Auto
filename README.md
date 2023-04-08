## 前提
Chrome Driver がインストールされていること（chromedriver.exe に path が通っていること)
selenuim がインストールされていること (pip install selenium とかで入れよう)

# Run
0.port.bat を編集  

```bat:port.bat
"C:\Program Files\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9222 --user-data-dir="C:\Users\kpp01\"
```

最初の = chrome.exe の path  
--user-data-dir = chrome のデータを保存する場所(たぶんどこでもいいのでUser直下とかでいいんじゃないかな)  

1.port.bat を実行(エクスプローラー上でダブルクリックとか)  
2.1で出たchrome上で以下(*1)のURLにアクセスしログイン(cmd.exeは閉じていい)  
3.問題が表示されてるページまで移動(*2)  
4.2つディレクトリが見えるところで開く  

![スクリーンショット 2023-04-08 101613](https://user-images.githubusercontent.com/76511273/230697148-d20f43a9-cccf-4feb-9735-6cdd558301f1.png)

5.main.py の line20当たりのrangeを好きなUnitにする  
6.実行  


(*1)https://nanext.alcnanext.jp/anetn/Student/stlogin/index/nit-ariake/  
(*2)https://nanext.alcnanext.jp/anetn/Student/StUnitList  

# 詳細
## port.bat
ポートを指定してselenium を実行することで既に開いている chrome の操作が可能になる。  
その為、main.py でも

```bat:port.bat
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
```

というように port.bat で指定した port : 9222 を開くようにしてある。

## main.py
### 選択アルゴリズム
日本語と英語をあらかじめ スクレイピング で取得しておいて、問題を取得し、それに対応する英単語、もしくは日本語を選択する。  
各Unit ごとに 双方向の辞書型を持っておく。

## 操作
基本は x_path による操作。
大体要素の x_path は決まってあるが一度手を付けて、「途中からやりますか？」的なことを言われる状態の時は、要素が1つずれたりする。  

```py:port.py
try:
    # 処理
    ok_xpath = '/html/body/div[12]/div[3]/div/button/span'
    is_filled_xpath = '//*[@id="ui-id-6"]/div[3]/div/ul/li[20]'
except:
    ok_xpath = '/html/body/div[13]/div[3]/div/button/span'
    is_filled_xpath = '//*[@id="ui-id-5"]/div[3]/div/ul/li[20]'
```

drill 1,2,4 は与えられた問題 key に対応する value を答える。  
特に drill 2 はその答えを selenium で入力しているだけである。
