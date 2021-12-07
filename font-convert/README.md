docker build . -t font-convert
docker run -it -p 8080:80 -v $(pwd)/:/var/www/html font-convert
