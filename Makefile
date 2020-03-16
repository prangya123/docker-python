all : test docs
.PHONY : all
test:
	@echo "Hello AppleTeam"

docs:
	@echo "Author:Prangya Parmita Kar"
	@echo "This is to build TextWrap in python3 ubuntu  image"
	@echo "make clean:  To clean all images and containers"
	@echo "make build:  To build ubuntu python3 image and copy textwrap.py and it creates the docker image"
	@echo "make run:  To run the TextWrap for given Paragraph and Page_Width"
	@echo "Sample input:"
	@echo "Paragraph = \"This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.\""
	@echo "Page Width = 20 "


build:
	@echo "Creating docker build"
	docker images
	docker build -t prangya-text-wrap:1.0 . -f Dockerfile --no-cache


run:
	@echo "Creating docker container"
	docker ps -a
	docker run -it --name prangya-text-wrap prangya-text-wrap:1.0

clean:
	@echo "Cleaning docker images and process"
	@echo "Cleaning docker images"
	docker rmi -f $$(docker images -q) || true
	@echo "Cleaning docker running processes"
	docker rm -f $$(docker ps -a -q) || true
