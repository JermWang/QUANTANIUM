.PHONY: build run clean

build:
	docker build -t quantanium .

run:
	docker run --rm -p 8000:8000 quantanium

clean:
	docker rmi quantanium