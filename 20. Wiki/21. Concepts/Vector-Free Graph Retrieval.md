---
type: wiki-page
aliases:
  - Embedding-Free Graph Retrieval
  - 벡터 없는 그래프 검색
description: "A retrieval approach that answers questions by traversing explicit graph topology instead of relying on embedding similarity and a vector store."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - retrieval
  - knowledge-graph
  - graph-traversal
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[Graph-Based Codebase Understanding]]"
  - "[[Knowledge Graph Query Economy]]"
  - "[[RAG vs Compiled Wiki]]"
confidence: medium
layer: concepts
explored: false
claimType: theoretical
evidenceScope: single-source
verificationStatus: unverified
---

# Vector-Free Graph Retrieval

## Definition

임베딩 유사도와 벡터 저장소 대신 명시적 그래프의 이웃, 경로, 커뮤니티를 탐색해 관련 정보를 좁히는 방식이다. [[Graphify]]는 NetworkX 그래프와 Leiden 커뮤니티 탐지를 사용하며 벡터 임베딩이 필요 없다고 주장한다.

## Comparison

벡터 검색은 표현이 다른 의미적 유사성을 찾는 데 강하다. 그래프 탐색은 연결 경로와 관계 유형을 설명하기 쉽다. 따라서 둘은 완전한 대체 관계라기보다 질의 종류에 따라 강점이 다르다. 구조적 질문에는 그래프가, 느슨한 주제 유사성에는 임베딩이 더 적합할 수 있다.

> [!note] Bias Check
> Counter-argument: “벡터가 필요 없다”는 구현 선택이지 모든 검색 문제에서 벡터 검색보다 낫다는 증거가 아니다.
> Data gap: 동일 코퍼스·동일 질의에서 그래프 검색과 dense retrieval을 비교한 독립 결과가 없다.

## Related

- [[Knowledge Graph Query Economy]]
- [[Graph-Based Codebase Understanding]]
- [[RAG vs Compiled Wiki]]
