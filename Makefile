# Repository or specific service
SERVICE =
IMAGE =
help:
	@echo 'Makefile for sivtools                                    '
	@echo '                                                         '
	@echo 'Usage:                                                   '
	@echo ' make bandit     runs bandit for security                '
	@echo ' make test       runs tests                              '
	@echo ' make test_cov   runs test with coverage report          '
	@echo '                                                         '

bandit:
	bandit -r sivtools

test: ## Can pass in parameters using p=''
	pytest $(p)

test_all:
	detox

test_cov:
	pytest --cov=sivtools

test_cov_view:
	pytest --cov=sivtools --cov-report=html && open ./htmlcov/index.html
