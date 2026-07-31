---
type: wiki-page
aliases:
  - Graphify Academic Evaluation Guide
  - Graphify 연구 도구 평가
description: "A verification-oriented guide for evaluating Graphify as an academic research tool without treating product-page claims as established evidence."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - guide
  - research-method
  - graphify
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[Graphify]]"
  - "[[Knowledge Graph Query Economy]]"
  - "[[Multimodal Repository Knowledge Graph]]"
confidence: medium
layer: guides
explored: false
claimType: prescriptive
evidenceScope: synthesis-only
verificationStatus: unverified
---

# Evaluating Graphify for Academic Research

## Goal

Graphify를 논문·코드 혼합 코퍼스의 분석 도구로 채택하기 전에 기능, 검색 품질, 비용, 재현성을 검증한다. 제품 홈페이지의 수치를 연구 근거로 바로 사용하지 않는다.

## Minimal Evaluation Protocol

1. 버전과 환경을 고정한다.
2. 정답 관계가 알려진 소규모 코드+논문 코퍼스를 만든다.
3. 노드·엣지 추출의 precision/recall을 사람이 표본 검토한다.
4. 구조 질의, 의미 질의, 경로 질의를 분리한다.
5. 동일 코퍼스에서 키워드 검색과 dense retrieval을 대조군으로 둔다.
6. 그래프 구축·갱신·질의의 시간과 토큰을 모두 측정한다.
7. `graph.json`에서 답변 근거가 원문 위치로 추적되는지 확인한다.

## Acceptance Criteria

- 핵심 관계의 오류율이 연구 목적에 허용 가능한가
- 코드와 논문 사이의 연결이 재현 가능한가
- 답변 품질을 유지하면서 총비용이 감소하는가
- 다른 연구자가 같은 버전과 설정으로 결과를 재현할 수 있는가

> [!warning] Evidence Boundary
> [[Knowledge Graph Query Economy]]의 `71.5×` 수치는 현재 제작자 제공 사례다. 실험 조건을 재현하기 전에는 연구 결과가 아니라 검증 대상 가설로 취급한다.

> [!note] Bias Check
> Counter-argument: 도구 중심 평가가 연구 질문보다 도구의 장점을 과대대표할 수 있다.
> Data gap: 아직 이 볼트에서 Graphify를 설치하거나 평가 코퍼스로 실행하지 않았다.

## Related

- [[MOC-Graph-Based Repository Analysis]]
- [[Static-Semantic Hybrid Extraction]]
- [[Vector-Free Graph Retrieval]]
