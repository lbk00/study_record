> ### 프로젝트 수행을 위해 각각의 가상환경으로 독립적인 설치환경 생성 (비눗방울) , 같은 패키지를 다른 버전으로 사용

> ## poetry?
> python 개발시 패키지의 의존성을 관리하는 라이브러리

> ### Poetry add django 에러 발생
> 
>  파이선 버전 3.7 -> 3.12로 업그레이드 후
> 
> Poetry env use python // poetrty 파이썬 버전 변경
> 
> python = "^3.7" -> python = "^3.12" 변경

> poetry shell //poetry 진입
>
> exit // poetry 종료


>1.	mkdir 폴더 생성
>2.	git init
>3.	poetry 설치 
>    `pip install poetry`
>4.	`poerty init` // poetry 생성
>5.	`poetry add django`
>6.	`poetry shell` // 가상환경 진입
>오류 발생시
>파워쉘- 관리자 권한 실행 후 `Set-ExecutionPolicy RemoteSigned` 입력
>7.	`django-admin startproject ‘프로젝트 이름’ .` 입력  // 프로젝트 생성
>8.	git ignore 세팅
