---
type: log
aliases:
  - Change Log
  - Wiki Log
  - Ingest Log
description: "Chronological log of all wiki operations — ingests, queries, lint fixes, and structural changes. Append-only; entries use a bracketed-date operation prefix for grep-based parsing."
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
  - system
  - log
status: active
---

# 📝 LLM Wiki — Change Log

> 모든 wiki 변경사항을 시간순으로 기록합니다. **Append-only** — 기존 항목을 수정하지 마세요.
>
> **Entry format (Karpathy-style)**: `## [YYYY-MM-DD] operation | title`
>
> **Quick scan**:
>
> ```bash
> grep "^## \[" log.md | tail -10   # 최근 10개 operation
> grep "^## \[.*\] ingest" log.md   # ingest만 필터
> ```
>
> **Operations**: `ingest`, `update`, `create`, `lint`, `query`, `restructure`, `cleanup`

---

## [2026-04-12] ingest | Karpathy LLM Wiki Gist (example)

- Source: [[2026-04-12-Karpathy-LLM-Wiki]]
- Origin: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Raw Source 저장: `10. Raw Sources/11. Articles/`
- Wiki 페이지 생성 (10):
	- Concepts (4): [[LLM Wiki Pattern]], [[RAG vs Compiled Wiki]], [[3-Layer Architecture]], [[Ingest-Query-Lint Cycle]]
	- Entities (3): [[Andrej Karpathy]], [[Vannevar Bush]], [[Memex]]
	- Guides (1): [[Obsidian Tooling for LLM Wiki]]
	- Maps (2): [[MOC-Knowledge Management]], [[MOC-LLM Wiki Guide]]
- **예시 ingest** — 이 볼트가 어떻게 성장하는지 보여주기 위한 샘플. 본인 소스 ingest 시작 시 이 entry 아래에 append.

## [2026-07-31] create | Vault initialized — onboarding (Mode A)

- Cloned from [cmds-llm-wiki template](https://github.com/johnfkoo951/cmds-llm-wiki)
- 운영 모드 확정: **Mode A (단독 운영)** — 상위 `Documents/Obsidian Vault/` 가 별도 Obsidian 볼트이지만 모선으로 연계하지 않음. `mainVaultRelated` · `mainVaultCmds` 미사용.
- Placeholder 치환 (화이트리스트 방식, 운영 파일 15 개):
	- `{your-name}` · `{Your Name}` → `cheoljun1986` — [[CLAUDE]], [[AGENTS]], [[Core Context]], [[index]], [[log]], `Template_Raw Source`, `Template_AI Research Capture`, `capture-tabs` (Claude · Codex)
	- `{PATH_TO_YOUR_LLM_WIKI}` → 볼트 절대경로 — `.codex/hooks.json`, `.codex/hooks/qmd-reindex.sh`, `90. Settings/qmd-config-template.yml`, `90. Settings/Web Clipper Templates.md`, [[CLAUDE]], [[AGENTS]]
	- **제외**: `README.md`, `CHANGELOG.md`, `Setup Guide.md`, `.claude/commands/onboard.md` — placeholder 토큰 자체를 설명하는 문서라 치환 시 의미가 깨짐
	- **제외**: `{YYYY-MM-DD}` 전역 치환 — harness 의 로그 출력 템플릿(`.claude/commands/ingest.md` 등) 과 경로 규약 문서에 리터럴로 남아야 함. [[Core Context]] · [[index]] · [[log]] 3 개 파일에서만 치환.
- [[Core Context]] 작성: §1 정체성 (데이터사이언스 실무자 + 학업 병행), §2 재활용 축 4 개 (학술 연구 · 논문 / 수업 · 코스워크 / 프로젝트 · 구현 / 커리어 · 포트폴리오), §5 Mothership 섹션 삭제, `status: template` → `active`
- [[index]] 실측 동기화: Concepts 4 → 9, Guides 1 → 2, Recent Ingests 1 → 2 건으로 갱신 (기존 인덱스가 실제 볼트와 drift 상태였음)
- 미결 항목: [[Core Context]] §1 연속성 선언은 **에이전트 초안** — 본인 문장으로 교체 필요. §3 프레임워크 · §4 철학 미작성.
- 다음: `/status` → `00. Inbox/` 에 첫 소스 투입 → `/ingest`

## [2026-07-31] ingest | 현업과제 제안서 — PatchCore 기반 반도체 특수가스 용기 표면 이상탐지

- Source: [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]
- **Purpose**: 프로젝트 · 구현, 수업 · 코스워크
- Mothership links: 없음 (Mode A — 단독 운영)
- 입력 형식: `.docx` (바이너리) → Step 0.5 변환 수행
	- 변환 도구가 없어(`markitdown`·`pandoc` 미설치) `90. Settings/Scripts/docx_to_md.py` 를 신규 작성 — 파이썬 표준 라이브러리(zipfile + xml.etree)만 사용, 외부 설치 불필요
	- 원본 바이너리는 `80. References/Attachments/현업과제 제안서 (2).docx` 로 보존 이동 (불변 원칙을 참조로 충족)
	- 변환 충실도 `medium` — 제목 · 문단 · 목록 · 표 · 굵게 보존, 시각적 서식 소실. 문서 내 이미지 0 건
	- verbatim 검증: Raw Source 본문과 `.docx` 재생성본이 21,178 바이트로 완전 일치
- Pages created (12):
	- Concepts (8): [[Visual Anomaly Detection]], [[PatchCore]], [[Patch-based High-Resolution Inspection]], [[Safety-Critical Threshold Policy]], [[Multi-View Aggregation]], [[한도견본]], [[Human-in-the-Loop Inspection]], [[Temporal Split and Data Leakage]]
	- Entities (2): [[EfficientNet]], [[ConvNeXt]]
	- Guides (1): [[Excel 임베디드 이미지 추출]]
	- Maps (1): [[MOC-Visual Anomaly Detection]]
- Pages updated: [[index]] (stats 16→28 wiki pages, 신규 클러스터 등재, Recent Ingests 행 추가)
- 발견한 모순: [[Temporal Split and Data Leakage]] 에 `> [!warning] Contradiction` 1 건 — 제안서가 동일 실린더 재등장을 "별도 표본" 으로 간주하면서 동시에 밸브가 약 5 년간 교체되지 않는다고 명시. 물리적으로 같은 밸브 표면이 학습·평가에 모두 등장할 수 있어 그룹 누수 가능성이 남는다.
- Open Questions (9): View 별 메모리 뱅크 분리 여부, baseline 과 PatchCore 의 공정 비교 조건, 한도견본 개정 시 소급 재판정 정책, 자동화 수준 졸업 기준, 타일 경계 결함 처리, 제조사별 Excel 양식 차이 등
- 지식 공백: 이번 클러스터는 전부 `evidenceScope: single-source`. PatchCore 원논문(Roth et al., CVPR 2022), 이상탐지 서베이, MVTec AD 벤치마크를 ingest 하면 대부분 `multi-source-primary` 로 승격 가능 — 다음 ingest 우선순위.

## [2026-07-31] ingest | Graphify — AI 코딩 어시스턴트를 위한 지식 그래프

- Source: [[2026-07-31-Graphify-Korean-Homepage]]
- Origin: https://graphify.net/kr/
- **Purpose**: 학술 연구 · 논문 — 지식 그래프 기반 문헌·코드 분석 방식과 주장된 토큰 효율을 연구 도구 후보로 평가
- Mothership links: 없음 (Mode A — 단독 운영)
- Raw Source 저장: `10. Raw Sources/11. Articles/`
	- 공개 한국어 홈페이지의 렌더링 본문을 `## Original Content` 아래 보존
	- 내비게이션·푸터·시각 스타일·상호작용은 캡처 범위에서 제외
- Pages created (10):
	- Concepts (6): [[Graph-Based Codebase Understanding]], [[Multimodal Repository Knowledge Graph]], [[Static-Semantic Hybrid Extraction]], [[Vector-Free Graph Retrieval]], [[Software Architecture Community Detection]], [[Knowledge Graph Query Economy]]
	- Entities (2): [[Graphify]], [[Tree-sitter]]
	- Guides (1): [[Evaluating Graphify for Academic Research]]
	- Maps (1): [[MOC-Graph-Based Repository Analysis]]
- Pages updated: [[index]] (Raw Sources 3→4, Wiki Pages 28→38, 신규 클러스터 및 Recent Ingests 등재)
- 검증 경계: 홈페이지의 `71.5×` 토큰 절감, 약 50만 단어 코퍼스의 2k 토큰 질의, 보안·확장성 설명은 제작자 주장으로 보존했으며 독립 검증하지 않음.
- 다음 연구 단계: 버전 고정 로컬 실행, 정답 관계가 알려진 코드+논문 코퍼스, 키워드 검색·dense retrieval 대조군을 사용해 추출 정확도·답변 품질·총비용을 평가.

## [2026-07-31] ingest | 서울대학교 데이터사이언스 코스워크 — 9개 과목 자료 묶음

- Source corpus: `10. Raw Sources/17.seoul_univ_ds/`
- **Purpose**: 수업 · 코스워크 — 서울대학교 데이터사이언스 강의자료를 과목별 학습·복습 자산으로 컴파일
- Mothership links: 없음 (Mode A — 단독 운영)
- 처리 범위:
	- 9개 과목, 306개 파일의 경로·형식·크기 인벤토리를 생성
	- 원본 PDF·PPTX·IPYNB·코드·데이터·압축 파일은 이동하거나 재작성하지 않음
	- 약 1.8GB 이상의 혼합형 코퍼스이므로 `status: stub`, `conversionFidelity: inventory-only` 점진형 인제스트 적용
	- 일부 동일 파일명 후보, 0바이트 파일, 텍스트 비추출 바이너리 형식을 과목별 Raw Source 인덱스에 기록
- Raw Source indexes created (9):
	- [[2026-07-31-snu-ds-advanced-llms-rag-course-index]]
	- [[2026-07-31-snu-ds-computer-vision-course-index]]
	- [[2026-07-31-snu-ds-generative-image-methods-course-index]]
	- [[2026-07-31-snu-ds-data-mining-course-index]]
	- [[2026-07-31-snu-ds-data-structures-algorithms-course-index]]
	- [[2026-07-31-snu-ds-reinforcement-learning-course-index]]
	- [[2026-07-31-snu-ds-linear-algebra-optimization-course-index]]
	- [[2026-07-31-snu-ds-special-lectures-course-index]]
	- [[2026-07-31-snu-ds-python-data-visualization-course-index]]
- Wiki pages created (10):
	- Guides (9): [[서울대 데이터사이언스 - 고급 LLM 및 RAG]], [[서울대 데이터사이언스 - 컴퓨터 비전]], [[서울대 데이터사이언스 - 생성형 AI 이미지 방법론]], [[서울대 데이터사이언스 - 데이터 마이닝]], [[서울대 데이터사이언스 - 자료구조와 알고리즘]], [[서울대 데이터사이언스 - 강화학습]], [[서울대 데이터사이언스 - 선형대수와 최적화]], [[서울대 데이터사이언스 - 특강 모음]], [[서울대 데이터사이언스 - 파이썬과 데이터 시각화]]
	- Maps (1): [[MOC-서울대학교 데이터사이언스 코스워크]]
- Pages updated: [[index]] (Raw Sources 4→13, Wiki Pages 38→48, Guides 4→13, MOCs 4→5)
- Stop condition: 시스템 구축까지만 수행. 강의 본문 전면 추출·요약·세부 개념 페이지 양산·qmd 임베딩 생성은 하지 않음.
