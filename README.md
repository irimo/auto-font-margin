# font auto margin

* フォントファイルのマージンを自動で調整してくれるものです。
* ざっくりとしたフォントファイルから、そこそこいい感じのマージンにしてくれるくらいのレベルを目指しています。
* 微調整は必要ですが、なんちゃってフォントならこれだけでいいと思います。


## memo

```
docker build . -t web-app
docker run -it -p 5000:5000 -v $(pwd)/:/home web-app
python3 app.py

docker build . -t font-convert
docker run -it -p 8080:80 -v $(pwd)/:/var/www/html font-convert
```
