---
type: wiki-page
aliases:
  - Agent Engineering Lifecycle
  - 에이전트 엔지니어링 생애주기
description: "A lifecycle that connects agent construction, tracing, evaluation, deployment, human feedback, and iterative improvement."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - concept
  - agent-engineering
  - lifecycle
source:
  - "[[2026-07-31-LangChain-homepage]]"
related:
  - "[[Agent Observability]]"
  - "[[Production Trace Evaluation Loop]]"
  - "[[Durable Agent Execution]]"
confidence: medium
layer: method
explored: false
claimType: mixed
evidenceScope: single-source
verificationStatus: unverified
disputed: false
---

# Agent Engineering Lifecycle

## Overview

에이전트 개발을 프롬프트 작성으로 끝내지 않고 구축, 실행 추적, 평가, 배포, 사람 피드백과 개선의 반복 생애주기로 관리하는 관점이다.

## Lifecycle

	- Build: 문제에 맞는 [[LangChain]], [[LangGraph]] 또는 [[Deep Agents]] 선택
	- Observe: [[Agent Observability]]로 실행 경로와 실패 기록
	- Evaluate: [[Production Trace Evaluation Loop]]로 실제 실패를 테스트로 전환
	- Deploy: [[Durable Agent Execution]]과 사람 협업을 고려
	- Improve: 모델, 도구, Prompt와 분기 규칙을 버전별로 비교

> [!note] Bias Check
> Counter-argument: 제품 플랫폼을 도입하지 않아도 이 생애주기는 일반 로그·테스트·워크플로 도구로 구현할 수 있다.
> Data gap: 과제 규모에서 필요한 최소 운영 수준과 플랫폼 도입 편익을 아직 비교하지 않았다.

## Related

	- [[MOC-Agent Engineering Stack]]
	- [[서울대 데이터사이언스 - 고급 LLM 및 RAG]]
