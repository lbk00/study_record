=> 
화살표 함수
 기존의 함수 선언식이나 함수 표현식보다 좀 더 간결하게 표현할수 있다
const add = (a, b) => {
    return a + b;
};
function 키워드 대신 =>기호(화살표)를 사용
컴포넌트(Component) 
재사용이 가능한 각각의 독립된 모듈
컴포넌트 key
React가 어떤 항목을 변경하거나 추가할지 또는 삭제할지 구별하도록 돕는 역할
같은 컴포넌트를 여러 번 렌더링할 때, 다른 컴포넌트임을 구분하기 위해 사용하는 속성
컴포넌트로 데이터를 fetch하는 방법..
Fetch
 네트워크 요청 API 중 하나로 특정 URL로부터 정보를 받아오는 API
fetch()로부터 반환받은 객체는 단순한 HTTP Response로 실제 JSON이 아니다. response로 부터 원하는 데이터를 가져오기 위해 json()메서드 사용 ( 응답 데이터를 JSON 개체로 변환 ) 

 useState
컴포넌트의 상태를 간편하게 생성하고 업데이트 해주는 도구를 제공
const [state, setState] = useState(초기값);
컴포넌트의 현재 상태 값은 state변수에 들어있고 state를 변경하려면 setState 함수를 이용해서 변경
props
프로퍼티
상위 컴포넌트가 하위 컴포넌트에 값을 전달할때 사용하는 속성
