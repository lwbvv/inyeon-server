from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('__all__')
        # read_only_fields = ('created_at',)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id','email', 'password', 'created' )


class ConfirmRepetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')


class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ('__all__')


class ProfileTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileText
        fields = ('__all__')


class ProfileImageTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImageTest
        fields = ('__all__')


class MaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Male
        fields = ('__all__')

class FemaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Female
        fields = ('__all__')

class MaleScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Male
        fields = ('one_point','two_point','three_point','four_point','five_point', 'raters', 'evaluating')

class FemaleScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Female
        fields = ('one_point','two_point','three_point','four_point','five_point', 'raters', 'evaluating')



# class AppraisalMaleSerializer(serializers.ModelSerializer):
#     member_male = MaleSerializer(many=True, read_only=True)
#     member_profile_image = ProfileImageSerializer(many=True, read_only = True)
#     class Meta:
#         model = Member
#         fields = ('email', 'gender', 'member_male', 'member_profile_image')


class AppraisalSerializer(serializers.ModelSerializer):
    member_male = MaleSerializer(many=True, read_only=True)
    member_female = FemaleSerializer(many=True, read_only=True)
    member_profile_image = ProfileImageSerializer(many=True, read_only = True)
    class Meta:
        model = Member
        fields = ('email', 'gender', 'member_male','member_female', 'member_profile_image')


class RecommendMaleSerializer(serializers.ModelSerializer):
    member_profile_image = ProfileImageSerializer(many=True, read_only = True)
    class Meta:
        model = Male
        fields = ('__all__', 'member_profile_image')

class RecommendFemaleSerializer(serializers.ModelSerializer):
    member_profile_image = ProfileImageSerializer(many=True, read_only = True)
    class Meta:
        model = Female
        fields = ('__all__', 'member_profile_image')
