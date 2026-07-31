---
type: wiki-page
aliases:
  - Temporal Split and Data Leakage
  - 시간순 분할
  - 데이터 누수
  - Group Leakage
description: "Evaluation design that prevents optimistic bias by (a) keeping all images of one decision unit inside a single split and (b) holding out the most recent period as the test set. Necessary whenever the same physical object recurs across records and whenever the data-generating process drifts over time."
author:
  - Claude
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - evaluation
  - data-leakage
  - train-test-split
  - methodology
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
related:
  - "[[Multi-View Aggregation]]"
  - "[[Visual Anomaly Detection]]"
  - "[[한도견본]]"
confidence: medium
layer: method
explored: false
claimType: prescriptive
evidenceScope: single-source
verificationStatus: unverified
---

# Temporal Split and Data Leakage

## Overview

성능 수치를 정직하게 만드는 **분할 설계**의 문제다. 두 종류의 누수를 동시에 막아야 한다.

- **그룹 누수** — 같은 판정 단위에 속한 샘플이 학습과 평가에 흩어지는 것
- **시간 누수** — 미래 데이터로 학습하고 과거 데이터로 평가하는 것

둘 다 성능을 실제보다 좋아 보이게 만든다.

## Details

### 데이터 단위를 먼저 정의한다

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|제안서]]에서 가장 정교한 대목이다. 무엇이 하나의 데이터인가에 대한 답이 자명하지 않다.

- 실린더는 **영구적인 Serial Number** 를 갖는다.
- 사용 후 회수 → 재충전 → 재납품되므로 **같은 실린더가 여러 번 등장**한다.
- 밸브는 약 5 년 수명이라 **매 회차 교체되지 않는다** — 같은 밸브가 여러 검사 이력에 걸쳐 반복된다.
- 그러나 운송 중 스크래치·오염 상태는 **납품 시점마다 다르다**.

이에 따라 제안서는 데이터 단위를 실린더가 아니라 **"특정 납품 시점의 검사 건"** 으로 정의하고, 실린더 ID 와 검사일(또는 납품 Batch)을 결합해 관리한다.

### 두 가지 분할 규칙

| 규칙 | 내용 | 막는 누수 |
|---|---|---|
| 5 View 는 같은 집합에 | 한 검사 건의 이미지 5 장을 Train/Val/Test 에 흩지 않음 | 그룹 누수 — 같은 사진의 이웃 View 를 이미 본 상태로 평가 |
| 최근 기간을 Test 로 | 과거 검사 건으로 학습·검증, 최근 기간을 독립 Test | 시간 누수 — 미래를 보고 과거를 맞히는 낙관 편향 |

첫 번째는 [[Multi-View Aggregation]] 과 직결된다. 5 장이 하나의 최종 판정 단위이므로, 분할이 갈리면 실린더 단위 성능을 아예 계산할 수 없다.

### 같은 실린더의 재등장은 누수인가

제안서의 입장은 **아니다** — 다른 시점의 검사 건은 새로운 밸브 상태와 새로운 충전 상태를 가진 별도 표본으로 간주한다. 다만 과거 이상 이력은 이후 검사의 참고 정보로 활용할 수 있도록 추적 가능하게 설계한다.

이 판단은 논쟁 여지가 있다. 밸브가 교체되지 않았다면 **같은 물리적 표면**이 학습과 평가에 모두 등장하며, 영구적 특징(제조 각인, 고유 흠집)이 모델에 기억될 수 있다.

### 시간순 분할이 필요한 진짜 이유

무작위 분할이 아니라 시간순 분할을 택하는 것은 단순히 관행이 아니다. 제안서가 위험 항목으로 든 **제조사·촬영 환경 변화** 때문이다. 조명이 바뀌거나 카메라가 교체되거나 [[한도견본]] 기준이 개정되면 데이터 분포가 이동한다. 무작위 분할은 이 이동을 평균 내어 감춘다.

> [!warning] Contradiction
> 제안서는 같은 실린더의 재등장을 "별도 표본" 으로 간주하면서, 동시에 밸브가 약 5 년간 교체되지 않는다고 명시한다. **밸브 표면이 물리적으로 동일한데 독립 표본으로 취급하는 것**은 그룹 누수를 남길 수 있다. 최소한 밸브 ID 단위 분할을 함께 시험해 두 방식의 성능 차이를 확인해야 판단할 수 있다.

> [!note] Bias Check
> Counter-argument: 밸브 ID 단위로 엄격히 분할하면 학습 표본이 줄고, 실제 운영에서는 같은 밸브가 반복 검사되는 것이 정상이므로 오히려 비현실적인 평가가 될 수 있다. 어느 쪽이 옳은지는 두 분할의 성능 격차를 실측해야 한다.
> Data gap: 데이터셋에서 동일 밸브가 재등장하는 비율이 확인되지 않았다. 이 비율이 낮으면 위 모순은 실무적으로 무시할 수 있다.

> [!question] Open Question
> 최근 기간을 Test 로 두면 **Test 기간의 FAIL 건수가 충분한가?** FAIL 이 드문 데이터에서 시간순 홀드아웃은 평가 표본의 양성 사례를 극단적으로 적게 만들 수 있고, 그러면 Recall 추정의 신뢰구간이 매우 넓어진다.

## Related

- [[Multi-View Aggregation]] — 5 장을 같은 분할에 묶어야 하는 이유
- [[Visual Anomaly Detection]] — 정직한 평가가 특히 중요한 불균형 문제
- [[한도견본]] — 기준 개정이 분포 이동을 만드는 경로

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §3.7 모델 평가 및 검증, §6 예상 어려움
