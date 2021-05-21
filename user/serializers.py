# serializers.py
#from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
"""
class UserLoginSerializer(LoginSerializer):
    def get_fields(self):
        fields = super(LoginSerializer, self).get_fields()
        fields['email'] = fields['username']
        #username = None
        del fields['username']
        return fields

    #def validate(self, attrs):
        #attrs['username'] = attrs['email']
        #del attrs['email']
        #return super(LoginSerializer, self).validate(attrs)

"""
class UserLoginSerializer(LoginSerializer):
    username = None

#class UserRegisterSerializer(RegisterSerializer):
#    username =None