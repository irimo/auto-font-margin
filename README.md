# font auto margin

* フォントファイルのマージンを自動で調整してくれるものです。
* ざっくりとしたフォントファイルから、そこそこいい感じのマージンにしてくれるくらいのレベルを目指しています。
* 微調整は必要ですが、なんちゃってフォントならこれだけでいいと思います。


## memo

'''
via https://hackmd.io/@T7k0V7TMQFelvJKKdo3pww/ryBaiO2uU
docker build . -t web-app
docker run -it -p 5000:5000 -v $(pwd)/:/home web-app python3 app.py
'''