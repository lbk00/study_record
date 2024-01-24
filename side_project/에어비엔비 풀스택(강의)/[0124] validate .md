> `serializer.is_valid()`로 유효성을 검사할 때 
>
> #### 특정 필드의 유효성을 커스텀하려면 serializer 내부에 메서드 정의
> 
> `validate_원하는필드` / 검증 시 유효한 값이면 value를 리턴 , 그렇지 않다면 에러 리턴
>
> ``` 
> def validate_check_in(self,value): # check_in 필드의 유효성 검사
>        now = timezone.localtime(timezone.now()).date()
>        if now > value :
>            raise serializers.ValidationError("예약시작 시간이 현재보다 과거입니다")
>        return value
>```
    
> 모든 필드 유효성을 검사하려면 validate 메서드 정의
> ```
> def validate(self,data): # 모든 data를 전달받음
>   return data
> ```

