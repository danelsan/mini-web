all: build

build:
	docker build -t mini-web .

run:
	docker run --rm -d -p 8089:80 --name miniweb mini-web

stop:
	docker rm miniweb -f

