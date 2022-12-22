docker build . -t ocr
docker run --name ocr1 -it -v $(pwd)/:/home ocr
# docker run --name ocr2 -it -v $(pwd)/:/home padding


<!-- response = requests.get('https://i.stack.imgur.com/J2ojU.png') 
img = Image.open(io.BytesIO(response.content))
text = pytesseract.image_to_string(img, lang='eng', config='--psm 7') -->
