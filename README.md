# Twitter Data Analysis

1) Create an EC2 instance with Role to access Kinesis Firehose, Comprehend, Translate APIs
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html

2) Create an Amazon ElasticSerach Domain
https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-gsg-create-domain.html
Create an Amazon Kinesis Firehose to push data to ES Domain
https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html
or
Go to CloudFormation Directory and use the teamplate to create Elasticsearch domain and Kinesis Firehose

3) Create Twitter account and get access keys

4) Download this git repository to EC2, put Twitter keys in accessConfig.py, install dependencies using setup.sh

5) Merge getBatchData.py , translate.py, comprehend.py to get Twitter data in all languages for hiring and other keywords, 
identify organization tweets and send to Kinesis Firehose

6) View Data in Kibana on Amazon ES and create graphs like top hiring loctions

