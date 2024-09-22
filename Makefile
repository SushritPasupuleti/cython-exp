test:
	@python3 test.py

clean:
	@echo "Cleaning up..."
	@rm -rf __pycache__
	@rm main.c
	@rm -rf build
	@echo "Cleaned up"

build: clean
	@python3 setup.py build_ext --inplace
