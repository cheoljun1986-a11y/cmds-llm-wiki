---
type: query-result
aliases:
  - 공정 수율 예측과 LangGraph 적용
  - 특수가스 데이터 기반 현업과제 대안
description: "A project recommendation for predicting semiconductor process yield or incoming gas quality risk from structured manufacturing data, with LangGraph used as the human-in-the-loop orchestration layer rather than the predictive model."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - query-result
  - manufacturing
  - yield-prediction
  - tabular-data
  - langgraph
  - industry-project
query: "현업과제 제안서를 바탕으로 이미지가 아닌 데이터로 공정 수율을 분석하고 LangGraph를 활용할 수 있는가?"
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
  - "[[서울대 데이터사이언스 - 데이터 마이닝]]"
  - "[[서울대 데이터사이언스 - 고급 LLM 및 RAG]]"
  - "[[Temporal Split and Data Leakage]]"
reusableFor:
  - 프로젝트 및 구현
  - 수업 및 코스워크
  - 커리어 및 포트폴리오
confidence: medium
---

# 공정 수율 예측과 LangGraph 적용

## 결론

현재 제안서의 외관 이미지와 실린더 식별정보만으로는 반도체 공정 수율을 계산하거나 예측할 수 없다. 수율의 결과값과 공정 투입 이력이 없기 때문이다.

가스 실린더 또는 가스 Batch가 어느 설비·Chamber·공정 Lot에 사용되었는지 연결하고, 해당 Lot의 수율 또는 품질 결과를 확보할 수 있다면 이미지 없이도 `특수가스 품질·공급 이력 기반 공정 수율 저하 위험 예측` 과제를 수행할 수 있다.

이 연결이 불가능하면 목표를 `공급사·가스 Batch·실린더별 입고 FAIL 위험 및 품질 추세 분석`으로 낮추는 것이 타당하다. 이는 공정 수율이 아니라 입고 품질 수율이다.

LangGraph는 수율을 예측하는 알고리즘이 아니다. 데이터 검증, 모델 실행, 설명 생성, 담당자 검토, 승인 또는 재분석, 보고서 생성을 상태와 이력에 따라 연결하는 오케스트레이션 계층으로 사용하는 것이 적절하다.

## 권장 과제

### 1순위: 특수가스 이력 기반 공정 수율 저하 위험 예측

- 분석 단위: 공정 Lot 또는 설비·Chamber·시간 구간
- 목표변수:
	- 연속형: 최종 Yield %, 불량률, 결함 수
	- 이진형: 기준 수율 미달 여부, 이상 Lot 여부
- 핵심 질문:
	- 특정 공급사·가스 Batch·실린더 이력이 수율 저하와 연관되는가?
	- 수율 저하를 사전에 예측할 수 있는가?
	- 어떤 공정 조건과 가스 속성이 위험을 높이는가?
- 주의: 연관성 분석만으로 가스가 수율 저하의 원인이라고 단정하지 않는다. 설비, 제품, Recipe, 작업조건, 유지보수 등 교란요인을 함께 통제해야 한다.

### 2순위: 입고 품질 수율과 FAIL 위험 예측

- 공정 Lot 연결이 불가능할 때 선택한다.
- 목표변수: 입고 PASS/FAIL, 재촬영 여부, Leak 검사 결과, 공급사 확인 결과
- 산출물: 공급사·Batch·기간별 입고 합격률, FAIL 위험점수, 이상 추세, 재검사 우선순위
- 장점: 현재 제안서의 실린더 ID, 검사일, 제조사, 판정 프로세스와 직접 연결된다.
- 한계: 반도체 제조 공정의 Wafer Yield를 설명하지는 못한다.

## 필요한 최소 데이터

### 가스·공급 데이터

- 실린더 ID, 가스 Batch/Lot, 공급사
- 충전일, 납품일, 사용 시작·종료일
- 순도, 수분, 산소 및 기타 불순물 분석값
- 압력, 충전량, 재사용 횟수, 밸브 사용기간
- 입고검사·Leak 검사·이상조치 결과

### 공정 데이터

- 설비 ID, Chamber ID, 공정 Recipe, 제품·Layer
- 공정 시작·종료 시각과 Lot ID
- 주요 센서·FDC 요약값, Alarm, 유지보수 이력
- 가스 교체·연결 시점과 실린더 또는 Batch 매핑

### 결과 데이터

- Wafer 또는 Lot 단위 Yield
- Defect count/density, Scrap, Rework
- 계측값과 규격 이탈 여부

핵심 Join Key는 `gas_batch 또는 cylinder_id → 사용시간 → equipment/chamber → process_lot → yield_result`이다. 이 연결키가 없으면 1순위 과제는 중단하고 2순위로 전환한다.

## 분석 방법

### 탐색과 기준선

- 공급사·Batch·설비·Recipe·기간별 수율 분포와 결측률을 확인한다.
- 단순 평균 비교와 통계 검정으로 후보 신호를 찾되 인과관계로 해석하지 않는다.
- 회귀 또는 로지스틱 회귀를 해석 가능한 기준선으로 둔다.

### 예측 모델

- 표형 데이터의 1차 후보는 트리 기반 앙상블이다.
- 연속 수율은 회귀, 기준 미달 여부는 분류로 모델링한다.
- 데이터가 시간 순서로 누적되므로 과거 학습·최근 Test의 시간 분할을 적용한다.
- 동일 Lot, 설비, 실린더 또는 가스 Batch가 Train과 Test에 중복되어 누수가 생기지 않도록 Group 분할을 함께 검토한다.
- 평가는 MAE/RMSE와 함께 낮은 수율 Lot의 Recall, PR-AUC, False Negative를 본다.

### 설명과 원인 후보

- Feature importance 또는 SHAP 계열 설명으로 위험 기여요인을 제시한다.
- 설명 결과는 `원인 확정`이 아니라 `조사 우선순위`로 표현한다.
- 설비·Recipe·제품군별 층화 분석과 시간 전후 비교로 교란을 줄인다.

## LangGraph 적용 구조

공식 문서 기준 LangGraph는 장기 실행되는 상태형 워크플로, 체크포인트 기반 재개, 사람의 승인 Interrupt, 결정적 단계와 LLM 단계를 한 그래프에 결합하는 데 적합하다.

권장 그래프:

`요청 접수 → 데이터 스키마 검사 → Join 가능성 판정 → 데이터 품질 검사 → 분석 경로 선택 → 모델 실행 → 성능 게이트 → 설명 생성 → 품질담당자 검토 Interrupt → 승인/재분석 분기 → 보고서 저장`

- 결정적 노드:
	- 데이터 로딩과 스키마 검사
	- Feature 생성
	- 학습·평가
	- 성능 기준 판정
- LLM 노드:
	- 데이터 품질 이슈 요약
	- 모델 설명의 현업 언어 변환
	- 조사 질문과 보고서 초안 생성
- Human-in-the-loop 노드:
	- Join 매핑 오류 승인
	- 수율 저하 원인 후보 검토
	- 외부 공유 전 보고서 승인

예측모델의 학습·추론은 일반 Python ML 파이프라인이 담당하고, LangGraph는 실행 상태와 승인 흐름을 관리한다. 5주 PoC에서는 LangGraph를 마지막 통합 단계에 넣고, 먼저 데이터 Join과 예측 가능성을 입증해야 한다.

## 5주 PoC

1주차:
	- 데이터 사전과 Join Key 검증
	- 공정 수율 연결 가능 여부를 Go/No-Go로 판정

2주차:
	- 결측·중복·시간정합성 점검
	- 공급사·Batch·설비·Recipe별 EDA

3주차:
	- 회귀·로지스틱 기준선과 트리 앙상블 비교
	- 시간·Group 분할 평가

4주차:
	- 저수율 Recall 중심 오류분석
	- Feature importance/SHAP와 현업 검토

5주차:
	- LangGraph로 검증·분석·승인·보고 흐름 연결
	- 최근 기간 독립 Test와 최종 데모

## 성공 기준과 중단 조건

- 데이터 성공 기준:
	- 공정 Lot의 충분한 비율이 가스 Batch 및 설비 이력과 정확히 연결됨
	- 최근 기간 Test에 저수율 또는 FAIL 사례가 충분히 존재함
- 모델 성공 기준:
	- 단순 기준선보다 최근 기간 Test에서 개선
	- 낮은 수율 Lot 또는 FAIL의 Recall을 우선 평가
- 업무 성공 기준:
	- 분석 결과가 조사 우선순위 또는 재검사 결정에 사용 가능함
	- LangGraph 재실행·승인 이력이 남음
- 중단 조건:
	- 핵심 Join Key가 없거나 연결률이 낮으면 Wafer Yield 예측 주장을 중단
	- 결과 라벨이 없으면 지도학습을 중단하고 품질 추세·이상탐지 또는 데이터 기반 구축 과제로 전환

## 위키 자산 활용

- [[서울대 데이터사이언스 - 데이터 마이닝]]: 회귀, 로지스틱 회귀, 앙상블, 결측치 처리, 통계적 추론의 기준선
- [[Temporal Split and Data Leakage]]: 시간 분할과 동일 개체·Batch의 Group 누수 방지
- [[서울대 데이터사이언스 - 고급 LLM 및 RAG]]: LangGraph와 Agent Engineering의 구현 학습
- [[서울대 데이터사이언스 - 파이썬과 데이터 시각화]]: 공급사·Batch·설비별 수율 추세와 오류분석 시각화

> [!warning] Evidence Boundary
>	현재 위키의 데이터 마이닝 및 고급 LLM 가이드는 강의 파일명 기반의 `unverified scaffold`다. 실제 구현 전에 관련 강의 본문과 공식 LangGraph 문서를 다시 확인해야 한다.

> [!question] Open Question
>	가스 실린더 또는 Batch와 공정 Lot·설비·Chamber·수율 결과를 연결하는 키가 실제 사내 데이터에 존재하는가?

## External Reference

- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangGraph Functional API and human-in-the-loop interrupts](https://docs.langchain.com/oss/python/langgraph/functional-api)

## Reuse

이 결과는 프로젝트 및 구현, 수업 및 코스워크, 커리어 및 포트폴리오에 재사용 가능하다. 현업 데이터 문제를 통계·ML·LLM 오케스트레이션으로 분리해 설명하는 사례가 되기 때문이다.
