---
type: moc
aliases:
  - Graph-Based Repository Analysis MOC
  - 그래프 기반 저장소 분석 MOC
description: "A map of content connecting Graphify, hybrid extraction, multimodal repository graphs, graph retrieval, community detection, query economy, and academic evaluation."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - moc
  - knowledge-graph
  - research-tooling
topic: 그래프 기반 저장소 분석
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[MOC-Knowledge Management]]"
  - "[[Graphify]]"
---

# MOC — Graph-Based Repository Analysis

코드, 문서, 논문, 다이어그램을 하나의 구조적 그래프로 분석하는 지식 묶음이다. 현재 출발점은 Graphify 제작자의 한국어 소개 페이지 한 건이므로 기능 범위와 성능 주장을 구분해 읽는다.

## 1. 도구

- [[Graphify]] — 저장소를 질의 가능한 지식 그래프로 변환하는 오픈소스 도구.
- [[Tree-sitter]] — 코드 AST와 관계를 추출하는 정적 분석 구성요소.

## 2. 표현과 추출

- [[Graph-Based Codebase Understanding]] — 코드베이스를 노드·엣지 구조로 이해하는 기본 관점.
- [[Multimodal Repository Knowledge Graph]] — 코드·문서·논문·그림을 하나의 그래프에 통합.
- [[Static-Semantic Hybrid Extraction]] — 코드에는 정적 분석, 비정형 자료에는 모델 기반 의미 추출을 사용하는 분업.

## 3. 분석과 검색

- [[Vector-Free Graph Retrieval]] — 임베딩 대신 그래프 경로와 이웃을 이용하는 검색.
- [[Software Architecture Community Detection]] — 그래프 커뮤니티를 잠재적 서브시스템으로 해석.
- [[Knowledge Graph Query Economy]] — 관련 서브그래프만 읽어 컨텍스트 비용을 낮춘다는 가설.

## 4. 연구 적용

- [[Evaluating Graphify for Academic Research]] — 제품 주장과 검증된 연구 근거를 분리하는 평가 절차.

> [!question] Open Question
> 동일한 코드+논문 코퍼스에서 Graphify의 그래프 질의가 키워드 검색과 dense retrieval보다 어떤 질의 유형에서 우수하며, 그래프 구축 비용까지 포함한 총비용은 어떻게 달라지는가?

> [!note] Bias Check
> Counter-argument: 이 묶음은 Graphify가 제시한 문제 정의를 중심으로 만들어져 그래프 접근에 유리한 평가 프레임을 가질 수 있다.
> Data gap: 독립 논문, 공식 기술 문서의 버전 고정 검토, 로컬 재현 실험이 아직 없다.

## Related

- [[MOC-Knowledge Management]]
- [[LLM Wiki Token Optimization Strategies]]
- [[RAG vs Compiled Wiki]]
