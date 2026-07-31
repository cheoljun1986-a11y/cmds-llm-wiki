---
type: wiki-page
aliases:
  - Multimodal Codebase Graph
  - 멀티모달 저장소 지식 그래프
description: "A shared graph representation that connects source code, prose documents, research papers, and diagrams within one repository-level analytical surface."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - multimodal
  - knowledge-graph
  - research-tooling
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[Graph-Based Codebase Understanding]]"
  - "[[Static-Semantic Hybrid Extraction]]"
  - "[[Graphify]]"
confidence: medium
layer: concepts
explored: false
claimType: definition
evidenceScope: single-source
verificationStatus: unverified
---

# Multimodal Repository Knowledge Graph

## Definition

코드, Markdown 문서, PDF 논문, 이미지·다이어그램처럼 형식이 다른 자료를 하나의 노드·엣지 공간에 통합한 그래프다. 목적은 자료 유형별 검색 결과를 나열하는 데서 그치지 않고, 코드 구현과 문서의 설계 이유, 논문의 이론적 근거 사이를 연결하는 것이다.

## Extraction Boundary

각 형식은 같은 추출기로 처리되지 않는다. [[Tree-sitter]] 같은 정적 분석기는 코드 구조를, LLM은 문서 개념을, 비전 모델은 다이어그램 의미를 맡는다. 이 때문에 [[Static-Semantic Hybrid Extraction]]은 멀티모달 그래프의 전제다.

## Academic Use

논문과 재현 코드를 같은 그래프에 넣으면 “논문의 어떤 개념이 어느 구현 요소와 연결되는가”를 탐색할 수 있다. 그러나 연결이 원문에서 명시된 것인지 모델이 추론한 것인지 구분되지 않으면 인용 근거로 사용하기 어렵다.

> [!note] Bias Check
> Counter-argument: 서로 다른 추출기의 오류가 하나의 그래프에서 결합되면 단일 모달 분석보다 오류 전파가 커질 수 있다.
> Data gap: Graphify 소개 페이지는 지원 형식을 제시하지만 모달별 정확도나 정렬 성능은 보고하지 않는다.

## Related

- [[Graph-Based Codebase Understanding]]
- [[Static-Semantic Hybrid Extraction]]
- [[Knowledge Graph Query Economy]]
