> ### M-N 관계
>
> `models.ManyToManyField()`
>
> 다대다 관계로 하나의 모델이 여러개의 모델을 가질수 있음을 의미한다

> ### Meta
>
> model의 동작이나 Django가 model로 무엇을 해야하는지 커스텀해주는 클래스
> 
>```
>class Meta: 
>  abstract = True #클래스 모델안에 선언하여 데이터베이스에 저장되지않게 한다
>  verbose_name_plural = "복수형" # 복수형 표현을 어떻게 나타낼지 정의해준다
>```

> `blank = True` // form에서 필드가 필수적이지 않게 해준다
> 
> `null = True` // 이 필드가 데이터베이스에서 null일 수 있음

> ### startapp으로 어플리케이션을 추가 후, config/setting.py에 추가해줘야 한다
>
> 파이썬에서는 튜플을 괄호없이 표현가능

