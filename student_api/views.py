from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


from .serializers import StudentSerializer, PathSerializer
from .models import Student, Path

# Function Based Views


@api_view(['GET'])
def get_all_students(request):
    db_all_students = Student.objects.all()
    converter = StudentSerializer(db_all_students, many=True)
    return Response(converter.data)


@api_view(['POST'])
def add_new_student(request):
    json_user_sent = request.data
    converter = StudentSerializer(data=json_user_sent)
    if converter.is_valid():
        converter.save()
        message = {
            "details": "Öğrenci başarılı bir şekilde oluşturuldu"
        }
        return Response(message, status=status.HTTP_201_CREATED)

    return Response(converter.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_one_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    converter = StudentSerializer(one_student)
    return Response(converter.data)


@api_view(['PUT'])
def update_existing_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=one_student, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_existing_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    one_student.delete()

    return Response({"detail": "Öğrenci başarılı bir şekilde silindi"})


@api_view(['PATCH'])
def partially_update_student(request, pk):
    one_student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(
        instance=one_student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = {"detail": "Öğrenci başarılı bir şekilde güncellendi"}
        return Response(message, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_paths(reguest):
    db_all_paths = Path.objects.all()
    converter = PathSerializer(db_all_paths, many=True)
    return Response(converter.data)


@api_view(['POST'])
def add_new_path(request):
    converter = StudentSerializer(data=request.data)
    if converter.is_valid():
        converter.save()
        message = {
            "details": "Path başarılı bir şekilde oluşturuldu"
        }
        return Response(message, status=status.HTTP_201_CREATED)

    return Response(converter.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def get_one_path(request, pk):
    one_path = get_object_or_404(Path, id=pk)
    converter = PathSerializer(one_path)
    return Response(converter.data)


@api_view(['PUT'])
def update_existing_path(request, pk):
    one_path = get_object_or_404(Path, id=pk)
    serializer = PathSerializer(instance=one_path, data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_existing_path(request, pk):
    one_path = get_object_or_404(Path, id=pk)
    one_path.delete()

    return Response({"detail": "Path başarılı bir şekilde silindi"})


@api_view(['PATCH'])
def partially_update_path(request, pk):
    one_student = get_object_or_404(Path, id=pk)
    serializer = PathSerializer(
        instance=one_student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message = {"detail": "Path başarılı bir şekilde güncellendi"}
        return Response(message, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class Based Views

class StudentListCreate(APIView):
    def get(self, request):
        db_all_students = Student.objects.all()
        serializer = StudentSerializer(db_all_students, many=True)
        return Response(serializer.data)

    def post(self, request):
        json_user_sent = request.data
        converter = StudentSerializer(data=json_user_sent)

        if converter.is_valid():
            converter.save()
            message = {
                "details": "Öğrenci başarılı bir şekilde oluşturuldu"
            }
            return Response(message, status=status.HTTP_201_CREATED)

        return Response(converter.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentRetrieveUpdateDestroy(APIView):

    def get(self, request, pk):
        one_student = get_object_or_404(Student, id=pk)
        converter = StudentSerializer(one_student)
        return Response(converter.data)

    def put(self, request, pk):
        one_student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=one_student, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        one_student = get_object_or_404(Student, id=pk)
        one_student.delete()

        return Response({"detail": "Öğrenci başarılı bir şekilde silindi"})


class PathListCreate(APIView):
    def get(self, request):
        db_all_paths = Path.objects.all()
        converter = PathSerializer(db_all_paths, many=True)
        return Response(converter.data)

    def post(self, request):
        converter = StudentSerializer(data=request.data)
        if converter.is_valid():
            converter.save()
            message = {
                "details": "Path başarılı bir şekilde oluşturuldu"
            }
            return Response(message, status=status.HTTP_201_CREATED)

        return Response(converter.errors, status=status.HTTP_400_BAD_REQUEST)


class PathRetrieveUpdateDestroy(APIView):
    def get(self, request, pk):
        one_path = get_object_or_404(Path, id=pk)
        converter = PathSerializer(one_path)
        return Response(converter.data)

    def put(self, request, pk):
        one_path = get_object_or_404(Path, id=pk)
        serializer = PathSerializer(instance=one_path, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        one_path = get_object_or_404(Path, id=pk)
        one_path.delete()

        return Response({"detail": "Path başarılı bir şekilde silindi"})

# Generic API Views


class StudentsGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PathsGAV(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PathDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Concrete API View


class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class PathCV(ListCreateAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer


class PathDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer


class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer
