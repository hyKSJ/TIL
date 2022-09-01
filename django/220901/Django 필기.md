# Django

* ### intro
  
  * framework :  만들어 놓은 것 재사용 문화
  
  * server 만드는 framework
  
  * design pattern : 자주 사용하는 구조가 있어서 이를 일반화해서 하나의 공법으로 만든 것 (방법론)
  
  * 

정적 웹페이지 = 데이터 변화X

동적 웹페이지 = 데이터 변화O  (ex. 안녕, 원석)

static typing -> c java

dynamic typing -> python js (ex. list와 array(java) 차이 -> list는 뒤에 빈공간이 만들어져 있음)

MVT -> MVC(스프링) 기반 변형패턴

M = data

(View) --> 중간다리 역할(처리) , MVC view와 다름

T = 화면(HTML)

URLS -> 푸드코트 주문과 비슷

가상 설치

가상 실행

pip install 라이브러리

백업은 -> freeze

백업한거 설치는 install -r ~~

앱등록 ->  프로젝트 -> 셋팅 -> 인스톨 앱(순서 중요, 장고꺼를 밑에 커스텀을 위에)

코드작성 프로젝트 -> urls (from ~ import~)

1.앱만드릭

startapp ~~~~

2. 등록
   
   firstpjt -> setting.py ->installed_apps

3. urls.py 코드 자겅
   
   path(in~)

장고 템플릿 언어

html안에 장고 코드 비슷한거 넣는다 (파이썬은 아닌데 파이썬처럼 씀)

템플릿(화면 html) 상속

ex. 부트스트립 일일히 html 다 넣기 불편하기 떄문에 base html으로 상속 받게 함

form action method(get,post)

get = 데이터변화x,주소에 데이터 o

post = 데이터 변화 o,주소에 데이터 x
