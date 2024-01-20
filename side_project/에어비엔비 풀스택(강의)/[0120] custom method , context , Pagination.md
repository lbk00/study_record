> ### Serializer  커스텀 메서드 (함수 호출하는법)
> ```
> rating = serializers.SerializerMethodField() #rating의 값을 계산할 메서드를 만들것이라고 알려준다
> def get_rating(self,room): #2번째 인자로 연결된 모델을 받는다. get_필드의 모양을 가져야한다
>   return room.rating()# 해당 모델에 있는 메서드 호출
> ```

> ### context
>  Serializer로 데이터를 보내준다
> 
> `context={"request": request},` serializer에서 request객체 사용가능

> ### 동적필드
> 해당 api를 보고있는 유저에따라 값이 달라지는 필드

> ### Pagination 
> 한번에 불러올 데이터가 너무 많은경우 , DB에 문제를 줄수있음
> 
> 페이지를 설정해 불러올 데이터 갯수를 제한
> 
> #### /urls?page=1
> ```
> page = request.query_params.get('page',1) # url에 있는 page 를 가져온다
> page = int(page)
> ```

> #### 쿼리세트는 평가하기 전까지 로드되지 않는다
> `room.reviews.all()[start:end],` # 해당 쿼리 세트에 인덱스를 설정해 페이지네이션 가능

> ### A - FK(B) // 모델 A가 모델 B에 대한 외부키를 가지고있으면
> 
> ### B.A_set // 모델 B는 자동적으로 A_set이라는 역접근자를 받음
