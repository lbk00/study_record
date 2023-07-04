### 람다식(Lambda Expression) 이란?

- 함수를 하나의 식(expression)으로 표현한 것

- 익명 함수의 한 종류

- 불필요한 코드를 줄이고, 가독성을 높이기 위함

> `(매개변수, ...) -> { 실행문 }`

### 스트림(Stream) 이란?

- 컬렉션의 저장 요소를 하나씩 참조해서 람다식으로 처리할 수 있도록 해주는 반복자
  
- 최종 연산 전까지 중간연산을 수행되지 않음
  
- 스트림은 원본 데이터 소스를 변경하지 않음

> `store.values().stream().filter(member -> member.getName().equals(name)).findAny();`
