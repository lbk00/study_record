> ![image](https://github.com/lbk00/study_record/assets/99525751/0ac94460-79b1-45a0-8412-6e01495a0639)
>
> ### Model
> 서버가 가지고 있는 데이터베이스 작업
>
> ### View
> 브라우저 상에서 사용자에게 보여지는 페이지
>
> ### Controller
> Model 에다가 일을 시키는 작업. User는 뷰를 통해 컨트롤러를 실행시켜 Model에다가 작업을 요청
> 
> View와 Model의 중간다리 역할

> #### 장고에서는 MTV로 View와 Controller의 이름이 다르다
> Model       <->   Model
>
> View         <->   Template
>
> Controller  <->    View

> Django에서는 어플리케이션 단위로 웹페이지를 개발
>
> application기능은 프로젝트 폴더에 넣었다 뺐다 할 수 있어서 개발속도 향상에 도움
>
> ### 프로젝트에 application을 넣고 빼는 작업은 url을 연결시켜주는 작업과 같다
