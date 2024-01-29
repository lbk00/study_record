> `MEDIA_ROOT`
>
>  사진이 업로드되는 폴더를 지정할수있음 / 서버에 실제로 파일이 존재하는 장소

> `MEDIA_URL`
>
> 해당 url에서 서버에 업로드된 파일들에 접근할수있음 / 브라우저가 파일에 가는 방법

> #### 파일 -> Cloudflare에 업로드 -> 파일의 url -> 장고에게 url 제공

> ### permission_classes 
> 해당 View에 대한 권한을 설정해서 사용자가 서비스를 이용할수 있는지 권한을 검증
> 
> `IsAuthenticated` 인증된 사용자만 사용가능
> 
> `IsAutheticatedOrReadOnly` 요청이 GET이라면 누구나 통과할 수 있게 해주고,
> 
> POST, PUT, DELETE라면 오직 인증받는 사람들만 통과할 수 있다

