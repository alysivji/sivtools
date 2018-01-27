# Repository or specific service
SERVICE =
IMAGE =
help:
	@echo 'Makefile for sivtools                                    '
	@echo '                                                         '
	@echo 'Usage:                                                   '
	@echo ' make test       runs tests                              '
	@echo ' make test_cov   runs test with coverage report          '
	@echo '                                                         '

test: ## Can pass in parameters using p=''
	pytest $(p)

test_cov:
	pytest --cov=sivtools

test_cov_html:
	pytest --cov=sivtools --cov-report=html
