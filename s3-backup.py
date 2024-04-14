import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    # Name of the source S3 bucket
    source_bucket_name = 'testlog321'
    
    # Name of the destination S3 bucket
    destination_bucket_name = 'backupfolder2'

    # Connect to AWS S3
    s3_client = boto3.client('s3')
    
    # Get list of objects in the source bucket
    response = s3_client.list_objects_v2(Bucket=source_bucket_name)
    
    # Create backup folder if it doesn't exist
    backup_folder = 'backup_' + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Backup each object in the source bucket to the destination bucket
    for obj in response.get('Contents', []):
        key = obj['Key']
        print(f"Backing up {key}...")
        dest_key = os.path.join(backup_folder, key)
        copy_source = {'Bucket': source_bucket_name, 'Key': key}
        s3_client.copy_object(CopySource=copy_source, Bucket=destination_bucket_name, Key=dest_key)

    print("Backup completed successfully!")

    return {
        'statusCode': 200,
        'body': 'Backup completed successfully!'
    }
