> ### OAuth
> 인터넷 사용자들이 비밀번호를 제공하지 않고 다른 웹사이트 상의 자신들의 정보에 대해 웹사이트나 애플리케이션의 접근 권한을 부여할 수 있는 공통적인 수단으로서 사용되는, 접근 위임을 위한 개방형 프로토콜

> 1. 장고가 사용자를 github로 보내면 github는 사용자에게 수락할것인지 질문 
> 
> 2. 수락한다면  github는 사용자에게 token을 전달
> 
> 3. 다시 웹 사이트로 돌아온 사용자는 이 토큰을 장고에게 전달
>   
> 4. 장고는 github API와 통신을 하고 사용자 정보를 얻음
>
> https://github.com/settings/applications/new 앱 생성
> ![image](https://github.com/lbk00/study_record/assets/99525751/af5463f4-daf5-4ac3-8c6b-45ce2c2fdad1)

> ### scope
> 사용자로부터 얻고싶은 정보

