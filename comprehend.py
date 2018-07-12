import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = "Ulta Beauty is looking for talented professionals to join our amazing team! We are hiring in #Tucson, AZ. "

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text = text, LanguageCode = "en"), sort_keys=True, indent=4))
