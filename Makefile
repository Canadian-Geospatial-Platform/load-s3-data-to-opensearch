lint:
	pylint --rcfile=.pylintrc load_s3_data_to_opensearch.py

test:
	pytest --cov=load_s3_data_to_opensearch --cov-fail-under=80

coverage:
	coverage html
	coverage report

deploy:
	aws cloudformation package --template-file template.yaml --s3-bucket my-lambda-code-bucket --output-template-file output-template.yaml
	aws cloudformation deploy --template-file output-template.yaml --stack-name load-s3-data-to-opensearch
