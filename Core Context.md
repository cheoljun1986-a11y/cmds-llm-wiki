---
type: core-context
aliases:
  - User Context
  - 핵심 맥락
description: "Core context for cheoljun1986 — identity as a data-science practitioner studying alongside work, four knowledge-reuse axes (research, coursework, projects, career), and operating directives. LLM must read this BEFORE any ingest/query/lint so operations align with purpose, not just structure."
author:
  - "[[cheoljun1986]]"
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - system
  - schema
  - core-context
source: []
version: "1.0"
snapshot_date: 2026-07-31
status: active
---

# 🧭 Core Context — LLM Wiki 사용자 맥락

> 이 노트는 LLM 이 ingest / query / lint 전에 **반드시 먼저 읽는** 사용자 맥락이다.
> 운영 모드: **Mode A (단독 운영)** — 별도 mothership 볼트를 연계하지 않는다. `mainVaultRelated` · `mainVaultCmds` 프로퍼티는 이 볼트에서 사용하지 않으며, `/ingest` 의 Step 0-a (메인 볼트 연결 검색) 는 건너뛴다.

---

## 1. Who — 사용자 정체성

### 기본 정체성

- **이름**: cheoljun1986
- **직함 / 역할**: 데이터사이언스 실무자 + 학업 병행 (현업 적용과 코스워크를 동시에 진행)
- **전문 분야**: 데이터사이언스 · 머신러닝
- **주 활동 영역**: 실무 데이터 문제 해결 + 정규 코스워크 학습 (Computer Vision, Database, Data Intelligence, Machine Learning, Reinforcement Learning, Visualization, 알고리즘)

### 연속성 선언 (Continuity Statement)

> [!question] 확인 필요 — 에이전트 초안
> 아래 문장은 사용자가 직접 진술한 것이 아니라, 온보딩 시점의 볼트 정황(코스워크 노트 구성 + 실무 병행)에서 **에이전트가 추론한 초안**이다. 본인 문장으로 교체하는 것이 이 노트의 가장 큰 성능 개선 지점이다.

> "나는 실무에서 데이터로 의사결정을 만드는 사람이다. 지금 수업에서 CV · RL · DB 를 따로 배우고 있지만 내가 보는 것은 결국 하나 — '데이터를 어떻게 신뢰 가능한 판단으로 바꾸는가' 이다. 코스워크는 그 판단의 근거를 더 깊게 만들기 위한 도구의 확장이지, 별개의 트랙이 아니다."

이 선언은 LLM 이 "왜 이 사람이 이 주제를 수집하는가" 의 깊이를 이해하는 앵커가 된다. 수정하려면 이 섹션을 직접 고치거나 `/refresh-context` 를 실행한다.

---

## 2. Why — 지식을 수집하는 목적 (재활용 축)

**미래의 나에게 보내는 편지**: "이 소스가 아래 어느 축에 재활용될지" 를 수집 시점에 명시하지 못하면 수집하지 않는다.

`/ingest` 는 매 수집마다 아래 축 중 하나 이상을 묻고 `collectionPurpose` 프로퍼티에 기록한다.

1. **학술 연구 · 논문**: 연구 질문, 논문 작성, 학위 과정 산출물. 서베이 · 선행연구 정리, 방법론 비교가 여기 붙는다.
2. **수업 · 코스워크**: 수강 과목 학습, 과제, 시험 대비. CV · DB · DI · ML · RL · VIS · 알고리즘 등 정규 과정 소화.
3. **프로젝트 · 구현**: 실제로 코드로 이어지는 것 — 미니프로젝트, 캡스톤, 실무 파이프라인, 재현 실험.
4. **커리어 · 포트폴리오**: 취업 · 이직 준비, 기술 블로그, 포트폴리오로 외재화될 자료.

> [!note] 축 확장 후보 (현재 비활성)
> 키트 권장은 5~9 개 축이고 현재는 4 개다. 축이 적으면 대부분의 수집이 한두 축으로 쏠려 `collectionPurpose` 의 변별력이 떨어진다. 아래는 위 4 축에 잘 안 들어가는 자료가 반복해서 나타날 때 승격할 후보다 — 실제로 그런 자료가 3 회 이상 쌓이기 전에는 추가하지 않는다 (YAGNI).
> - **도구 · 인프라**: MLOps, 실험 관리, 개발 환경 자체에 관한 자료
> - **도메인 지식**: 데이터가 아니라 그 데이터가 설명하는 산업 · 분야에 관한 자료
> - **학습 방법론 · 지식관리**: 이 볼트 운영 자체를 개선하는 메타 자료

---

## 3. What — (옵션) 개인 지식 프레임워크

**미작성.** 자체 지식 관리 프레임워크(지식 생애주기 단계, 카테고리 체계 등)가 정립되면 여기에 기록한다. 현재는 이 볼트의 3-Layer 구조([[CLAUDE]] 참조)를 그대로 따른다.

참고 사례: [cmds-system-files](https://github.com/johnfkoo951/cmds-system-files) — Connect → Merge → Develop → Share + 100-900 9 categories.

---

## 4. How — (옵션) 지식 시스템 철학

**미작성.** LLM 이 정리 과정에서 따라야 할 개인 원칙이 정해지면 3~5 개로 요약해 기록한다. 본인 에세이 · 블로그 · 회고에서 추출하는 것이 가장 정확하다 — 해당 글이 생기면 `/refresh-context` 로 이 섹션을 채울 수 있다.

이 섹션이 비어 있는 동안 LLM 은 §1 연속성 선언과 §2 재활용 축만을 정렬 기준으로 사용한다.

---

## 5. Operational Directives (LLM 행동 규칙)

### Ingest 시

1. `/ingest` 는 반드시 "왜 수집했는가?" 를 1 회 묻는다 (미래의 나에게 보내는 편지, §2 축 참조).
2. **Mode A 이므로 mothership 검색(Step 0-a) 은 건너뛴다.** `mainVaultRelated` · `mainVaultCmds` 프로퍼티는 기록하지 않는다.
3. Raw Source frontmatter 에 `collectionPurpose` 를 기록한다.

### Query 시

1. 답변이 §2 재활용 축 중 어느 축에 연결되는지 명시한다.
2. 인용 시 `verificationStatus` + `confidence` 를 함께 읽는다 — `verified` + `high` 면 단언, `partial` 또는 `medium` 이하면 hedge, `disputed` 면 양쪽을 명시한 뒤 답한다.

### Lint 시

- Raw Source 에 `collectionPurpose` 없으면 flag.
- Core Context `snapshot_date` 가 30 일 이상 오래되면 `/refresh-context` 추천.
- **Mode A 이므로 `mainVaultRelated` 누락은 flag 하지 않는다.**

### 이미지 저장

- 모든 이미지 · 첨부: `80. References/Attachments/` 일원화.

---

## 6. 온보딩 체크리스트

- [x] §1 정체성 채움 (연속성 선언은 에이전트 초안 — 본인 문장으로 교체 권장)
- [x] §2 재활용 축 정의 (4 개 활성 + 3 개 확장 후보)
- [ ] (옵션) §3 개인 프레임워크
- [ ] (옵션) §4 철학 3~5 개
- [x] Mode A 확정 — mothership 섹션 삭제
- [x] frontmatter `status: active`
- [x] frontmatter `snapshot_date` 2026-07-31
- [ ] frontmatter `source:` 에 본인이 참고한 에세이 · 노트 경로 추가

---

## 7. Related

- [[CLAUDE]] — LLM Wiki Schema
- [[index]] — Master Index
- [[log]] — Change Log
- [[LLM-Wiki-Starter-Kit]] — 외부 공유용 간이 킷

---

*Core Context v1.0 — Karpathy LLM Wiki pattern + 미래의 나에게 보내는 편지. 온보딩 2026-07-31, Mode A (standalone).*
