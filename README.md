# django_board-api


> 3가지 폴더
>
>* django-board
>    - MySQL 데이터 베이스를 활용한 게시판 개발
>    - allauth를 통한 회원가입
>
>* boardapi
>    - boardapi_server를 활용한 게시판 개발
>
>* boardapi_server
>    - REST api 서버
>    - HTTP 의 ruequst 이용한 CRUD 서비스도 가능
>    - rest-auth를 통한 회원가입



# 개발환경

>* server
>   - ubuntu 18.04LTS (윈도우 wsl)
>* db
>   - MySQL
>* python
>   - 3.74 ver
>   - Django 3.12
>   - Django REST Framework 3.12.1




# RESTful api server end-points

>* 회원가입
>
> |HTTP|Path|Method|목적|
> |------|---|---|---|
> |POST|rest-auth/registration/|CREATE|USER 생성|
>
>* 게시판
>
> |HTTP|Path|Method|목적|
> |------|---|---|----------|
> |GET|boardapi/|LIST|게시판 조회|
> |POST|boardapi/|CREATE|게시글 작성|
> |GET|boardapi/<int:pk>/|READ|게시글 조회|
> |PUT|boardapi/<int:pk>/|UPDATE|게시글 수정|
> |DELETE|boardapi/<int:pk>/|DELETE|게시글 삭제|

# References

> * Youtube BIPA SORI
> https://www.youtube.com/watch?v=ycgDdzxpxQs&list=PLr_ki3_GfpZMCHR_Im1AEeRd-NNs16KSh
>   - django-board에 참고
