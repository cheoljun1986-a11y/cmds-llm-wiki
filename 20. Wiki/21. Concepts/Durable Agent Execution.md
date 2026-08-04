---
type: wiki-page
aliases:
  - Durable Agent Execution
  - 지속 가능한 에이전트 실행
  - Durable Checkpointing
description: "A long-running execution pattern that persists workflow state so agent work can survive interruption, await human input, and resume."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - concept
  - durable-execution
  - checkpointing
  - human-in-the-loop
source:
  - "[[2026-07-31-LangChain-homepage]]"
related:
  - "[[LangGraph]]"
  - "[[LangSmith]]"
  - "[[Human-in-the-Loop Inspection]]"
confidence: medium
layer: method
explored: false
claimType: definition
evidenceScope: single-source
verificationStatus: unverified
disputed: false
---

# Durable Agent Execution

## Overview

장기 실행 워크플로가 중단되거나 사람의 결정을 기다려야 할 때 현재 상태를 체크포인트로 보존하고 나중에 이어서 실행하는 패턴이다.

## 제조 분석 적용

	- 데이터 검증 실패 시 수정 요청 상태로 정지
	- 품질담당자의 원인 후보 검토를 기다림
	- 승인 후 다음 보고 단계부터 재개
	- 중간 모델 결과와 입력 버전을 연결하여 재현성 유지

이는 [[Human-in-the-Loop Inspection]]의 사람 확정 구조를 에이전트 실행 상태까지 확장한 것으로 볼 수 있다.

> [!warning] Evidence Boundary
>	홈페이지는 메모리, 대화 Thread와 체크포인트 지원을 주장하지만 저장소 구성과 장애 복구 보장은 별도 문서 검증이 필요하다.

## Related

	- [[LangGraph]]
	- [[Agent Engineering Lifecycle]]
