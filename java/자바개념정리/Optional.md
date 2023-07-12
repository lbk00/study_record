### 옵셔널 클래스(Optional Class)

- null 가능성에 대해서 스스로 처리하는 클래스 // null로 인한 if-else 문 대체 가능 / if (os1 != null)
  
- null 일 수 있는 인스턴스 변수를 Optional로 선언 

- NPE(NullPointerException) 문제를 해결할 수 있는 방법을 제공, 즉, null 값으로 인해 에러가 발생하는 현상을 효율적으로 방지한다.

- 모든 타입의 객체를 담을 수 있는 래퍼 클래스
  
- Optional 객체를 생성하려면 of() 메서드 또는 ofNullable() 메서드를 사용
  - Optional<String> os1 = Optional.of(new String("Toy1")); : null을 허용하지 않음
  - Optional<String> os2 = Optional.ofNullable(new String("Toy2")); : null을 허용

> ### Optional 클래스의 메서드
>
> orElse("empty") 메서드 : 인스턴스가 비어있으면 전달된 값을 대신 반환
>
> map 메서드 : 반환하는 대상을 Optional 인스턴스에 담아서 반환
> 
> flatMap 메서드 : 그냥 반환, 필요하면 직접 Optional로 감싸야 함
