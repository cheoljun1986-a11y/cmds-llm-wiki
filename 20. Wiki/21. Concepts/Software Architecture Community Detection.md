---
type: wiki-page
aliases:
  - Graph Community Detection for Codebases
  - 소프트웨어 아키텍처 커뮤니티 탐지
description: "The use of graph community-detection algorithms to identify densely connected subsystems and architectural regions in a repository knowledge graph."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - community-detection
  - software-architecture
  - leiden
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[Graph-Based Codebase Understanding]]"
  - "[[Graphify]]"
confidence: medium
layer: concepts
explored: false
claimType: theoretical
evidenceScope: single-source
verificationStatus: unverified
---

# Software Architecture Community Detection

## Definition

저장소 지식 그래프에서 내부 연결이 조밀하고 외부 연결이 상대적으로 적은 노드 집단을 찾아 잠재적 서브시스템으로 해석하는 방법이다. [[Graphify]]는 Leiden 알고리즘으로 의미 커뮤니티를 탐지한다고 설명한다.

## Interpretation Risk

탐지된 커뮤니티는 실제 모듈 경계와 일치할 수도 있지만, 추출된 엣지 종류와 밀도에 의해 만들어진 통계적 묶음일 뿐이다. “커뮤니티”를 곧바로 “아키텍처”로 부르면 순환 의존성, 유틸리티 허브, 생성 코드 같은 교란 요인을 놓칠 수 있다.

> [!note] Bias Check
> Counter-argument: 그래프 군집은 아키텍처 이해의 보조 지표이지 설계 의도를 직접 복원하는 방법이 아니다.
> Data gap: 알려진 모듈 경계와 탐지 커뮤니티의 일치도를 측정한 결과가 현재 소스에 없다.

## Related

- [[Graph-Based Codebase Understanding]]
- [[Knowledge Graph Query Economy]]
- [[Evaluating Graphify for Academic Research]]
