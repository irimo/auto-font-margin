# font auto margin

* フォントファイルのマージンを自動で調整してくれるものです。
* ざっくりとしたフォントファイルから、そこそこいい感じのマージンにしてくれるくらいのレベルを目指しています。
* 微調整は必要ですが、なんちゃってフォントならこれだけでいいと思います。

# フォント作成手順

## 切り抜き（ペイントソフトでもOK）
```
docker buildx build --platform linux/amd64 . -t web-app
docker run --rm -it -p 5000:5000 -v $(pwd)/:/home web-app
python3 crop.py
```
1. /docker/web-app を docker build
1. /web-app をマウントしてdocker run
1. localhost:5000 は多分特定の大きさの切り抜きができるので文字を切り抜いていく

## フォント化
```
docker build . -t font-convert
docker run -it -p 8080:80 -v $(pwd)/:/var/www/html font-convert
```
1. /docker/font-convert を docker build
1. /font-convert/index.html （静的ですみません。。）を、ひらがなの文字コードを調べて修正する
1. /font-convert をマウントして docker run
1. /font-convert をブラウザで開いて、GUIｗで文字の画像をあてはめていく
1. ttf （TrueTypeFont）ファイルできます

## 微調整
1. FontForge を無料ダウンロード
1. 余白や位置を修正
1. ファイル名、作者名を修正（ファイル内容がかぶらないように、修正された方のお名前をいれていただきたいのと、バージョンを公開版ごとに修正していってください）