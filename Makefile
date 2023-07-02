.PHONY: init unit_test regression

init:
	pip3 install --user -r requirements.txt

unit_test:
	pytest -v --color=yes -n 16 \
	--cov=vlsi_flow --cov-report term-missing --cov-report html:run/conv_html \
	tests/unit_tests

regression:
	pytest -v --color=yes -n 16 \
	--cov=vlsi_flow --cov-report term-missing --cov-report html:run/conv_html \
	tests/regression_tests
