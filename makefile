##############################################################################################
# Variables
##############################################################################################

current_dir := $(realpath .)
APP_PATH = ${current_dir}/app/src/main.py
BUILD_TEST_PATH = ${current_dir}/app/tests/build.py

##############################################################################################
# Jupyter Commands
##############################################################################################

.PHONY: local-jupyter
local-jupyter: ## Create pyvenv
	@echo Local Jupyter...
	@jupyter nbconvert --to notebook --execute notebooks/reports.ipynb --output output/reports.ipynb
	@echo.

##############################################################################################
# Python Commands
##############################################################################################

.PHONY: create-venv 
create-venv: ## Create pyvenv
	@echo Builiding Python Virtual Environment...
	@python -m venv app\venv
	@echo.