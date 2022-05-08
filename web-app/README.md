docker build . -t web-app
docker run -it -p 5000:5000 -v $(pwd)/:/home web-app
<!-- python3 app.py -->
python3 crop.py