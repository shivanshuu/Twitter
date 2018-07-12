import boto3
import json

translate = boto3.client(service_name='translate', region_name='us-east-1')
text = "Ulta Beauty is looking for talented professionals to join our amazing team! We are hiring in #Tucson, AZ. "
result = translate.translate_text(Text=text, 
            SourceLanguageCode="en", TargetLanguageCode="de")
print('TranslatedText: ' + result.get('TranslatedText'))
print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
