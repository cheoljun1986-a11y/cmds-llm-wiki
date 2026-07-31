---
type: moc
aliases:
  - Wiki Index
  - Master Index
description: "Master index of the LLM Wiki. Central navigation hub listing all Wiki pages organized by category (Concepts, Entities, Guides, Maps, Questions). Updated automatically on every ingest operation."
author:
  - "[[cheoljun1986]]"
  - Codex
model:
  - claude-opus-5
  - gpt-5.5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - index
  - moc
  - system
status: active
---

# 📖 LLM Wiki — Master Index

> **Architecture**: Karpathy LLM Wiki Pattern
> Raw Sources → **LLM Compiler** → This Wiki

이 볼트는 LLM 이 직접 작성하고 관리하는 **persistent knowledge wiki** 입니다.
매번 query 마다 재합성하지 않고, 한 번 컴파일된 지식이 계속 성장합니다.

> [!info] 운영 설정
> **Mode A (단독 운영)** · 사용자: cheoljun1986 · 온보딩 2026-07-31
> 재활용 축 4 개 — 학술 연구 · 논문 / 수업 · 코스워크 / 프로젝트 · 구현 / 커리어 · 포트폴리오 ([[Core Context]] §2)

---

## 📊 Stats

*(2026-07-31 기준 실측)*

| Metric | Count |
|--------|-------|
| Raw Sources | 13 |
| Wiki Pages | 48 |
| — Concepts | 23 |
| — Entities | 7 |
| — Guides | 13 |
| — MOCs | 5 |
| Research Questions | 0 |
| Queries | 0 |
| Paper Analyses | 0 |
| Inbox (미처리) | 0 |

> *Stats 는 `/ingest` 실행 시 갱신됩니다. `/status` 로 언제든 실측할 수 있습니다.*

---

## 🗂 Wiki Pages

현재 네 개의 지식 클러스터가 있습니다.

- **🛠 볼트 운영** — 키트에 동봉된 시드 페이지. Karpathy 의 LLM Wiki 원문을 ingest 한 결과로, 이 볼트의 사용법 자체를 설명하는 메타 지식층.
- **🔍 외관 이상탐지** — 2026-07-31 첫 도메인 ingest. [[MOC-Visual Anomaly Detection]] 에서 전체 구조를 볼 수 있습니다.
- **🕸 그래프 기반 저장소 분석** — 코드·문서·논문을 지식 그래프로 연결하는 접근과 Graphify의 연구 도구 적합성. [[MOC-Graph-Based Repository Analysis]] 에서 전체 구조를 볼 수 있습니다.
- **🎓 서울대학교 데이터사이언스 코스워크** — 9개 과목·306개 혼합형 강의 파일의 점진형 학습 지도. [[MOC-서울대학교 데이터사이언스 코스워크]] 에서 전체 구조와 추천 학습 경로를 볼 수 있습니다.

### Concepts

> 추상 개념, 기술, 방법론

**🔍 외관 이상탐지**

- [[Visual Anomaly Detection]] — 결함을 배우는 대신 정상을 배우는 문제 설정. 언제 이 틀을 택하는가
- [[PatchCore]] — 정상 패치 메모리 뱅크 + 최근접 이웃 거리 기반 이상탐지. 이상점수와 Heatmap 을 함께 산출
- [[Patch-based High-Resolution Inspection]] — 몇 픽셀짜리 미세 결함을 리사이즈로 죽이지 않는 입력 처리 (ROI · 타일 분할)
- [[Safety-Critical Threshold Policy]] — 두 오류의 비용이 비대칭일 때 임계값을 FN 최소화 쪽으로 두는 원칙
- [[Multi-View Aggregation]] — 이미지 5 장을 물체 1 개의 판정으로 합치는 OR 규칙과 오탐 누적이라는 대가
- [[한도견본]] — 합격 경계선을 실물로 고정한 품질 기준. AI 검사에서는 라벨의 원천
- [[Human-in-the-Loop Inspection]] — 모델이 선별하고 사람이 확정하는 운영 구조
- [[Temporal Split and Data Leakage]] — 그룹 누수와 시간 누수를 함께 막는 평가 분할 설계

**🛠 볼트 운영**

- [[LLM Wiki Pattern]] — LLM 이 raw source 를 컴파일하여 persistent wiki 를 관리하는 패턴
- [[RAG vs Compiled Wiki]] — RAG(매번 재검색) vs Compiled Wiki(한 번 컴파일)의 비교
- [[3-Layer Architecture]] — Raw Sources / Wiki / Schema 3 층 구조
- [[Ingest-Query-Lint Cycle]] — Wiki 운영의 세 가지 핵심 작업 (Ingest, Query, Lint)
- [[Book Ingest Pattern]] — 멀티 페이지 책 · 문서 사이트용 ingest 변형. 챕터 stub 을 만들고 실제로 읽을 때 승격
- [[External Pre-processing Pattern]] — 무거운 원자료를 저렴한 외부 플랫폼에서 1 차 가공한 뒤 정제된 결과만 ingest 하는 비용 최적화 패턴
- [[Idea Generation Pipeline]] — 새 소스 ingest 를 아이디어 발산 트리거로 전환하는 워크플로
- [[Track Classification and Research Gap Detection]] — 논문을 주제 트랙으로 분류하고 커버리지가 낮은 트랙을 연구 공백으로 드러내는 패턴
- [[Cohort Token Economy]] — 집단(수업 · 연구실 · 스터디)이 LLM Wiki 를 쓸 때 토큰 한도가 병목이 되는 실패 패턴

**🕸 그래프 기반 저장소 분석**

- [[Graph-Based Codebase Understanding]] — 코드와 문서를 검색 청크가 아니라 관계 그래프로 이해하는 접근
- [[Multimodal Repository Knowledge Graph]] — 코드·문서·논문·다이어그램을 하나의 그래프에 통합
- [[Static-Semantic Hybrid Extraction]] — 코드 정적 분석과 모델 기반 의미 추출의 분업
- [[Vector-Free Graph Retrieval]] — 임베딩 대신 그래프 경로·이웃으로 범위를 좁히는 검색
- [[Software Architecture Community Detection]] — 그래프 커뮤니티를 잠재적 서브시스템으로 해석
- [[Knowledge Graph Query Economy]] — 서브그래프 질의로 컨텍스트 비용을 낮춘다는 검증 대상 가설

### Entities

> 사람, 조직, 제품, 모델

- [[EfficientNet]] — 깊이 · 너비 · 해상도를 함께 확장하는 CNN 백본. B0 는 빠른 분류 baseline
- [[ConvNeXt]] — 트랜스포머 설계 요소를 CNN 으로 되가져온 백본. Tiny 는 현대적 baseline
- [[Andrej Karpathy]] — AI 연구자, LLM Wiki 패턴 제안자
- [[Vannevar Bush]] — Memex 개념 제안자 (1945)
- [[Memex]] — 문서 간 associative trail 을 가진 개인 지식 저장소 구상
- [[Graphify]] — 코드·문서·논문·다이어그램을 질의 가능한 지식 그래프로 변환하는 오픈소스 도구
- [[Tree-sitter]] — Graphify의 코드 AST·관계 추출에 사용되는 정적 분석 파서

### Guides

> How-to, 튜토리얼, 실전 가이드

- [[Excel 임베디드 이미지 추출]] — .xlsx 내부 이미지와 Drawing Anchor 를 화질 손실 없이 꺼내 행에 매핑하는 절차
- [[Obsidian Tooling for LLM Wiki]] — Web Clipper, Dataview, qmd 등 실용 도구 가이드
- [[LLM Wiki Token Optimization Strategies]] — 토큰 예산 제약 하에서 무거운 위키 작업을 지속하는 전략
- [[Evaluating Graphify for Academic Research]] — Graphify의 제품 주장과 연구 근거를 분리해 평가하는 절차
- [[서울대 데이터사이언스 - 고급 LLM 및 RAG]] — 임베딩·RAG·LangChain·LangGraph·에이전트 엔지니어링 학습 지도
- [[서울대 데이터사이언스 - 컴퓨터 비전]] — 고전 비전부터 다중시점 기하·CNN·자세 추정·생성 모델까지의 학습 지도
- [[서울대 데이터사이언스 - 생성형 AI 이미지 방법론]] — VAE·Diffusion·Flow Matching·Autoregressive 생성과 FID 평가 학습 지도
- [[서울대 데이터사이언스 - 데이터 마이닝]] — 통계 추론·회귀·군집·차원축소·결측치·추천 학습 지도
- [[서울대 데이터사이언스 - 자료구조와 알고리즘]] — 자료구조·정렬·DP·그래프·최단경로·A* 학습 지도
- [[서울대 데이터사이언스 - 강화학습]] — MDP·DP·MC/TD·함수 근사·정책경사·Deep RL 학습 지도
- [[서울대 데이터사이언스 - 선형대수와 최적화]] — 머신러닝 수학 기초와 선형대수·최적화 실습 지도
- [[서울대 데이터사이언스 - 특강 모음]] — 이상탐지·암호·블록체인·양자컴퓨팅·DB 특강 지도
- [[서울대 데이터사이언스 - 파이썬과 데이터 시각화]] — Python·NumPy·pandas·Matplotlib·Altair·Spotfire 학습 지도

### Maps (MOC)

> 주제별 Map of Content

- [[MOC-Visual Anomaly Detection]] — 산업 외관 이상탐지: 방법 · 판정 · 기준 · 평가 전체 구조
- [[MOC-Knowledge Management]] — 지식 관리 개념, 패턴, 역사 종합
- [[MOC-LLM Wiki Guide]] — 이 볼트 사용 온보딩 가이드
- [[MOC-Graph-Based Repository Analysis]] — Graphify·혼합 추출·그래프 검색·연구 평가 구조
- [[MOC-서울대학교 데이터사이언스 코스워크]] — 9개 과목의 기초·모델링·생성형 AI 학습 경로

### Questions (RQ)

> 1 급 연구 질문 카드 (`RQ-{slug}.md`) — Open Question 콜아웃의 승격 대상

(첫 Research Question 카드를 만들면 여기에 기록됩니다.)

---

## 🔎 Queries (Synthesized Answers)

> 질의 결과가 wiki 에 역피드백된 합성 페이지. [[Ingest-Query-Lint Cycle|Karpathy 원문 권장]]: "good answers can be filed back into the wiki as new pages."

(첫 `/query` 를 실행하면 여기에 기록됩니다.)

---

## 📄 Paper Analyses (허브만)

> 논문 12 단 분석 — `40. Paper Analyses/{citekey}/` 의 허브(S00)만 여기 등록한다 (원자는 허브의 Atom Catalog 참조).

(첫 Paper Ingest 를 실행하면 여기에 기록됩니다.)

---

## 📥 Recent Ingests

| Date | Source | Pages Touched |
|------|--------|---------------|
| 2026-07-31 | [[MOC-서울대학교 데이터사이언스 코스워크\|서울대학교 데이터사이언스 코스워크]] | Raw index 9 · Guide 9 · MOC 1 |
| 2026-07-31 | [[2026-07-31-Graphify-Korean-Homepage\|Graphify 한국어 홈페이지]] | 10 신규 (Concepts 6 · Entities 2 · Guide 1 · MOC 1) |
| 2026-07-31 | [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서\|현업과제 제안서 — PatchCore 표면 이상탐지]] | 12 신규 (Concepts 8 · Entities 2 · Guide 1 · MOC 1) |
| 2026-04-12 | [[2026-04-12-Karpathy-LLM-Wiki\|Karpathy LLM Wiki Gist]] | 시드 — Concepts/Entities/Guides 다수 |
| 2026-04-02 | [[2026-04-02-Karpathy-LLM-Knowledge-Bases-X-Thread\|Karpathy LLM Knowledge Bases (X Thread)]] | 시드 — 토큰 경제 · 전처리 패턴 계열 |

→ [[log]] 참조

---

## 🔗 Quick Links

- [[Core Context]] — 사용자 맥락 (**모든 operation 전에 먼저 읽힘**)
- [[log]] — 전체 변경 이력
- [[CLAUDE]] — Schema (볼트 규칙서)
- [[MOC-LLM Wiki Guide]] — 볼트 사용 가이드

---

## 🚀 다음 단계

온보딩(placeholder 치환 + Core Context 작성)은 2026-07-31 에 완료되었습니다. 지금부터의 순서:

1. `/status` — 볼트 실측 상태 확인
2. 소스를 `00. Inbox/` 에 넣기 (Obsidian Web Clipper 또는 수동 저장)
3. `/ingest` — **목적 질문이 뜨면 [[Core Context]] §2 의 4 개 축 중 하나로 답할 것**
4. `/query` — 쌓인 Wiki 를 바탕으로 질문 답변
5. `/lint` — 주기적 건강도 체크

> [!tip] 첫 ingest 를 무엇으로 할까
> 재활용 축이 즉시 분명한 것부터 시작하는 편이 좋습니다. 예를 들어 수강 중인 과목의 핵심 논문 1 편(→ *학술 연구 · 논문* + *수업 · 코스워크*)이면 목적 질문에 망설임 없이 답할 수 있고, 축이 실제로 작동하는지도 바로 검증됩니다.

자세한 가이드는 [[LLM-Wiki-Starter-Kit]] 및 `90. Settings/Sharing/Setup Guide.md` 참조.
