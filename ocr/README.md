docker build . -t ocr
docker run -it -v $(pwd)/:/home ocr name=ocr1
<!-- python3 app.py -->
python3 crop.py