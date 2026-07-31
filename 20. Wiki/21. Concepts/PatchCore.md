---
type: wiki-page
aliases:
  - PatchCore
  - 패치코어
  - Memory Bank Anomaly Detection
description: "Memory-bank based visual anomaly detection method that stores locally-aware patch features from normal images only, then scores new patches by nearest-neighbour distance to that bank. Produces both an image-level anomaly score and a pixel-level heatmap, which makes it attractive when defect labels are scarce and defect types are open-ended."
author:
  - Claude
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - anomaly-detection
  - computer-vision
  - patchcore
  - unsupervised
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
related:
  - "[[Visual Anomaly Detection]]"
  - "[[Patch-based High-Resolution Inspection]]"
  - "[[Safety-Critical Threshold Policy]]"
  - "[[Multi-View Aggregation]]"
confidence: medium
layer: method
explored: false
claimType: theoretical
evidenceScope: single-source
verificationStatus: unverified
---

# PatchCore

## Overview

PatchCore 는 **정상 이미지만으로 학습하는 이상탐지 방법**이다. 사전학습된 백본에서 뽑은 국소 특징(patch feature)을 메모리 뱅크에 저장해 두고, 새 이미지의 각 패치가 그 뱅크로부터 얼마나 떨어져 있는지를 이상점수로 계산한다.

이 접근이 산업 검사에서 선택되는 이유는 데이터 조건 때문이다 — 결함 사례는 드물고, 어떤 결함이 나타날지 미리 열거할 수 없다. 정상 분포만 모델링하면 **"본 적 없는 종류의 결함"도 원리상 탐지 대상**이 된다.

## Details

### 동작 구조

1. **특징 추출** — 사전학습 CNN 의 중간 계층에서 패치 단위 특징을 뽑는다. 최종 계층이 아닌 중간 계층을 쓰는 이유는, 너무 깊으면 ImageNet 분류에 특화되어 미세 텍스처 정보가 사라지기 때문이다.
2. **메모리 뱅크 구축** — 정상 이미지들의 패치 특징을 모두 모은다.
3. **Coreset subsampling** — 뱅크가 그대로면 추론이 느려지므로, 원본 분포를 최대한 보존하는 소수 대표 집합만 남긴다.
4. **추론** — 신규 패치마다 뱅크 내 최근접 이웃까지의 거리를 구한다. 이 거리가 곧 패치의 이상점수이며, 패치 점수를 이미지 좌표에 되돌리면 **Heatmap**, 최댓값 계열 통계를 취하면 **이미지 단위 점수**가 된다.

### 왜 이 사례에서 채택되었나

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|현업과제 제안서]]는 다음 세 조건을 근거로 PatchCore 를 주 모델로 두고, 지도학습 분류(EfficientNet-B0 / ConvNeXt-Tiny)를 비교 baseline 으로 배치했다.

- 기존 PASS/FAIL 판정 이력이 **구조화된 라벨로 저장되어 있지 않아** 지도학습 데이터가 부족하다.
- Particle, Scratch, 오염, 변색, 부식 의심 등 **결함 유형이 다양하고 열려 있다**.
- 담당자가 판정 근거를 확인해야 하므로 **이상 위치의 시각적 제시(Heatmap)** 가 요구된다.

### 한계

- 정상 데이터의 다양성이 곧 성능 상한이다. 정상 범주에 속하지만 뱅크에 없는 변형(촬영 각도, 조명 편차)은 이상으로 오인된다 → [[Patch-based High-Resolution Inspection]] 의 정렬·정규화 전처리가 함께 필요하다.
- 이상점수는 **상대적 거리**일 뿐 확률이 아니다. 운영 임계값을 별도로 정해야 하며, 그 정책이 [[Safety-Critical Threshold Policy]] 다.
- 메모리 뱅크가 커지면 추론 비용이 증가한다 (coreset 이 이를 완화한다).

> [!note] Bias Check
> Counter-argument: "정상만으로 학습하니 라벨이 필요 없다" 는 서술은 과장이다. 임계값 설정과 성능 평가에는 여전히 **FAIL 라벨이 필요**하다. 라벨 부담이 사라지는 게 아니라 학습 단계에서 평가 단계로 이동할 뿐이다.
> Data gap: 이 페이지의 알고리즘 서술(coreset, 중간 계층 특징)은 일반적으로 알려진 내용이며, 현재 인용 가능한 출처는 제안서 한 건뿐이다. 원논문(Roth et al., CVPR 2022) 을 ingest 해 `evidenceScope` 를 `multi-source-primary` 로 올릴 필요가 있다.

> [!question] Open Question
> 이 프로젝트의 5개 View 각각에 대해 **별도 메모리 뱅크를 둘 것인가, 통합 뱅크를 쓸 것인가?** 제안서는 View 별 학습·평가를 우선한다고만 밝히고 뱅크 분리 여부는 명시하지 않았다. View 별 정상 형태가 다르므로 뱅크 분리가 자연스럽지만, View 당 정상 표본 수가 1/5 로 줄어드는 트레이드오프가 있다.

## Related

- [[Visual Anomaly Detection]] — PatchCore 가 속한 상위 문제 범주
- [[Patch-based High-Resolution Inspection]] — 미세 결함을 살리는 입력 처리
- [[Safety-Critical Threshold Policy]] — 이상점수를 PASS/FAIL 로 바꾸는 정책
- [[Multi-View Aggregation]] — 이미지 단위 판정을 실린더 단위로 통합
- [[EfficientNet]] · [[ConvNeXt]] — 비교 baseline 으로 검토된 분류 백본

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §3.5 모델 개발 전략
