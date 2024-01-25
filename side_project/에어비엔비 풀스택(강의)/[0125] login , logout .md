> #### 사용자 생성 후, 비밀번호를 저장할 때
> 
> `user.password = password` #해쉬화되지않은 비밀번호를 db에 바로 저장하는 것이므로 위험하다

> ```
> user.set_password(password) # django에서 비밀번호를 해쉬화
> user.save() # db에 해쉬화된 비밀번호를 저장
> ```
> `user.check_password(old_password):` # 기존 비밀번호와 동일한지 검사

> #### django에서는 login과 logout 기능을 지원하므로 사용자 로그인 , 로그아웃을 수행가능
