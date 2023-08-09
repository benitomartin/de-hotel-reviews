install:
	pip install -r requirements.txt

pylint:
	pylint --verbose --recursive=y .