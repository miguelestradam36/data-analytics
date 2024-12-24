##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
APP_PATH = ${current_dir}/main.py
BUILD_TEST_PATH = ${current_dir}/app/tests/build.py

##############################################################################################
# Commands
##############################################################################################

.PHONY: pytest-tests
pytest-tests: ## Create pyvenv
	@echo Running python main code...
	@python -m pytest tests/
	@echo Finished running the tests...

.PHONY: create-venv 
create-venv: ## Create pyvenv
	@echo Builiding Python Virtual Environment...
	@python -m venv app\venv
	@echo.