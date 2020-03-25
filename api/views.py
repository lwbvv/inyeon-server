from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
import json
from rest_framework.parsers import JSONParser
import io
from ast import literal_eval
from django.core import serializers
# from braces.views import CsrfExemptMixin

class MemberCreate(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'email'


class GenderCreate(APIView):
    authentication_classes = []
    def post(self, request, format=None):
        userEmail = request.data["member_email"]
        clientGender = request.data["gender"]

        requestString = str(request.data)
        commaIndex = requestString.find(',')
        emailParsing = requestString[0:commaIndex]+"}"
        dictionary = literal_eval(emailParsing)
        # data = json.load(jsondata)
# jsondata = json.dumps(score.data)
# stream = io.StringIO(jsondata)
# data = json.load(stream)

        # # get 방식으로 아이디 패스워드 보낸 후 반환 해 준다
        if clientGender:
            serializer = MaleSerializer(data = dictionary)
        else:
            serializer = FemaleSerializer(data = dictionary)

        if serializer.is_valid():
            serializer.save()
            return Response("0")

        return Response(dictionary)



class ProfileImageCreate(viewsets.ModelViewSet):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
    lookup_field = 'member_email'

class ProfileTextCreate(viewsets.ModelViewSet):
    queryset = ProfileText.objects.all()
    serializer_class = ProfileTextSerializer
    lookup_field = 'member_email'

class ProfileImageTestCreate(viewsets.ModelViewSet):
    queryset = ProfileImageTest.objects.all()
    serializer_class = ProfileImageTestSerializer

##############################################################################################
# APIview 클래스 이용


class LoginDetail(APIView):
    authentication_classes = []

    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, string):
        try:
            return Member.objects.get(email = string) #디비에서 불러오는 부분
        except Member.DoesNotExist:
            raise Http404
    def post(self, request, format=None):
        clientEmail = request.data['email']
        clientPassword = request.data['password']
        userData = ""
        result = "0"
        # # get 방식으로 아이디 패스워드 보낸 후 반환 해 준다

        try:
            userData = Member.objects.get(email = clientEmail)
        except Member.DoesNotExist:
                return Response("0")

        dbEmail = userData.email
        dbPassword = userData.password
        if clientPassword == dbPassword:
            result = "2"
        else:
            result = "1"

        sendData = str(userData.gender) + result

        return Response(sendData)



###################################################################################
#이메일 중복 확인하는 부분
###################################################################################
class ConfirmRepetition(APIView):
    def get_object(self, pk):
        try:
            return Member.objects.get(pk = pk) #디비에서 불러오는 부분
        except Member.DoesNotExist:
            raise Http404
###
### 동일한 이메일이 존재 할 경우 1을 반환 아닐 경우 0을 반환
###
###
    def post(self, request, format=None):
        responseData = -1
        user_email = request.data["email"]
        queryset = ""
        try:
            queryset = Member.objects.get(email = user_email) #디비에서 불러오는 부분
        except Member.DoesNotExist:
            queryset = "실패"
        if user_email == str(queryset) :
            responseData = 1 #아이디가 있으면 1 반환
        else:
            responseData = 0# 없으면 0 반환
        return Response(responseData)

###################################################################################
#이메일 중복 확인하는 부분
###################################################################################




##################################################################################
#회원 평가 데이터 정렬하기
##################################################################################
class GetAssessmentData(APIView):
    authentication_classes = []

    def get_object(self, string):
        try:
            return Member.objects.get(email = string) #디비에서 불러오는 부분
        except Member.DoesNotExist:
            raise Http404


###################################################################################################################################
#처리해야 되는 조건: 해당 유저가 아예 없을 경우 반환값,
###################################################################################################################################
    def post(self, request, format=None):
        user_email = request.data["email"] #클라이언트에서 이메일을 받아온다(평가 하는 사람 이메일)
        userRater = "|"+user_email+"|"
        gender = request.data["gender"] #클라이언트에서 성별을 받아옴(평가 하는 사람 성별)
        evaluating_member = ""
        profileImage = ""
        profileText = ""
        userData = "없음"
        assessment_serializers = None
       #평가를 하는 유저가 남자 유저인지 여자 유저인지 if문으로 판별
        try:
            if gender == True:
                evaluating_member = Female.objects.filter(evaluating = True).order_by('start_date')[:5] # 유저가 남자일 경우 여성 테이블에서 현재 심사 진행중인 유저를 필터링 한 뒤 날짜 순서대로 정렬하여 50명을 가져온다
                assessment_serializers = FemaleSerializer(evaluating_member, many = True) #10분의 1 규모로 테스트
            else:
                evaluating_member = Male.objects.filter(evaluating = True).order_by('start_date')[:5] #유저가 여성일 경우 남성 테이블에서 현재 심사 진행중인 유저를 필터링 한 뒤 날짜 순서대로 정렬하여 50명을 가져온다
                assessment_serializers = MaleSerializer(evaluating_member, many = True) #10분의 1 규모로 테스트
        except Member.DoesNotExist:
            evaluating_member = "실패"

        #평가진행중인 유저의 쿼리셋을 제이슨 형태로 변형시켜준다 제이슨 어레이 안에 제이슨 오브젝트가 쌓이는 형식으로 들어간다

        for user in assessment_serializers.data: #유저의 데이터를 처음부터 순차적으로 순회하면서 내가 평가를 한 유저인지 확인한다(raters에 문자열이 포함되어 있는지 확인)
            rater = user["raters"]
            if not userRater in rater:
                profileImage = ProfileImage.objects.get(member_email = user['member_email'])
                profileText = ProfileText.objects.get(member_email = user["member_email"])
                profileImage_serializers = ProfileImageSerializer(profileImage)
                profileText_serializers = ProfileTextSerializer(profileText)
                userData = [user,profileImage_serializers.data,profileText_serializers.data] #클라이언트에 뿌려줄 데이터 어레이로 묶어서 보내는 부분
                jsondump = json.dumps(userData)
                return Response(str(jsondump))


        return Response(userData)

# 별점 주는 부분
    # def put(self, request, pk, format=None):
    #     snippet = Male.objects.get(member_email = pk)
    #     serializer = MaleSerializer(snippet)
    #     # if serializer.is_valid():
    #         # serializer.save()
    #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##################################################################################################
#화원 평가시 별점 바꿔주는 부분
##################################################################################################
    def patch(self, request, string, format=None):
        query = self.get_object(string)


        # 성별에 따라 유저의 쿼리 데이터 불러오는 부분
        if query.gender:
            user = Male.objects.get(member_email = query.email)# 이메일을 이용해서 평가 받는 사람 쿼리 가져와서 젠더 사용하고 매칭 데이터 불러온다
            score = MaleScoreSerializer(user)
        elif query.gender==False:
            user = Female.objects.get(member_email = query.email)
            score = FemaleScoreSerializer(user)

        jsondata = json.dumps(score.data)
        stream = io.StringIO(jsondata)
        data = json.load(stream)
        if (request.data['point'] == 1):
            data['one_point'] += 1
        elif(request.data['point'] == 2):
            data['two_point'] += 1
        elif(request.data['point'] == 3):
            data['three_point'] += 1
        elif(request.data['point'] == 4):
            data['four_point'] += 1
        elif(request.data['point'] == 5):
            data['five_point'] += 1
        data['raters'] = data['raters']+request.data['raters']


        ratersCount = data['one_point']+ data['two_point']+ data['three_point']+ data['four_point']+ data['five_point']# 총 몇명의 회원이 평가 했는지
        #5명 이상이 평가 했을 시에 평가 한 유저를 초기화 하고 '평가중' 상태를 평가완료 상태로 만든다
        if ratersCount > 2:
            data['raters'] = "|"
            data['evaluating'] = False

        if(query.gender):
            serializer = MaleScoreSerializer(user, data = data)
        elif(query.gender==False):
            serializer = FemaleScoreSerializer(user, data = data)

        if serializer.is_valid():
            serializer.save()

        return Response(str(data['one_point']))




##################################################################################
#평가 페이지 데이터 뿌려주는 부분
##################################################################################
class Appraisal(APIView):

    def get_object(self, string):
        try:
            return Member.objects.get(email = string) #디비에서 불러오는 부분
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, string):
        # result = Member.values_list(id = 2)
        result = Member.objects.get(email = string)

        serializers = AppraisalSerializer(result)
        # jj = json.loads(result)
        # return Response(str(result.male_set.get(member_email=result.email)))
        # jsondata = json.dumps(serializers.data)
        return Response(serializers.data)


class RecommendOpposite(APIView):
    authentication_classes = []
    def patch(self, request, string, format=None):

# 이메일로 조회해서 그냥 바로 데이터를 get으로 가져온다
        gender = request.data['gender']
        if gender == True:
            oppositeMember = Female.objects.filter(average_point__gt = 3.0).exclude(recommend_user__exact = "|"+string+"|").order_by("?").first()
            # oppositeMember = Female.objects.filter(average_point__gt = 3.0).first()
            recommend = FemaleSerializer(oppositeMember)
        else:
            oppositeMember = Male.objects.filter(average_point__gt = 3.0).exclude(recommend_user__exact = "|"+string+"|").order_by("?").first()
            recommend = MaleSerializer(oppositeMember)

            # 데이터가 없을 시에 없음 반환
        if recommend.data['member_email'] is None:
            return Response("없음")

        jsondata = json.dumps(recommend.data)
        stream = io.StringIO(jsondata)
        data = json.load(stream)
        data['recommend_user'] = data['recommend_user'] + string + "|"


        user_email_dict = {'recommend_user' : oppositeMember.recommend_user + string + "|"}

        if gender == True:
            serializer = FemaleSerializer(oppositeMember, data = data)
        else:
            serializer = MaleSerializer(oppositeMember, data = data)

        # 화면에 뿌려질 유저의 프로파일 이미지 가져오는 부분


        if serializer.is_valid():
            serializer.save()
            recommend_user = serializer.data['member_email']
            profileImage = ProfileImage.objects.get(member_email = recommend_user)
            profileSerializer = ProfileImageSerializer(profileImage)
            profileText = ProfileText.objects.get(member_email = recommend_user)
            profileTextSerializer = ProfileTextSerializer(profileText)
            recommendOb = {"user_data" : serializer.data, "image" : profileSerializer.data, "text" : profileTextSerializer.data}
            return Response(recommendOb)

        return Response(serializer.data['recommend_user'])
