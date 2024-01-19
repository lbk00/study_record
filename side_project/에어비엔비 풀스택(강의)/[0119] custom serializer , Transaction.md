> Serializer를 설정할 때
> 
> `depth = 1`을 추가하여 fk로 연결된 데이터를 모두 가져옴
> #### 모든정보를 가져오기 때문에 DB에 비효율적(커스텀 할 수가 없음)

> ### Serializer를 커스텀하는법
> 해당 serializer가 특정 필드를 serialize 하려고하면
> 
> Serializer 내부에서 `field = 원하는 serializer` 로 설정할수있다
> 
> serializer로 post를 이용해 데이터를 생성할 때
> 
> 해당 필드가 입력받지않아도 됨을 표시하려면 serializer에 `read_only = True` 설정
> 
> `owner = TinyUserSerializer(read_only=True)`

> #### `request.user`
>  현재 로그인한 유저의 정보를 가져온다
> 
> `create`나 `save` 메서드의 validated_data에 데이터를 추가하려면
> 
> save를 호출할 때 데이터를 추가해주면 된다
> ```
> room = serializer.save(
>                    owner=request.user,
>                    category=category,
>                ) 
>```

> ManyToMany 관계에서는 FK와 다르게 `save()` 메서드 내부에 데이터를 넘겨주지않고
> 
> 생성된 객체를 통해 `add()` , `remove()` 로 데이터를 추가 및 삭제 할 수있다.
>
> `room.amenities.add(amenity)`
> 
> 여러 개의 값을 입력받고 , 하나씩 해당 값이 유효한지 검증

> ### 트랜잭션 (all or nothing)
> 코드 중 하나라도 오류가 발생하면 DB에서 변경된 사항들을 모두 되돌린다
> 
> ```
> with transaction.atomic():
>	  #DB에 변경사항을 주는 쿼리들
> ```


