gunicorn:
	@cd services/app && gunicorn -b 0.0.0.0:5000 manage:app

install-youtube:
	@pip uninstall youtube -y
	@pip install /home/lyle/professional-projects/youtube-wrapper/dist/youtube-0.0.1-py3-none-any.whl

build-dev:
	@docker build -f ./services/app/Dockerfile -t youtube-video-stats-dev:latest ./services/app

run-dev:
	@docker run -p5000:5000 --env-file=./services/app/.env youtube-video-stats-dev:latest

build-prod:
	@docker build -f ./services/app/Dockerfile.prod -t youtube-video-stats-prod:latest ./services/app

run-prod:
	@docker run -p5000:5000 --env-file=./services/app/.env youtube-video-stats-prod:latest
