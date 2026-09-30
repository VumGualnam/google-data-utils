.PHONY: help tree clean install test build publish-test publish

help:
	@echo "Available targets:"
	@echo "  tree          Show project structure"
	@echo "  install       Install package in editable mode"
	@echo "  test          Run tests"
	@echo "  build         Build package"
	@echo "  publish-test  Upload to TestPyPI"
	@echo "  publish       Upload to PyPI"
	@echo "  clean         Remove build artifacts"

tree:
	tree -I '__pycache__|.git|.pytest_cache|build|dist|*.egg-info'

install-dev:
	pip install -e ".[dev]"

install:
	pip install -e .

test:
	pytest -v

build:
	python -m build

publish-test:
	twine upload --repository testpypi dist/*

publish:
	twine upload dist/*

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete