---
type: wiki-page
aliases:
  - Graphify-Labs Graphify
  - graphifyy
description: "An open-source tool and agent skill that converts code, documents, papers, and diagrams into a queryable repository knowledge graph."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - entity
  - graphify
  - developer-tool
source:
  - "[[2026-07-31-Graphify-Korean-Homepage]]"
related:
  - "[[Graph-Based Codebase Understanding]]"
  - "[[Tree-sitter]]"
  - "[[Multimodal Repository Knowledge Graph]]"
confidence: medium
layer: entities
explored: false
claimType: mixed
evidenceScope: single-source
verificationStatus: unverified
---

# Graphify

## Overview

Graphify는 코드, 문서, 논문, 다이어그램을 질의 가능한 지식 그래프로 변환하는 오픈소스 도구이자 AI 코딩 어시스턴트용 스킬이다. PyPI 패키지명은 `graphifyy`, CLI 명령은 `graphify`다.

## Pipeline

홈페이지가 설명하는 주요 단계는 파일 탐지, [[Tree-sitter]] 기반 코드 구조 추출, 모델 기반 의미 추출, NetworkX 그래프 구축, Leiden 커뮤니티 탐지, 분석·보고·내보내기다. 출력물은 `graph.html`, `graph.json`, `GRAPH_REPORT.md`로 구성된다.

## Research Status

도구의 존재와 공개 저장소는 확인되지만, 홈페이지의 토큰 절감·확장성·보안 주장은 독립 검증되지 않았다. 논문에서 도구를 평가하거나 인용할 때는 [[Evaluating Graphify for Academic Research]]의 검증 절차를 적용한다.

> [!note] Bias Check
> Counter-argument: 프로젝트 설명은 기능 범위를 보여주지만 실제 정확도와 총비용을 입증하지 않는다.
> Data gap: 버전 고정 실행, 재현 벤치마크, 보안 코드 감사가 수행되지 않았다.

## Related

- [[MOC-Graph-Based Repository Analysis]]
- [[Static-Semantic Hybrid Extraction]]
- [[Knowledge Graph Query Economy]]
