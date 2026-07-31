---
type: wiki-page
aliases:
  - Multi-View Aggregation
  - 다시점 통합 판정
  - 5장 통합 로직
  - View Aggregation
description: "Rule for collapsing several per-image predictions about the same physical object into one decision. An OR rule (any image FAIL implies object FAIL) maximises safety recall but compounds per-image false positives across views, so the per-image threshold and the aggregation rule must be designed together."
author:
  - Claude
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - aggregation
  - decision-logic
  - quality-inspection
  - evaluation
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
related:
  - "[[Safety-Critical Threshold Policy]]"
  - "[[PatchCore]]"
  - "[[Temporal Split and Data Leakage]]"
confidence: medium
layer: method
explored: false
claimType: prescriptive
evidenceScope: single-source
verificationStatus: unverified
---

# Multi-View Aggregation

## Overview

같은 물체를 여러 각도에서 찍은 이미지들의 개별 판정을 **하나의 물체 판정으로 합치는 규칙**이다.

모델이 내놓는 것은 이미지 단위 판정이지만, 현업에서 필요한 것은 물체(실린더) 단위 판정이다. 그 사이를 잇는 규칙이 성능과 안전성을 크게 좌우한다.

## Details

### OR 규칙 — 하나라도 FAIL 이면 FAIL

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|제안서]]가 채택한 규칙은 단순하다.

- 실린더 1 대 = 정해진 부위·각도의 이미지 5 장
- **5 장 중 한 장이라도 FAIL → 실린더 FAIL**
- 5 장 모두 유효한 화질이고 모두 PASS → 실린더 PASS 후보
- 흐림·과노출·가림·잘못된 부위 등 판단 불가 → FAIL 로 취급하여 재확인

물리적으로 타당한 규칙이다 — 결함은 실린더의 한 곳에만 있어도 결함이며, 그 부위를 찍은 사진에만 나타난다.

### 수학적 대가: 오탐이 누적된다

OR 규칙은 재현율을 올리는 대신 **오탐을 5 번 곱한다**. 이미지 단위 FP 율이 $p$ 이고 View 들이 독립이라면, 실린더 단위 FP 율은

$$1 - (1-p)^5$$

이미지 FP 율 5% 는 실린더 FP 율 약 23% 가 된다. 1% 라도 약 5% 다. 즉 **이미지 단위 임계값을 정할 때 이미 5배 증폭을 염두에 두어야** 한다.

| 이미지 FP 율 | 실린더 FP 율 (OR, 독립 가정) |
|---|---|
| 0.5% | 약 2.5% |
| 1% | 약 4.9% |
| 3% | 약 14.1% |
| 5% | 약 22.6% |

이 때문에 [[Safety-Critical Threshold Policy]] 와 이 페이지는 **따로 정할 수 없다**. 임계값을 이미지 단위로만 최적화하면 실린더 단위 업무량이 예상을 벗어난다.

### 평가도 두 층위로

제안서는 **View 별 이미지 성능과 5 장 통합 실린더 성능을 모두 산출**한다고 명시했다. 이미지 지표만 보면 통합 후 실제 운영 부하를 알 수 없고, 실린더 지표만 보면 어느 View 가 문제인지 알 수 없다.

> [!note] Bias Check
> Counter-argument: 위 증폭 계산은 **View 간 독립**을 가정한다. 실제로는 같은 실린더의 조명·표면 상태가 공유되므로 오탐이 상관되어 실제 증폭은 이보다 작을 가능성이 높다. 표의 수치는 상한선으로 읽어야 한다.
> Data gap: View 간 오탐 상관계수가 측정되지 않았다. 실측 전까지 실린더 단위 FP 율은 추정치일 뿐이다.

> [!question] Open Question
> **OR 이 아닌 대안 규칙이 더 나을 수 있는가?** 예를 들어 "이상점수 최댓값이 임계값 초과" 또는 "2 장 이상 FAIL" 같은 규칙은 FP 를 줄이지만 단일 부위 결함을 놓칠 위험이 있다. 제안서는 OR 만 채택하고 대안을 비교하지 않았다.

## Related

- [[Safety-Critical Threshold Policy]] — 함께 설계해야 하는 임계값 정책
- [[PatchCore]] — 이미지 단위 점수를 만들어 내는 모델
- [[Temporal Split and Data Leakage]] — 5 장을 같은 분할에 묶어야 하는 이유

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §3.6 실린더 단위 판정 로직, §3.7 모델 평가 및 검증
