.PHONY: clean clean-pyc clean-checkpoint

clean: clean-pyc clean-checkpoint


clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-checkpoint:
	find . -name '.ipynb_checkpoints' -exec rm -rf {} +
