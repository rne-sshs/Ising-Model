Ising-Model
========
2022 SSHS R&E 

* 김선웅(seonu)
* 이지후(numbering)
* 박세진(exabyte)
* 정현우(andy)

내용
--------

### Ising-Model  
각 분자의 스핀은 +1, -1이 가능.  
분자 n개를 선택하여 목적 함수를 최대화하는 것이 목적.
![image](https://user-images.githubusercontent.com/35063338/170424912-e9d66890-6669-4d1a-9bf8-bdf7cb886906.png)

### Input
남자와 여자를 좌표평면의 점으로 표현한 후, 남자와 여자 사이의 만족도를 유클리드 거리로 설정.  
<img src="https://user-images.githubusercontent.com/35063338/170417792-c08cb4cb-4052-4e70-88ea-d40a5f5f572b.png" width="300" height="200"/>

### Process
Sum-Product Belief Propagation을 Ising Model에 적용.  
![image](https://user-images.githubusercontent.com/35063338/170425695-a6264f11-66da-4f1c-9417-d183302b6460.png)  
수렴하면 고정된 i에 대하여 <img src="https://user-images.githubusercontent.com/35063338/170426276-316293bb-2f70-4977-abab-8c6853b83b9d.png" width="90" height="20"/>의 값이 양수가 되는 j와 연결

### Result
![image](https://user-images.githubusercontent.com/35063338/170419394-af59ed98-cf0a-4415-b140-668ba7679efd.png)  
충분히 작은 T에서 Max-Sum과 정확히 같은 결과가 나옴.

### Temperature
식에서의 T로, 입자계의 온도를 말한다.  
T가 작을수록 더 정확한 결과가 나오지만, 너무 작으면 연산이 어렵다.  

### Graph of Temperature
코드를 바탕으로 T에 따른 수렴할 때까지 실행 횟수, 선택 횟수에 대한 데이터를 얻고 그래프로 그린다. (100개의 데이터 셋에 대한 평균으로 구한다.)  
1. n=20  
![image](https://user-images.githubusercontent.com/35063338/170430002-e2277c7b-e12a-4f01-91b2-cc409a455dfe.png)
2. n=50
![image](https://user-images.githubusercontent.com/35063338/170428051-2ccaff07-74f1-4331-ab80-262952be8e48.png)
3. n=100
![image](https://user-images.githubusercontent.com/35063338/170427902-0f09bad5-2367-489d-8185-ce10abbc4877.png)
