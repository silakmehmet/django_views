from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    # FBP
    get_all_students,
    add_new_student,
    get_one_student,
    update_existing_student,
    delete_existing_student,
    partially_update_student,
    get_all_paths, add_new_path,
    get_one_path,
    update_existing_path,
    delete_existing_path,
    partially_update_path,

    # CBP
    StudentListCreate,
    StudentRetrieveUpdateDestroy,
    PathListCreate,
    PathRetrieveUpdateDestroy,

    # GBP
    StudentsGAV,
    StudentRetrieveUpdateDestroy,
    PathsGAV,
    PathDetailGAV,

    # CAV
    StudentCV,
    StudentDetailCV,
    PathCV,
    PathDetailCV,

    # MVS
    StudentMVS,
    PathMVS
)

router = DefaultRouter()
router.register("students", StudentMVS)
router.register("paths", PathMVS)

urlpatterns = [
    # Function Based Views

    # path("students/", get_all_students),
    # path("add_student/", add_new_student),
    # path("paths/", get_all_paths),
    # path("add_path/", add_new_path),

    # # DETAILS
    # path("student/<int:pk>", get_one_student),
    # path("update_student/<int:pk>", update_existing_student),
    # path("delete_student/<int:pk>", delete_existing_student),
    # path("p_u_student/<int:pk>", partially_update_student),
    # path("path/<int:pk>", get_one_path),
    # path("update_path/<int:pk>", update_existing_path),
    # path("delete_path/<int:pk>", delete_existing_path),
    # path("p_u_path/<int:pk>", partially_update_path),

    # Class Based Views
    # path("students/", StudentListCreate.as_view()),
    # path("student/<int:pk>", StudentRetrieveUpdateDestroy.as_view()),
    # path("paths/", PathListCreate.as_view()),
    # path("path/<int:pk>", PathRetrieveUpdateDestroy.as_view()),

    # Generic Based Views
    # path("students/", StudentsGAV.as_view()),
    # path("student/<int:pk>", StudentRetrieveUpdateDestroy.as_view())
    # path("paths/", PathListCreate.as_view()),
    # path("path/<int:pk>", PathDetailGAV.as_view()),


    # Concrete View

    # path("students/", StudentCV.as_view()),
    # path("student/<int:pk>", StudentDetailCV.as_view())
    # path("paths/", PathCV.as_view()),
    # path("path/<int:pk>", PathDetailCV.as_view()),


    # Model View Set

    path("", include(router.urls))

]
