import shutil
import uuid

from boto3 import session

ACCESS_ID = 'S5GYFWHITJSKHGJXVOT3'
SECRET_KEY = 'WBCwtwVPQ3bK5KVz/gZF+rgLxdkG0nRJ/S2v5tlbLc0'


def upload_image(path):
    # Initiate session
    sess = session.Session()
    client = sess.client('s3',
                         region_name='nyc3',
                         endpoint_url='https://nyc3.digitaloceanspaces.com',
                         aws_access_key_id=ACCESS_ID,
                         aws_secret_access_key=SECRET_KEY)
    uid = uuid.uuid4()
    client.upload_file(path, 'pytime-cdn', f'covers/{uid}.jpg')
    return uid


def upload_train_data(path):
    # Initiate session
    # sess = session.Session()
    # client = sess.client('s3',
    #                      region_name='nyc3',
    #                      endpoint_url='https://nyc3.digitaloceanspaces.com',
    #                      aws_access_key_id=ACCESS_ID,
    #                      aws_secret_access_key=SECRET_KEY)
    uid = uuid.uuid4()
    # client.upload_file(path, 'pytime-font-data', f'train/{uid}.jpg')
    shutil.move(path, f'/Volumes/USB/train/{uid}.jpg')
    return uid


def upload_test_data(path):
    # Initiate session
    # sess = session.Session()
    # client = sess.client('s3',
    #                      region_name='nyc3',
    #                      endpoint_url='https://nyc3.digitaloceanspaces.com',
    #                      aws_access_key_id=ACCESS_ID,
    #                      aws_secret_access_key=SECRET_KEY)
    uid = uuid.uuid4()
    shutil.move(path, f'/Volumes/USB/test/{uid}.jpg')
    # client.upload_file(path, 'pytime-font-data', f'/Volumes/ESD-USB/test/{uid}.jpg')
    return uid
