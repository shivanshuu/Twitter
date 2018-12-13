aws cloudformation create-stack \
--stack-name "ES-KINESIS" \
--capabilities "CAPABILITY_NAMED_IAM" \
--region "us-east-1" \
--template-body file://es_kinesis.json \
--parameters file://template.parameters.json
~                                                  
