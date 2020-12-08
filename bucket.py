import boto3

s3 = boto3.resource(
    "s3",
    endpoint_url='http://uvo1hthw26l85bir0ud.vm.cld.sr',
    aws_access_key_id='5sWfq4PMTSCH_lWPdwsJZA',
    aws_secret_access_key='UKCoNKgzn/MNz9nNJDzEv2DajLRE1xzuSL8YclwT',
)

bucket = s3.Bucket("images")


def download(filename):
    try:
        output_path = './.tmp/{}'.format(filename)
        bucket.download_file(filename, output_path)

        return output_path
    except Exception as e:
        return None


def upload(filename):
    try:
        input_path = './.tmp/{}'.format(filename)
        bucket.upload_file(input_path, filename)

        return input_path
    except Exception as e:
        return None


def list_files():
    try:
        files = []
        for my_bucket_object in bucket.objects.all():
            files.append(my_bucket_object.key)

        return files
    except Exception as e:
        return []
