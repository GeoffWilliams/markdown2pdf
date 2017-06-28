clean:
	pip install isort autopep8 flake8 --upgrade
	isort -rc markdown2pdf/
	autopep8 --in-place --recursive --aggressive markdown2pdf/
	flake8 markdown2pdf/
