
from folder.models import file


def get_image_by_face_recognition(male, female):
    data = file.objects.all()
    return data
print(get_image_by_face_recognition(1,1))