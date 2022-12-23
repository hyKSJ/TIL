# 알고리즘_3DAY

* 슬라이딩 윈도우
  
  * 2개의 포인터로 범위 지정 후, 범위 유지한 채 이동하며 문제 해결
  
  * (BOJ 12891) DNA 비밀번호
    
    ![화면 캡처 2022-12-23 143650.png](알고리즘_3DAY_assets/52197456f0b0be23aede8cb2800e88db773055e2.png)
    
    ![화면 캡처 2022-12-23 143717.png](알고리즘_3DAY_assets/29f8d0dd197c78bed610538a4f0111c2141b406f.png)
    
    * O(n) 으로 풀기 위해, 고정된 범위 하나씩 이동하면 체크리스트 비교
    
    ![화면 캡처 2022-12-23 145147.png](알고리즘_3DAY_assets/f7ff4350efcd822f645744e1bc21718fc354f709.png)
    
    ![화면 캡처 2022-12-23 145316.png](알고리즘_3DAY_assets/1e87085b2ff4fbe9c3de1e70818c6c7742c55f7b.png)
    
    ![화면 캡처 2022-12-23 145338.png](알고리즘_3DAY_assets/0be7fc284cdbf03f97538669fac3444033d4fa2d.png)
  
  * (BOJ 11003) 최솟값 찾기 1
    
    ![화면 캡처 2022-12-23 145422.png](알고리즘_3DAY_assets/a85eac7f36c434ef972132548deeded1737d51c6.png)
    
    * O(nlogn) 도 안되므로,  슬라이딩 윈도우와 덱으로 O(n) 접근
    * 빈 덱에, 인덱스와 값을 튜플로 넣어주기
    
    ![화면 캡처 2022-12-23 145459.png](알고리즘_3DAY_assets/08c5d3371d50e566b70813f647e300d5853ebbfe.png)

* 스택과 큐
  
  * (BOJ 1874) 스택으로 수열 만들기
    
    ![화면 캡처 2022-12-23 164554.png](알고리즘_3DAY_assets/7d4d01e65bf0f62a7305a3a224b2345ecfe827b5.png)
    
    ![화면 캡처 2022-12-23 164623.png](알고리즘_3DAY_assets/d05d371d2f39bb78d182dd7f9e5da082dbfdd5a4.png)
    
    ![화면 캡처 2022-12-23 164652.png](알고리즘_3DAY_assets/ce9f7a9f21b48d62acd914cf059b9eb93c403476.png)
    
    ![화면 캡처 2022-12-23 164713.png](알고리즘_3DAY_assets/a258e2aabc9ee5a18e46e8d667b719dc6770b1e8.png)
