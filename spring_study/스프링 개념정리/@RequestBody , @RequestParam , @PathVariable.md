> ### @RequestBody
> 클라이언트와 서버 간의 HTTP 통신에서 요청과 응답을 보낼 때, 필요한 데이터를 담아서 보내는 공간
> 
> ![image](https://github.com/lbk00/study_record/assets/99525751/2fdb9aef-b3be-43fd-a408-f9533df074df)
>
> 즉, Body를 이용해 응답 메시지로 데이터를 전달하는 방식

> ### @RequestParam
> 쿼리 파라미터로 전달된 값을 추출하여 사용하는 방식
> 
> ### `URL?파라미터=값`
>
> `required = false` 옵션 추가 시 key값이 없어도 예외 발생 안함 (기본값 true)
 
> ### @PathVariable
> URL 경로에서 변수 값을 추출하여 매개변수에 할당하는 방식
>
> ### `URL/변수`
