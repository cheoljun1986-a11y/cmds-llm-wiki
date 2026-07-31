---
type: wiki-page
aliases:
  - Visual Anomaly Detection
  - 시각적 이상탐지
  - 외관 이상탐지
  - Industrial Anomaly Detection
description: "Problem framing where a model learns what normal looks like and flags deviations, instead of learning to classify a fixed set of known defect classes. Chosen when defect samples are rare, defect types are open-ended, and missing a defect costs far more than a false alarm."
author:
  - Claude
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - anomaly-detection
  - computer-vision
  - quality-inspection
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
related:
  - "[[PatchCore]]"
  - "[[한도견본]]"
  - "[[Human-in-the-Loop Inspection]]"
  - "[[Safety-Critical Threshold Policy]]"
confidence: medium
layer: concepts
explored: false
claimType: theoretical
evidenceScope: single-source
verificationStatus: unverified
---

# Visual Anomaly Detection

## Overview

시각적 이상탐지는 **"결함이 무엇인지"를 배우는 대신 "정상이 무엇인지"를 배우는** 문제 설정이다. 정상 분포를 모델링해 두고, 새 이미지가 그 분포에서 벗어난 정도를 점수로 낸다.

지도학습 분류와의 갈림길은 데이터 조건에서 갈린다.

| 조건 | 지도학습 분류 | 이상탐지 |
|---|---|---|
| 결함 표본 수 | 클래스별로 충분해야 함 | 없어도 학습 가능 |
| 결함 유형 | 미리 열거 가능해야 함 | 열려 있어도 됨 |
| 새로운 결함 | 학습에 없으면 놓침 | 원리상 탐지 대상 |
| 산출물 | 클래스 확률 | 이상점수 + 위치 |

## Details

### 이 문제 설정이 선택되는 전형적 조건

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|현업과제 제안서]]의 상황이 교과서적 사례다.

1. **불균형이 극단적이다** — 납품 실린더 대부분은 정상이다. FAIL 은 드물게 발생한다.
2. **기존 판정 이력이 라벨로 남아 있지 않다** — 사람이 PASS/FAIL 을 판단해 왔지만 구조화된 형태로 축적되지 않아, 지도학습을 위한 정답지가 사실상 0 에서 시작한다.
3. **결함 유형이 열려 있다** — Particle, Scratch, 오염, 변색, 부식 의심까지 나열되지만, 이 목록이 닫혀 있다는 보장이 없다.
4. **정상 데이터는 풍부하다** — 연 약 10,000 실린더, 수년치 누적 시 최대 약 50,000 실린더 규모의 이미지가 존재한다.

### 평가가 정확도로 끝나지 않는 이유

정상이 압도적 다수인 데이터에서 **정확도(accuracy) 는 거의 무의미**하다. 전부 PASS 로 찍어도 높은 정확도가 나온다. 따라서 평가는 FAIL 쪽 지표 — Recall, False Negative 개수, PR-AUC — 로 이동한다. 임계값을 어디에 둘지는 통계가 아니라 **비용 구조**가 결정하며, 그 논리가 [[Safety-Critical Threshold Policy]] 다.

### 정답의 기준이 필요하다

"정상에서 벗어남" 을 판정하려면 어디까지가 정상인지에 대한 **인간 측 기준**이 있어야 한다. 제조 품질에서 그 역할을 하는 것이 [[한도견본]] 이다. 이상탐지 모델은 이 기준을 학습하는 것이 아니라, 이 기준으로 만들어진 라벨에 맞춰 **임계값이 조정**된다.

> [!note] Bias Check
> Counter-argument: 이상탐지가 "새로운 결함도 잡는다" 는 것은 원리적 장점이지만 실증적 보장은 아니다. 정상 분포에 미묘하게 섞여 들어가는 결함(예: 매우 옅은 변색)은 거리 기준으로 정상과 구분되지 않을 수 있다.
> Data gap: 위 비교표와 선택 조건은 제안서 한 건과 일반 지식에 기반한다. MVTec AD 같은 벤치마크 결과나 이상탐지 서베이를 ingest 해 뒷받침해야 한다.

> [!question] Open Question
> 지도학습 분류 baseline 과 이상탐지 중 **어느 쪽이 이 데이터에서 실제로 더 나은가?** 제안서는 둘을 비교하겠다고만 밝혔다. 라벨이 축적된 뒤에는 지도학습이 역전할 수도 있으며, 그 전환 시점을 판단할 기준이 아직 정의되지 않았다.

## Related

- [[PatchCore]] — 이 문제 설정의 구체적 구현 하나
- [[한도견본]] — 정상/이상의 인간 측 판정 기준
- [[Safety-Critical Threshold Policy]] — 이상점수를 판정으로 바꾸는 정책
- [[Human-in-the-Loop Inspection]] — 모델 단독 판정을 피하는 운영 구조
- [[Temporal Split and Data Leakage]] — 성능을 정직하게 측정하기 위한 분할 설계

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §2 문제 정의, §3.5 모델 개발 전략, §4 데이터 확보 계획
