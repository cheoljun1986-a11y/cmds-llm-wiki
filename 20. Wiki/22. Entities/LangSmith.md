---
type: wiki-page
aliases:
  - langsmith
  - LangSmith Agent Engineering Platform
description: "An agent engineering platform positioned around observability, evaluation, deployment, and iterative improvement from production traces."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - entity
  - langsmith
  - observability
  - evaluation
  - deployment
source:
  - "[[2026-07-31-LangChain-homepage]]"
related:
  - "[[Agent Observability]]"
  - "[[Production Trace Evaluation Loop]]"
  - "[[Durable Agent Execution]]"
confidence: medium
layer: entities
explored: false
claimType: definition
evidenceScope: single-source
verificationStatus: unverified
disputed: false
---

# LangSmith

## Overview

홈페이지는 LangSmith를 에이전트의 관측, 평가와 배포를 묶는 Agent Engineering Platform으로 설명한다. 특정 프레임워크에 종속되지 않고 여러 언어 SDK 또는 에이전트 스택과 통합할 수 있다고 주장한다.

## 기능 축

	- [[Agent Observability]]: 실행을 구조화된 단계 타임라인으로 추적
	- [[Production Trace Evaluation Loop]]: 운영 Trace를 테스트 사례와 평가 데이터로 전환
	- [[Durable Agent Execution]]: 장기 실행, 대화 Thread, 체크포인트와 사람 협업 지원

## 과제 활용

과제에서는 LangSmith를 필수 구성요소로 두기보다 LangGraph 워크플로의 Trace와 평가가 필요할 때 선택하는 운영 도구로 분리한다. 로컬·사내 환경과 데이터 반출 제약을 먼저 확인해야 한다.

> [!note] Bias Check
> Counter-argument: 5주 과제에서는 로컬 로그와 간단한 평가 테이블만으로도 충분할 수 있으며, 별도 플랫폼 도입이 과도할 수 있다.
> Data gap: 라이선스, 배포 위치, 사내 보안 적합성, 비용과 데이터 보존 정책을 아직 확인하지 않았다.

## Related

	- [[Agent Engineering Lifecycle]]
	- [[MOC-Agent Engineering Stack]]
