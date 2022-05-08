docker build . -t ml
docker run -it -v $(pwd)/:/home ml
python3 reco.py