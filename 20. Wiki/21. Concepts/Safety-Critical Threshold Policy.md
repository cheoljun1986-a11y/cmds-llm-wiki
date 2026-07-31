---
type: wiki-page
aliases:
  - Safety-Critical Threshold Policy
  - 안전 우선 임계값 정책
  - 비대칭 오류 비용
  - Asymmetric Error Cost
description: "Threshold-setting principle for classifiers whose two error types carry wildly different costs. When a false negative can cause a safety incident and a false positive only triggers a re-check, the operating point is chosen to minimise false negatives rather than to maximise accuracy or F1."
author:
  - Claude
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - evaluation
  - threshold
  - safety
  - quality-inspection
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
related:
  - "[[Visual Anomaly Detection]]"
  - "[[Multi-View Aggregation]]"
  - "[[Human-in-the-Loop Inspection]]"
  - "[[한도견본]]"
confidence: medium
layer: method
explored: false
claimType: prescriptive
evidenceScope: single-source
verificationStatus: unverified
---

# Safety-Critical Threshold Policy

## Overview

분류 모델의 임계값을 **통계적 최적점이 아니라 오류 비용의 비대칭성**에 맞춰 정하는 원칙이다.

두 오류의 결과가 대칭이 아닐 때, 정확도나 F1 을 최대화하는 임계값은 잘못된 선택이 된다. 그 지표들은 두 오류를 같은 무게로 세기 때문이다.

## Details

### 비용 구조를 먼저 쓴다

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|제안서]]의 사례에서 두 오류의 결과는 다음과 같다.

| 오류 | 무슨 일이 일어나는가 | 회복 가능한가 |
|---|---|---|
| False Positive (정상을 FAIL) | 제조사에 실물 확인·재촬영 요청 → 업무 증가 | 예 — 절차로 해소됨 |
| False Negative (FAIL 을 정상) | 오염·손상 실린더가 반입됨 → 밸브 부식 → LEAK → 화재·독성가스 노출 | 아니오 |

한쪽은 **업무 비용**이고 다른 쪽은 **안전사고**다. 이 비대칭이 확인되면 임계값 방향은 자동으로 정해진다 — FP 증가를 허용하고 FN 을 최소화한다.

### 지표 선택이 따라온다

제안서가 정한 지표 체계는 이 원칙의 직접적 귀결이다.

- **핵심 지표**: 실린더 단위 FAIL Recall, False Negative 개수
- **보조 지표**: Precision, F1-score, PR-AUC, Confusion Matrix
- **명시적 배제**: 전체 정확도 최대화, Precision 최대화

Recall 을 *개수*로도 보는 점이 눈에 띈다. 비율은 표본이 커지면 안정적으로 보이지만, 안전 맥락에서 중요한 것은 "몇 건을 놓쳤는가" 라는 절대 수다.

### FP 를 흡수하는 절차가 전제조건이다

이 정책은 공짜가 아니다. FP 가 늘어나는 만큼 **그것을 처리할 사람과 절차가 있어야** 성립한다. 제안서에서 그 역할을 하는 것이 제조사 실물 확인·재촬영 루프이며, 구조적으로는 [[Human-in-the-Loop Inspection]] 이다.

절차 용량을 넘어서면 정책이 무너진다 — 사람이 경보를 무시하기 시작하면 임계값을 아무리 보수적으로 잡아도 실효 FN 이 올라간다.

### PASS 도 표본 점검한다

제안서는 운영 초기에 **AI 가 PASS 로 판정한 건도 일정 비율 표본 점검**한다고 명시했다. FN 은 정의상 아무도 문제 제기를 하지 않기 때문에, 능동적으로 찾지 않으면 발견되지 않는다. FP 는 자연히 드러나지만 FN 은 그렇지 않다는 비대칭이 여기서도 작동한다.

> [!note] Bias Check
> Counter-argument: FN 최소화를 무한정 밀어붙이면 FP 가 폭증해 시스템이 사실상 "전부 재확인" 이 되고, AI 도입의 효용이 사라진다. 이 정책은 **FP 를 감당할 절차 용량이 있다는 전제** 위에서만 합리적이며, 그 용량은 제안서에 정량화되어 있지 않다.
> Data gap: 허용 가능한 FP 율의 상한, 재촬영 1 건당 실제 소요 시간·비용이 확인되지 않았다. 이 수치 없이는 "허용 가능" 이 검증 불가능한 주장으로 남는다.

> [!question] Open Question
> **임계값을 View 별로 따로 둘 것인가, 하나로 통일할 것인가?** 제안서는 View 별 조정을 언급하지만, View 마다 다른 임계값은 실린더 단위 FN 율을 예측하기 어렵게 만든다 ([[Multi-View Aggregation]] 의 OR 결합과 상호작용).

## Related

- [[Multi-View Aggregation]] — 임계값이 실린더 단위 판정으로 증폭되는 경로
- [[Human-in-the-Loop Inspection]] — FP 를 흡수하는 절차
- [[Visual Anomaly Detection]] — 이상점수를 임계값으로 자르는 문제 설정
- [[한도견본]] — 판단 불가를 FAIL 쪽에 두는 같은 방향의 원칙

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §1.2 성공 기준, §3.6 실린더 단위 판정 로직, §3.7 모델 평가 및 검증
