---
type: wiki-page
aliases:
  - Hybrid AST and LLM Extraction
  - 정적·의미 혼합 추출
description: "A hybrid extraction design that combines deterministic syntax analysis for code with model-based semantic interpretation for documents and diagrams."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - static-analysis
  - semantic-extraction
  - tree-sitter
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[Tree-sitter]]"
  - "[[Multimodal Repository Knowledge Graph]]"
  - "[[Graphify]]"
confidence: medium
layer: concepts
explored: false
claimType: definition
evidenceScope: single-source
verificationStatus: unverified
---

# Static-Semantic Hybrid Extraction

## Pattern

구조가 명시적인 코드는 결정론적 파서로, 의미가 비정형적인 문서·다이어그램은 LLM이나 비전 모델로 처리하는 분업 패턴이다. [[Graphify]] 소개에 따르면 코드에서는 [[Tree-sitter]]가 AST·호출 그래프·주석을 추출하고, 문서와 그림에서는 모델이 개념을 추출한다.

## Trade-off

정적 분석은 재현성과 위치 추적성이 높지만 설계 의도를 직접 이해하지 못한다. 모델 기반 의미 추출은 암묵적 연결을 만들 수 있지만 확률적이며 재현성과 근거 추적성이 약하다. 혼합 설계의 핵심은 두 결과를 합치는 것보다 **어떤 엣지가 어느 추출 경로에서 나왔는지 보존하는 것**이다.

> [!note] Bias Check
> Counter-argument: 두 추출 방식을 결합한다고 자동으로 각각의 약점이 상쇄되는 것은 아니다.
> Data gap: 홈페이지는 파이프라인을 설명하지만 추출기별 오류율과 결합 규칙을 제공하지 않는다.

## Related

- [[Multimodal Repository Knowledge Graph]]
- [[Graph-Based Codebase Understanding]]
- [[Evaluating Graphify for Academic Research]]
