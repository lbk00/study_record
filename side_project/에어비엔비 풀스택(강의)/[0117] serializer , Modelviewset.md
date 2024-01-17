> ### serializer
> user로부터 데이터를 받아 장고 모델을 만드는데 필요 (양방향 번역기)
> 
> 데이터의 형태를 알려줘야한다 // 데이터가 올바른지 검사해줌

> `is_valid()`  데이터가 유효한지 검사
>
> `**` 딕셔너리를 가져와 형태를 바꿔준다
```
{ "name" : "카테고리 from DRF", "kind" : "rooms"}
->
name = "카테고리 from DRF"
kind = "rooms"
```
> `partial=True` 이곳으로 들어오는 데이터가 완벽한 형태가 아닐수도 있음을 알려준다

> ### APIView
> if-elif문 대신 get_object로 객체를 가져온 뒤 get / put / post / delete 메서드를 수행할 수 있다
> 
> serializer는 해당 모델에 있는 데이터 형식을 모두 지정해줘야하므로 비효율적

> ### ModelSerializer
> 데이터 형식을 지정할 필요없이 serializer를 설정할수 있다
> ```
> class Meta:
>	model = Category # Category 모델을 위한 serializer 생성
>	fields = “__all__” # 보여질 필드 설정
> ```

> Modelviewset의 필요한 두가지 property
> 
> serializer_class = 어떤 Serializer인지
> 
> queryset = viewset의 object
>
> 그 후, Http 메소드와 class 메소드를 연결

