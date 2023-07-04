### Map이란?
- Map은 리스트나 배열처럼 순차적으로(sequential) 해당 요소 값을 구하지 않고 key를 통해 value를 얻는다.
  
- Key와 Value 한쌍으로 이루어진 자료형이다.
  
- 값(Value)은 중복될 수 있지만, Key는 고유한 값(Unique)
  
> ` Map<Long, String> map = new HashMap<>();`
> 
>  map은 Long을 key값으로, String은 value값으로 저장하는 객체
>
>  map.put(key, value) -> 키 - 값 저장
>
>  map.get(key) -> key에 해당되는 값 리턴

