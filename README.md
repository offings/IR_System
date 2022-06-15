## 정보 검색 시스템(IR System)
## 프로젝트 개발 배경
* 위키백과 기반 정보 검색 엔진 개발을 통한 자연어 처리 학습
* 자연어 처리에 필요한 모든 단계를 Python으로 직접 구현

## 프로젝트 개발 목표
수업 시간에 배운 자연어 처리 모든 과정을 Python을 이용해 구현해 보고, Query가 주어졌을 때 Query와 유사한 Document 5개를 출력한다.

## 프로젝트 개발 내용
* 형태소 분석에 사용하는 조사 리스트 구현
* Document에서 공백 단위로 토큰화 진행 및 조사 분리
* Term을 Inverted Index 형태로 저장
* 2개의 Term을 묶어 Bigram List를 만들고 Inverted Index 형태로 저장
* Term Frequency와 Document Frequency 계산
* Document Length Normalization 진행
* Query와 Document 사이 Score를 계산하고 상위 Rank 표시

## 프로젝트 구현 결과
![정보검색](https://user-images.githubusercontent.com/39369255/173773104-6b5f5e69-b429-41b6-acec-b8471cb50cc7.png)

