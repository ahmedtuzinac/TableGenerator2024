PYTHONPATH=src:. pytest --cov-report=html src/tests/ && open -a "Google Chrome" htmlcov/index.html
