---
type: moc
aliases:
  - Agent Engineering Stack
  - LangChain Ecosystem MOC
description: "A map of the LangChain agent-engineering ecosystem, connecting framework choice, observability, evaluation, durable execution, and manufacturing-coursework application."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - moc
  - agent-engineering
  - langchain
  - langgraph
  - coursework
topic: Agent Engineering Stack
source:
  - "[[2026-07-31-LangChain-homepage]]"
related:
  - "[[서울대 데이터사이언스 - 고급 LLM 및 RAG]]"
  - "[[2026-07-31-Q-공정-수율-예측과-LangGraph-적용]]"
confidence: medium
explored: false
verificationStatus: unverified
---

# MOC — Agent Engineering Stack

## Frameworks

	- [[LangChain]] — 빠른 Agent 시작
	- [[LangGraph]] — 명시적 상태·분기와 낮은 수준의 제어
	- [[Deep Agents]] — 개방형 장기 자율 작업
	- [[Choosing LangChain Agent Frameworks]] — 과제 형태에 따른 선택 기준

## Operations

	- [[LangSmith]] — 관측·평가·배포를 묶는 제품 플랫폼
	- [[Agent Observability]] — 단계별 실행 Trace
	- [[Production Trace Evaluation Loop]] — 운영 실패를 테스트로 전환
	- [[Durable Agent Execution]] — 체크포인트, 중단과 재개
	- [[Agent Engineering Lifecycle]] — 구축부터 개선까지의 반복 관리

## Coursework Path

	1. [[서울대 데이터사이언스 - 고급 LLM 및 RAG]]에서 기본 API와 실습 확인
	2. [[Choosing LangChain Agent Frameworks]]로 과제 요구와 프레임워크 매칭
	3. [[2026-07-31-Q-공정-수율-예측과-LangGraph-적용]]의 데이터·모델·승인 분리 적용
	4. 최근 기간 Test와 실패 Trace를 [[Production Trace Evaluation Loop]]로 관리

> [!note] Bias Check
> Counter-argument: 홈페이지의 제품 분류는 공급자 관점이며, 다른 워크플로·관측 도구와의 비교가 없다.
> Data gap: 강의 실습 결과, 공식 API 문서, 라이선스, 보안과 비용 검증이 필요하다.
