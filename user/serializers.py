# serializers.py
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_auth.serializers import PasswordChangeSerializer, UserDetailsSerializer
from rest_framework import serializers
from user.models import User

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



class UserRegisterSerializer(RegisterSerializer):
    pass

class UserLoginSerializer(LoginSerializer):
    #authentication_classes = (TokenAuthentication,)
    username = None



# 프로필 수정
class UserUpdateSerializer(PasswordChangeSerializer):  # 패스워드 변경 시리얼라이저 상속하여 비밀번호 변경과 암호자동화
    username = serializers.CharField(max_length=20)
    old_password = serializers.CharField(max_length=128)
    new_password1 = serializers.CharField(max_length=128, allow_blank=True)
    new_password2 = serializers.CharField(max_length=128, allow_blank=True)
    phone = serializers.CharField(max_length=100)
    birth = serializers.DateField()  # yyyy-mm-dd

    def validate(self, attrs):
        if attrs['new_password1']=='':
            attrs['new_password1'] = attrs['old_password']
        if attrs['new_password2']=='':
            attrs['new_password2'] = attrs['old_password']
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            print(attrs['new_password1'], attrs['new_password2'], attrs['old_password'])
            raise serializers.ValidationError(self.set_password_form.errors)
        try:
            temp_user = User.objects.get(username=attrs['username'])
        except Exception as e:
            temp_user = None
        if temp_user != None and self.user.username!=temp_user.username:  # 이미 리퀘스트의 유저네임이 있다는 것(중복)
            raise serializers.ValidationError('Username check error')
        else:  # 유저네임 중복 없으니까 데이터 변경
            self.user.birth = attrs['birth']
            self.user.username = attrs['username']
            self.user.phone = attrs['phone']
        return attrs

# 프로필 조회
class UserInfoSerializer(UserDetailsSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'birth', 'phone', 'avail_storage', 'used_storage', 'kakao', 'naver',
                  'last_login', 'date_joined')
        read_only_fields = ('email', )