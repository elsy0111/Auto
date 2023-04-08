# Discription
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
