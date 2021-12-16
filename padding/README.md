cd docker/padding
docker build . -t padding


docker run -it --name padding1 -p 4999:80 -v $(pwd)/:/home padding
python3 pad.py