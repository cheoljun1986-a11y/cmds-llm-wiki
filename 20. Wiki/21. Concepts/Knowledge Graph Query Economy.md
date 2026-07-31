---
type: wiki-page
aliases:
  - Graph-Scoped Context Economy
  - 지식 그래프 질의 경제성
description: "The proposed reduction in model context cost achieved by querying a scoped subgraph instead of sending or rereading an entire corpus."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - token-economy
  - context-engineering
  - knowledge-graph
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[Vector-Free Graph Retrieval]]"
  - "[[LLM Wiki Token Optimization Strategies]]"
  - "[[Cohort Token Economy]]"
confidence: low
layer: concepts
explored: false
claimType: empirical
evidenceScope: single-source
verificationStatus: unverified
---

# Knowledge Graph Query Economy

## Claim

전체 코퍼스를 다시 읽는 대신 관련 서브그래프만 모델 컨텍스트에 넣어 질의 비용을 줄인다는 아이디어다. Graphify 홈페이지는 Karpathy 혼합 코퍼스에서 평균 질의 비용이 약 1.7k 토큰이었고 단순 방식의 123k 토큰보다 71.5배 적었다고 주장한다.

## Required Verification

이 수치를 연구에 인용하려면 최소한 다음을 확인해야 한다.

- “단순 방식”의 정확한 정의
- 질의 집합과 난이도
- 그래프 구축 비용의 포함 여부
- 검색 실패와 답변 품질
- 반복 실험 및 분산

현재는 제작자 제공 단일 사례이므로 `confidence: low`다.

> [!note] Bias Check
> Counter-argument: 질의 단계 토큰이 줄어도 그래프 구축·갱신 비용과 검색 누락 비용을 포함하면 총비용 우위가 달라질 수 있다.
> Data gap: 재현 스크립트와 원시 측정값을 이 ingest에서 검증하지 않았다.

## Related

- [[Vector-Free Graph Retrieval]]
- [[LLM Wiki Token Optimization Strategies]]
- [[Evaluating Graphify for Academic Research]]
