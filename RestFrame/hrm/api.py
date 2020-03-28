from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serial import *

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class UserAuthentication(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serial=self.serializer_class(data=request.data,context={'request':request})
        serial.is_valid(raise_exception=True)
        user=serial.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        return Response(token.key)

class UserDList(APIView):

        def get(self,request):
            model=UsersD.objects.all();
            serial=UsersDSerial(model,many=True)
            return Response(serial.data)
        
        def post(self,request):
            serial=UsersDSerial(data=request.data)
            if(serial.is_valid()):
                serial.save()
                return Response(serial.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

    def getuser(self,employee_id):
        try:
            model=UsersD.objects.get(id=employee_id)
            return model
        except UsersD.DoesNotExist:
            return 
    
    def get(self,request,employee_id): 
        if not self.getuser(employee_id):
            return Response(f'User with ID {employee_id} is not found in database',status=status.HTTP_404_NOT_FOUND)  

        serial=UsersDSerial(self.getuser(employee_id))
        return Response(serial.data)
        
    def put(self,request,employee_id):
        if not self.getuser(employee_id):
            return Response(f'User with ID {employee_id} is not found in database',status=status.HTTP_404_NOT_FOUND)  

        serial=UsersDSerial(self.getuser(employee_id),data=request.data)
        if(serial.is_valid()):
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,employee_id):
        if not self.getuser(employee_id):
            return Response(f'User with ID {employee_id} is not found in database',status=status.HTTP_404_NOT_FOUND)  
            
        model=self.getuser(employee_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)