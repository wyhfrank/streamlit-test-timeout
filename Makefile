up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker build -t wyhfrank/streamlit-test-timeout:latest .

push:
	docker push wyhfrank/streamlit-test-timeout:latest