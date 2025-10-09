install:
	python -m pip install --upgrade pip
	python -m pip install -r requirement.txt

test:
	python -m pytest -vv --cov=. test_app.py

format:
	python -m black TD1/ex1.py TD1/ex2.py TD1/ex3.py TD1/ex4.py TD1/ex5.py

lint:
	python -m pylint --disable=R,C TD1/ex1.py TD1/ex2.py TD1/ex3.py TD1/ex4.py TD1/ex5.py



all: install lint test format
