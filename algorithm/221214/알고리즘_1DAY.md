# 알고리즘_1DAY

* 시간복잡도
  
  ![화면 캡처 2022-12-14 092229.png](알고리즘_1DAY_assets/48bffeb711aa4bf47e3377a28913119078d61bd6.png)
  
  * 빅-오로 계산
  
  * 1초 == 2000만 번
  
  * (BOJ 2750) 수 정렬하기
    
    <img title="" src="알고리즘_1DAY_assets/218857fde7f1947412caee673727b5dfa1535e85.png" alt="화면 캡처 2022-12-14 092714.png" width="393">
    
    * 버블정렬은 n2이므로 1백만**2 > 4천만
      
      * 부적합
    
    * 병합정렬은 nlogn 이므로 1백만log1백만 == 2천만 < 4천만
      
      * 적합
  
  * N == 3N 은 N으로 동일하다. 시간 낭비 하지말자

* 배열과 리스트
  
  * 파이썬에선 구분안한다
  
  * (BOJ 11720) 숫자의 합 구하기
    
    <img title="" src="알고리즘_1DAY_assets/c421d1bfb0d9cca4f28efac188b4726269a1cf60.png" alt="화면 캡처 2022-12-14 093604.png" width="423" data-align="inline">
    
    <img title="" src="알고리즘_1DAY_assets/dcfa0903f698fd9c5ddfd61bf8ac6d6226eb23c3.png" alt="화면 캡처 2022-12-14 093749.png" width="427">
  
  * (BOJ 1546) 평균 구하기
    
    <img src="알고리즘_1DAY_assets/7e929ab6dbf721b3250500b850ffdb8e7fa795af.png" title="" alt="화면 캡처 2022-12-14 093910.png" width="455">
    
    <img src="알고리즘_1DAY_assets/c2ca0d13e73a3f1e5f5f344ab98c9e1cfa9a1954.png" title="" alt="화면 캡처 2022-12-14 094209.png" width="446">

* 구간 합
  
  * 합 배열을 이용한 시간 복잡도 줄이기 위한 특수한 목적의 알고리즘!!! 중요하다
    
    * 합 배열
      
      <img title="" src="알고리즘_1DAY_assets/8f6e82c21d4382743fd78630096b91d8f1732ec0.png" alt="화면 캡처 2022-12-14 094615.png" width="338">
      
      * S[i] = S[i-1] + A[i]
      
      * 구간 합으로 사용 법 : S[j] - S[i-1]
  
  * (BOJ 11659) 구간 합 구하기 1
    
    <img src="알고리즘_1DAY_assets/3fc6cc20a030fd02b98aa18df531ca1580659f62.png" title="" alt="화면 캡처 2022-12-14 095119.png" width="475">
    
    - 10만*10만은 0.5초로 턱없이 부족하니 구간 합 사용
    
    - 합 배열을 만들어 모든 경우 적용
    
    ![화면 캡처 2022-12-14 100941.png](알고리즘_1DAY_assets/3a170dd139453f51241dc05f03c499c260a438c8.png)
  
  * (BOJ 11660) 구간 합 구하기 2
    
    ![화면 캡처 2022-12-14 101202.png](알고리즘_1DAY_assets/461e1038c5d3520d79aa6c729b9ddcb29a90ba6f.png)
    
    ![화면 캡처 2022-12-14 101222.png](알고리즘_1DAY_assets/823b09e4232bbab91f05099333a4418242c4d61f.png)
    
    * 1000 * 1000 * 10만이므로 1초 무리니 구간 합 사용
    
    ![화면 캡처 2022-12-14 102806.png](알고리즘_1DAY_assets/fc6915d46209c5dd0825bc36861d6277fccf2e50.png)
  
  * (BOJ 10986) 나머지 합 구하기
    
    ![화면 캡처 2022-12-14 102959.png](알고리즘_1DAY_assets/0d26fd664a8e7bb3423675a29608c8a815ee8b51.png)
    
    - 문제 오류있음,, 106이 아니라 10**6 승임
    
    - 너무 값이 크므로 배열 합을 이용해 구간 합 일일히 구하면 시간초과 100퍼센트 해결법은 참신하게 풀기
      
      - 배열 합 M으로 나누어 최신화 하고, 같은 숫자 조합으로 갯수
    
    ![화면 캡처 2022-12-14 111142.png](알고리즘_1DAY_assets/51b2e779f5f0b0cc460024cfb20415edaae5ff2d.png)
    
    ![화면 캡처 2022-12-14 111215.png](알고리즘_1DAY_assets/e3aec33e7e7c901df551e7f86281ea447bc98dd3.png)
