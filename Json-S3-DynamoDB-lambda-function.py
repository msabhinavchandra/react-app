# lambda_function.py

import boto3
import json

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    
    json_object = s3_client.get_object(Bucket=bucket, Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    
    table = dynamodb.Table('teachers') #write the name of your table, in the dynamoDB here in this case it is teachers
    table.put_item(Item=jsonDict) # and make sure that the primary key is the same as the one in the json file

# make sure whatever your uploading into the S3 bucket the Json file,which contains the json objects
#has this primary key there inside each and every JSON object.
    
