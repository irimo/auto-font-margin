docker build . -t machinelearning
docker run -it -v $(pwd)/:/home machinelearning
python3 ./ml/recognize.py