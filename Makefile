gunicorn:
	@cd services/app && gunicorn -b 0.0.0.0:5000 manage:app