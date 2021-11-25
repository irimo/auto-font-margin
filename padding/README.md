# GD の入った docker image
cd docker/padding
docker build . -t padding


docker run -it -p 4999:5000 -v $(pwd)/:/home padding
<!-- python3 app.py -->

localhost:4999