import boto3
import botocore

from flask import current_app


s3 = boto3.client("s3",
                  aws_access_key_id=current_app.config['S3_KEY'],
                  aws_secret_access_key=current_app.config['S3_SECRET'])


def upload_file_to_s3(file, bucket_name, acl="public-read"):

    try:
        s3.upload_fileobj(file, bucket_name, file.name, ExtraArgs={"ACL": acl, "ContentType": file.content_type})
    except Exception as e:
        print(f"Problems trying to upload {file.name} : {e}")
        return e

    return f"{current_app.config['S3_LOCATION']}{file.name}"
