### 옵셔널 클래스(Optional Class)

- null 가능성에 대해서 스스로 처리하는 클래스

- NPE(NullPointerException) 문제를 해결할 수 있는 방법을 제공, 즉, null 값으로 인해 에러가 발생하는 현상을 효율적으로 방지한다.

- 모든 타입의 객체를 담을 수 있는 래퍼 클래스
  
- Optional 객체를 생성하려면 of() 메서드 또는 ofNullable() 메서드를 사용
  - Optional<String> os1 = Optional.of(new String("Toy1")); : null을 허용하지 않음
  - Optional<String> os2 = Optional.ofNullable(new String("Toy2")); : null을 허용


