import base64
import os
import uuid
from os import getenv

import boto3
from botocore.exceptions import NoCredentialsError, ClientError, ValidationError
from botocore.config import Config

BUCKET_NAME = getenv('S3_BUCKET_NAME', 'weddpics')
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"
ACCESS_KEY = getenv('S3_ACCESS_KEY', None)
SECRET_ACCESS_KEY = getenv('S3_SECRET_ACCESS_KEY', None)


def s3_client():
    return boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY,
                        config=Config(signature_version='s3v4'))


def s3_upload_file(photo):
    client = s3_client()
    body = photo.stream.read()
    try:
        response = client.put_object(Key=f"{photo.filename}", Body=body, Bucket=BUCKET_NAME,
                          ContentType=photo.mimetype, ACL='public-read')

        print(f"S3 - RESPONSE {response}")
        photo_url = f"{S3_LOCATION}{photo.filename}"
    except (NoCredentialsError, ClientError) as e:
        raise ValidationError(f"It is not possible to add this photo. {e}")

    return photo_url
