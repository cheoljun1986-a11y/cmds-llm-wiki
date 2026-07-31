---
type: raw-source
aliases:
  - Graphify Korean Homepage
  - Graphify 지식 그래프 소개
description: "A Korean-language product overview of Graphify, an open-source skill that converts code, documents, papers, and diagrams into a queryable knowledge graph for AI coding assistants."
author:
  - Codex
model: gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
date ingested: 2026-07-31
tags:
  - raw-source
  - graphify
  - knowledge-graph
  - codebase-understanding
  - research-tooling
source: "https://graphify.net/kr/"
sourceAuthor: "Graphify / Safi Shamsi"
category: Articles
status: ingested
collectionPurpose: "학술 연구 · 논문 — Graphify의 지식 그래프 기반 문헌·코드 분석 방식과 주장된 토큰 효율을 연구 도구 후보로 평가"
captureMethod: "Rendered-text extraction from the public Korean webpage"
captureDate: 2026-07-31
captureLimitations: "Navigation, footer, visual styling, and interactive behavior are omitted. Product and benchmark claims are preserved as publisher claims and have not been independently verified."
---

# Graphify — AI 코딩 어시스턴트를 위한 지식 그래프

> [!info] Source
> 원본 출처: https://graphify.net/kr/
> 캡처일: 2026-07-31
> 아래 `Original Content`는 공개 한국어 페이지의 본문을 렌더링된 텍스트 기준으로 보존한 스냅샷이다.

## Original Content

# Graphify — AI 코딩 어시스턴트를 위한 지식 그래프

Graphify는 코드, 문서, 논문, 다이어그램을 질의 가능한 지식 그래프로 구성해 AI 코딩 어시스턴트가 멀티모달 코드베이스를 이해하도록 돕는 오픈소스 스킬입니다.

`pip install graphifyy`

## Graphify란?

Graphify는 Claude Code, OpenAI Codex, OpenCode 같은 AI 코딩 어시스턴트를 위해 만든 멀티모달 지식 그래프 빌더입니다. Tree-sitter 정적 분석과 LLM 기반 의미 추출을 결합해 소스 코드, 문서, 연구 논문, 다이어그램을 포함한 저장소 전체를 인터랙티브 그래프로 변환하며, 코드가 무엇을 하는지와 왜 그렇게 설계됐는지까지 설명합니다. 프로젝트는 Safi Shamsi가 유지보수하며 MIT 라이선스로 배포됩니다.

- 3.7k+ GitHub Stars
- MIT 라이선스
- 71.5× 토큰 절감률
- Python 3.10+ 런타임

## 핵심 기능

Graphify는 정적 분석, 의미 추출, 그래프 클러스터링을 하나의 스킬로 통합해 어떤 AI 코딩 어시스턴트에서도 호출할 수 있습니다.

### 멀티모달 추출

코드(.py, .js, .go, .java 등), Markdown, PDF, 이미지를 파싱합니다. Tree-sitter는 AST/호출 그래프/주석을 추출하고, LLM은 문서 개념을 추출하며, 비전 모델은 다이어그램을 읽습니다.

### 지식 그래프 구축

추출된 노드와 엣지를 NetworkX 그래프로 통합하고 Leiden 알고리즘으로 의미 커뮤니티를 탐지합니다. 벡터 임베딩이 필요 없습니다.

### 핵심 노드와 이상 연결

시스템 중심의 고차수 "god nodes"를 식별하고, 파일/도메인 간 예상 밖 연결을 표시해 조사 포인트를 제공합니다.

### 인터랙티브 출력

인터랙티브 `graph.html`, 질의 가능한 `graph.json`, 사람이 읽기 쉬운 `GRAPH_REPORT.md` 보고서를 내보냅니다.

### 어시스턴트 연동

`/graphify`, `/graphify query`, `/graphify path`, `/graphify explain` 명령을 제공합니다.

### 보안 기본값

입력 검증을 엄격히 적용합니다: http/https만 허용, 크기/타임아웃 제한, 경로 포함 검증, HTML 이스케이프 처리로 SSRF/주입/XSS 방어.

## 아키텍처 및 파이프라인

Graphify는 다단계 파이프라인 구조입니다. 각 단계가 독립 모듈이라 필요한 부분만 확장할 수 있습니다.

detect — 파일 수집
extract — AST + LLM 노드/엣지
build — NetworkX 그래프 구성
cluster — Leiden 커뮤니티
analyze — 핵심 노드/이상 연결
report — GRAPH_REPORT.md 생성
export — HTML / JSON / Obsidian

보조 모듈로는 URL 수집 `ingest.py`, 의미 캐시 `cache.py`, 입력 검증 `security.py`, 실시간 업데이트 `watch.py`, MCP 서비스 `serve.py`가 있습니다.

## 설치 및 실행

Graphify는 PyPI에서 배포됩니다. 패키지명은 `graphifyy`, CLI 명령은 `graphify`입니다.

```text
# Python 3.10+ 필요
pip install graphifyy && graphify install

# 프로젝트 폴더의 지식 그래프 생성
/graphify ./raw

# 결과물은 graphify-out/
graphify-out/
├── graph.html
├── GRAPH_REPORT.md
├── graph.json
└── cache/
```

Graphify는 LLM을 내장하지 않습니다. 이미 어시스턴트에 설정된 모델 API 키를 사용하며 원본 소스 코드가 아닌 의미 정보만 전송합니다.

## 실전 예제

저장소에는 소규모 라이브러리와 대규모 코드+논문 혼합 코퍼스에 대한 재현 가능한 예제가 포함됩니다.

### httpx (소규모)

HTTP 전송 계층을 모델링한 6개 Python 파일. 결과: 노드 144개, 엣지 330개, 커뮤니티 6개. 핵심 노드: `Client`, `AsyncClient`, `Response`, `Request`. 이상 연결: `DigestAuth → Response`.

### Karpathy 혼합 코퍼스

GPT 프레임워크 저장소 3개 + attention 논문 5편 + 다이어그램 4개(약 52개 파일, 9.2만 단어). 결과: 노드 285개, 엣지 340개, 커뮤니티 53개. 평균 질의 비용 약 1.7k 토큰으로, 단순 방식 123k 대비 71.5배 절감.

## 비교

코드 인텔리전스 인접 오픈소스와 Graphify의 차이점입니다.

| 프로젝트 | 초점 | 강점 | Graphify 대비 한계 |
|---|---|---|---|
| Sourcegraph | 크로스 리포지토리 코드 검색 | 엔터프라이즈급 탐색 | 지식 그래프가 아니며 설계 의미 표현이 제한적 |
| Code2Vec | 함수 단위 임베딩 | 벡터 검색/분류 | 그래프 구조와 멀티모달 입력이 없음 |
| Neo4j | 범용 그래프 DB | 강력한 Cypher 질의 | 코드에서 그래프를 자동 생성하지 않음 |

## 보안, 라이선스, 신뢰성

Graphify는 MIT 라이선스로 배포됩니다. 핵심 의존성 NetworkX(BSD), Tree-sitter(MIT)도 모두 허용적 라이선스입니다. 텔레메트리를 수집하지 않으며, 외부 네트워크 호출은 의미 추출 단계뿐입니다. 이때도 원본 소스 코드는 전송하지 않고 문서 의미 설명만 전송합니다. URL은 http/https로 제한되고, 다운로드 크기/시간 제한, 출력 경로 포함 검증, HTML 이스케이프를 적용해 SSRF/Cypher 주입/XSS를 방어합니다.

## 자주 묻는 질문

### Graphify가 내 코드를 외부 모델로 보내나요?

아니요. Graphify는 문서/다이어그램의 의미 설명만 전송하며 원본 소스 파일은 전송하지 않습니다.

### 어떤 AI 코딩 어시스턴트를 지원하나요?

Claude Code, OpenAI Codex, OpenCode를 기본 지원하며 `skill-*.md` 매니페스트를 제공합니다.

### 얼마나 큰 코드베이스까지 처리할 수 있나요?

Tree-sitter 파싱과 NetworkX 그래프 구축은 규모에 따라 선형적으로 확장됩니다. 약 50만 단어 코퍼스에서도 BFS 서브그래프 질의는 약 2k 토큰 수준을 유지합니다.

### 상업적으로 사용 가능한가요?

가능합니다. Graphify는 MIT 라이선스로 개인/상업 모두 무료입니다.

## Agent Ingest Notes

- 이 페이지는 제품 제작자가 게시한 소개 페이지다. 기능·보안·벤치마크 수치는 독립 검증 결과가 아니라 **publisher claims**로 취급한다.
- 연결된 공식 GitHub 저장소는 코드, 문서, PDF, 이미지 등을 질의 가능한 지식 그래프로 변환하는 프로젝트라는 큰 방향을 뒷받침한다.
- `71.5×` 토큰 절감과 `50만 단어 → 약 2k 토큰` 주장은 실험 조건, 비교 기준, 질의 난이도를 확인하기 전까지 일반화하지 않는다.
- 학술 활용의 핵심 후보는 코드와 논문을 하나의 그래프에 연결하는 [[Multimodal Repository Knowledge Graph]]이며, 평가 절차는 [[Evaluating Graphify for Academic Research]]에 정리한다.
