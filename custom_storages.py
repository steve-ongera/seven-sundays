from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = 'sevensundaysbucket'
    location = 'static'
    default_acl = 'public-read'
    file_overwrite = True


class MediaStorage(S3Boto3Storage):
    bucket_name = 'sevensundaysbucket'
    location = 'media'
    default_acl = 'public-read'  # or None if you want private media
    file_overwrite = False  # Prevent overwriting user uploads
