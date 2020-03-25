from django.db import models

# Create your models here.
    #가입 확인이 안 된다면 일정 시간 뒤에 삭제 되도록 구현해야됨


    ######### 젠더 필드명 나중에 디비 갈아 엎을 떄 man or male로 변경
    #########
    #########
class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, blank=True)
    phoneNumber = models.CharField(max_length=100, blank=True)
    gender = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Male(models.Model):
    member_email = models.ForeignKey(Member,related_name='member_male',on_delete=models.CASCADE, to_field='email')
    start_date = models.DateTimeField(auto_now = True)
    evaluating = models.BooleanField(default = True)
    sign_success = models.BooleanField(default = False)
    raters = models.TextField(blank = True, default = "|")
    one_point = models.IntegerField(default=0)
    two_point = models.IntegerField(default=0)
    three_point = models.IntegerField(default=0)
    four_point = models.IntegerField(default=0)
    five_point = models.IntegerField(default=0)
    total_point = models.IntegerField(default=0)
    average_point = models.FloatField(default=0)
    high_s_member = models.TextField(blank = True, default = "|") #high_score_member
    recommend_user = models.TextField(blank = True, default = "|") #오늘의 추천으로 띄워준 인연?

    def __str__(self):
        return str(self.member_email)


class Female(models.Model):
    member_email = models.ForeignKey(Member,related_name='member_female',on_delete=models.CASCADE, to_field='email')
    start_date = models.DateTimeField(auto_now = True)
    evaluating = models.BooleanField(default = True)
    sign_success = models.BooleanField(default = False)
    raters = models.TextField(blank = True, default = "|")
    one_point = models.IntegerField(default=0)
    two_point = models.IntegerField(default=0)
    three_point = models.IntegerField(default=0)
    four_point = models.IntegerField(default=0)
    five_point = models.IntegerField(default=0)
    total_point = models.IntegerField(default=0)
    average_point = models.FloatField(default=0)
    high_s_member = models.TextField(blank = True, default = "|") #high_score_member
    recommend_user = models.TextField(blank = True, default = "|") #오늘의 추천으로 띄워준 인연?

    def __str__(self):
        return str(self.member_email)


class ProfileImage(models.Model):
    member_email = models.ForeignKey(Member,related_name='member_profile_image',on_delete=models.CASCADE, to_field='email')
    imagePath0 = models.CharField(max_length=255, blank= False)
    imagePath1 = models.CharField(max_length=255, blank= False)
    imagePath2 = models.CharField(max_length=255, blank= True)
    imagePath3 = models.CharField(max_length=255, blank= True)
    imagePath4 = models.CharField(max_length=255, blank= True)

    def __str__(self):
        return str(self.member_email)


class ProfileText(models.Model):
    member_email = models.ForeignKey(Member,on_delete=models.CASCADE, to_field='email')
    nickname = models.CharField(max_length=20, blank = False)
    school = models.CharField(max_length=20, blank = False)
    major = models.CharField(max_length=20, blank = False)
    job = models.CharField(max_length=20, blank = False)
    company = models.CharField(max_length=50, blank = False)
    area = models.CharField(max_length=20, blank = False)
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    body = models.CharField(max_length=20, blank = False)
    character0 = models.CharField(max_length=20, default="")
    character1 = models.CharField(max_length=20, default="")
    character2 = models.CharField(max_length=20, default="")
    blood = models.CharField(max_length=20, blank = False)
    smoking = models.CharField(max_length=20, blank = False)
    alcohol = models.CharField(max_length=20, blank = False)
    religion = models.CharField(max_length=20, blank = False)

    def __str__(self):
        return str(self.member_email)












# from django.db import models
#
# # Create your models here.
#
# class AllMember(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     email = models.CharField(max_length=100, unique=False)
#     password = models.CharField(max_length=100, blank=False)
#     phoneNumber = models.CharField(max_length=100, blank=True)
#     # gender = models.BooleanField(default=True)
#     # sign_success = models.BooleanField(default = False)
#
#     def __str__(self):
#         return self.email
#
#
#
#
# # class Male(models.Model):
# #     member_email = ForeignKey(Member,on_delete=models.CASCADE,to_field='email')
# #     gender = models.BooleanField(default=True)
# #     start_date = models.DateTimeField(auto_now_add=True)
#
#
#
#
#
#
#
#
#
# class ProfileImage(models.Model):
#     member_email = models.ForeignKey(Member,on_delete=models.CASCADE, to_field='email')
#     imagePath0 = models.CharField(max_length=20, blank= False)
#     imagePath1 = models.CharField(max_length=20, blank= False)
#     imagePath2 = models.CharField(max_length=20, blank= True)
#     imagePath3 = models.CharField(max_length=20, blank= True)
#     imagePath4 = models.CharField(max_length=20, blank= True)
#     def __str__(self):
#         return str(self.member_email)
#
# class ProfileText(models.Model):
#     member_email = models.ForeignKey(Member,on_delete=models.CASCADE, to_field='email')
#     nickname = models.CharField(max_length=20, blank = False)
#     school = models.CharField(max_length=20, blank = False)
#     major = models.CharField(max_length=20, blank = False)
#     job = models.CharField(max_length=20, blank = False)
#     company = models.CharField(max_length=50, blank = False)
#     area = models.CharField(max_length=20, blank = False)
#     year = models.IntegerField(default=0)
#     month = models.IntegerField(default=0)
#     day = models.IntegerField(default=0)
#     height = models.IntegerField(default=0)
#     body = models.CharField(max_length=20, blank = False)
#     character0 = models.CharField(max_length=20, default="")
#     character1 = models.CharField(max_length=20, default="")
#     character2 = models.CharField(max_length=20, default="")
#     blood = models.CharField(max_length=20, blank = False)
#     smoking = models.CharField(max_length=20, blank = False)
#     alcohol = models.CharField(max_length=20, blank = False)
#     religion = models.CharField(max_length=20, blank = False)
#
#     def __str__(self):
#         return str(self.member_email)
#
class ProfileImageTest(models.Model):
    imagePath0 = models.CharField(max_length=20, blank= False)
    imagePath1 = models.CharField(max_length=20, blank= False)
    imagePath2 = models.CharField(max_length=20, blank= True)
    imagePath3 = models.CharField(max_length=20, blank= True)
    imagePath4 = models.CharField(max_length=20, blank= True)
    def __str__(self):
        return self.imagePath0
