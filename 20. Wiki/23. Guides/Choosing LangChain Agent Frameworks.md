---
type: wiki-page
aliases:
  - Choosing LangChain vs LangGraph vs Deep Agents
  - LangChain 프레임워크 선택 가이드
description: "A decision guide for choosing LangChain, LangGraph, or Deep Agents according to workflow control, determinism, autonomy, and project scope."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - guide
  - langchain
  - langgraph
  - deep-agents
  - framework-selection
source:
  - "[[2026-07-31-LangChain-homepage]]"
  - "[[2026-07-31-Q-공정-수율-예측과-LangGraph-적용]]"
related:
  - "[[2026-07-31-Q-공정-수율-예측과-LangGraph-적용]]"
  - "[[서울대 데이터사이언스 - 고급 LLM 및 RAG]]"
confidence: medium
layer: guides
explored: false
claimType: prescriptive
evidenceScope: multi-source-mixed
verificationStatus: unverified
disputed: false
---

# Choosing LangChain Agent Frameworks

## Decision Rule

	- 빠른 Agent Prototype과 기본 Tool 연결이 목표면 [[LangChain]]을 먼저 검토한다.
	- 상태, 승인, 재시도, 명시적 분기와 일정 수준의 결정성이 중요하면 [[LangGraph]]를 검토한다.
	- 목표와 경로가 열린 장기 자율 작업이면 [[Deep Agents]]를 비교한다.
	- Trace, 평가와 배포 운영은 프레임워크와 분리하여 [[LangSmith]] 또는 로컬 대안을 검토한다.

## 현업과제 선택

공정 수율 또는 입고 품질 분석은 데이터 검증과 모델 평가가 결정적이어야 하고, 담당자 승인 지점이 분명하다. 따라서 예측 파이프라인은 일반 Python ML로 유지하고 [[LangGraph]]는 상태형 업무 흐름에만 적용하는 구성이 적합하다.

5주 과제의 최소 범위:

	1. 데이터 Join과 예측 가능성 검증
	2. 기준선 모델과 시간 분할 평가
	3. 결과 설명과 사람 검토
	4. 마지막에 LangGraph로 단계 연결

> [!note] Bias Check
> Counter-argument: 네 단계가 단순하고 재개·분기가 거의 없다면 일반 Python 함수나 DAG가 더 작고 명확할 수 있다.
> Data gap: 실제 과제의 승인 횟수, 실패 복구 요구와 장기 실행 시간이 아직 정해지지 않았다.

## Related

	- [[2026-07-31-Q-공정-수율-예측과-LangGraph-적용]]
	- [[MOC-Agent Engineering Stack]]
