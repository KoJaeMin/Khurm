
#작동안됨 ㅜ
from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3StaticStorage',
    'S3DefaultStorage',
)

#class MediaStorage(S3Boto3Storage):
	#location = 'media' # s3 저장경로
	#file_overwrite = False # 이름 그대로


# for media
class S3DefaultStorage(S3Boto3Storage):
    default_acl = 'private'
    location = 'media'
    
# for static
class S3StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = 'static'