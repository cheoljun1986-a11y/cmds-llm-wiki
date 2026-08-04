---
type: wiki-page
aliases:
  - langgraph
  - LangGraph Framework
description: "A low-level orchestration framework positioned for reliable production agents that require explicit control and some determinism."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - entity
  - langgraph
  - orchestration
  - agent-framework
source:
  - "[[2026-07-31-LangChain-homepage]]"
related:
  - "[[LangChain]]"
  - "[[Durable Agent Execution]]"
  - "[[2026-07-31-Q-공정-수율-예측과-LangGraph-적용]]"
confidence: medium
layer: entities
explored: false
claimType: definition
evidenceScope: single-source
verificationStatus: unverified
disputed: false
---

# LangGraph

## Overview

LangChain 홈페이지는 LangGraph를 낮은 수준의 제어가 필요하고 일정 수준의 결정성을 요구하는 신뢰성 중심 에이전트용 프레임워크로 포지셔닝한다.

## 현업과제 적용

[[2026-07-31-Q-공정-수율-예측과-LangGraph-적용]]에서는 LangGraph를 수율 예측모델 자체가 아니라 데이터 검사, 분석 경로 선택, 모델 실행, 담당자 승인, 재분석과 보고서 저장을 연결하는 상태형 오케스트레이션 계층으로 배치한다.

	- 예측: 회귀·분류·이상탐지 모델이 담당
	- 오케스트레이션: LangGraph가 단계, 상태, 분기와 사람의 검토를 담당
	- 관측·평가: 필요하면 [[LangSmith]] 계열 기능을 별도로 검토

> [!warning] Evidence Boundary
>	홈페이지는 제품의 방향만 제시한다. API, 체크포인트 저장소, 배포 방식과 운영 제약은 공식 문서와 실습으로 확인해야 한다.

## Related

	- [[Durable Agent Execution]]
	- [[Choosing LangChain Agent Frameworks]]
	- [[서울대 데이터사이언스 - 고급 LLM 및 RAG]]
