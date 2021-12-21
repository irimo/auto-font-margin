docker build . -t machinelearning
docker run -it -v $(pwd)/:/home machinelearning
python3 reco.py