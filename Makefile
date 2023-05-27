gunicorn:
	@cd services/app && gunicorn -b 0.0.0.0:5000 manage:app

install-youtube:
	@pip uninstall youtube -y
	@pip install /home/lyle/professional-projects/youtube-wrapper/dist/youtube-0.0.1-py3-none-any.whl