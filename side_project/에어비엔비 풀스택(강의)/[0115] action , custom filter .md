> `all().values()` 해당하는 필드를 딕셔너리 형태로 가져옴
>
> `all()` 로 해당하는 모델을 모두 가져와 반복하는 것보다 최적화됨

> `search_fields` 검색 필터 요소에
> 
> ^를 추가하면 해당 키워드로 시작하는 결과를 반환  `"^element"`
> 
> = 해당 키워드와 완벽히 동일한 결과를 반환  `"=element"`
> 
> 아무것도 없으면 contains 으로 검색  `"element"`
> 
> 요소 뒤에 `__fk필드`를 추가하여 해당 fk의 내용으로 검색할수있다  `"element__fk필드"`

> ### admin.action
>
> 어드민 패널에서 여러가지 상호작용을 제어하는 함수
> 
> action함수에는 3가지 요소가 필요
> > 이 액션을 호출한 클래스 `model_admin`
> > 
> > 이 액션을 호출한 유저 정보를 가지고있는 `request`
> > 
> > 선택한 요소들 `queryset`

> ### admin.SimpleListFilter
> 
> 필터를 커스텀하여 원하는 기준으로 필터링 할 수있다.

