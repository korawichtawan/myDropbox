import json
import boto3
import os


bucket_name = ''#add bucket name here
s3 = boto3.resource('s3')
client = boto3.client('s3')
def lambda_handler(event, context):
    # TODO implement
    inputt = (event["queryStringParameters"])
    option = inputt["command"]
    if(option=="view"):
        #bucket = s3.Bucket(bucket_name)
        result = []
        for obj in s3.Bucket(bucket_name).objects.all():
            key = obj.key
            size = str(obj.size)
            last_modified = str(obj.last_modified)
            result.append({'key':key,'size':size,'last_modified':last_modified})
    if(option == "get"):
        key_input = inputt["Key"]
        try:
            response = client.get_object(Bucket=bucket_name, Key=key_input)
            result = str((response['Body']).read())
        except:
            result = "cant find this file"
    if(option=="put"):
        key_input = inputt["Key"]
        body_input = inputt["Body"]
        client.put_object(Bucket=bucket_name,Key=key_input, Body=body_input)
        result = "OK"
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
    
