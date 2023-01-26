import boto3
#from opensearchpy import OpenSearch

def load_data(event):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    print("CONTENT TYPE: " + obj['ContentType'])
