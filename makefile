build:
	pyinstaller --clean -y -n="pysweeper" --onefile --add-data="img/*:img" --add-data="font.ttf:." main.py
run:
	python main.py
run-build: build
	dist/pysweeper
clean:
	rm -rf build dist __pycache__ py_bin.spec
