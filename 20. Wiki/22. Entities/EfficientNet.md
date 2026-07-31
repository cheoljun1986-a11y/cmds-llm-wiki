---
type: wiki-page
aliases:
  - EfficientNet
  - EfficientNet-B0
  - 이피션트넷
description: "Family of convolutional image-classification backbones known for scaling depth, width, and input resolution together rather than one at a time. B0 is the smallest variant and is commonly used as a cheap, pretrained baseline when a project needs a quick answer to whether a supervised classifier is viable at all."
author:
  - Claude
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - model
  - cnn
  - backbone
  - image-classification
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
related:
  - "[[ConvNeXt]]"
  - "[[PatchCore]]"
  - "[[Visual Anomaly Detection]]"
confidence: low
layer: entities
explored: false
claimType: definition
evidenceScope: single-source
verificationStatus: unverified
---

# EfficientNet

## Overview

이미지 분류용 CNN 백본 계열이다. 깊이·너비·입력 해상도를 **따로가 아니라 함께 비율에 맞춰 키운다**는 것이 설계 아이디어이며, 그 결과 같은 연산량 대비 정확도가 높다.

`B0` 는 이 계열의 가장 작은 모델로, 사전학습 가중치를 그대로 가져다 쓰기 좋아 **빠른 baseline** 용도로 자주 선택된다.

## Details

### 이 프로젝트에서의 역할

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|현업과제 제안서]]는 EfficientNet-B0 를 [[ConvNeXt]]-Tiny 와 함께 **분류 baseline** 으로 배치했다. 주 모델은 [[PatchCore]] 이며, 이 둘은 다음 질문에 빠르게 답하기 위한 대조군이다.

> "지도학습 분류만으로도 PASS/FAIL 이 될 만한가?"

이 질문에 답이 나와야 이상탐지를 택한 결정이 근거를 갖는다. baseline 이 이미 충분하다면 더 복잡한 접근을 정당화할 수 없고, baseline 이 실패한다면 라벨 부족이라는 진단이 뒷받침된다.

### 왜 가장 작은 변형인가

B0 를 고른 것은 성능이 아니라 **속도와 비용** 때문으로 보인다. 5 주 프로젝트에서 baseline 은 결론이 아니라 방향 확인 도구이므로, 학습이 빨리 끝나는 편이 유리하다.

> [!note] Bias Check
> Counter-argument: 미세 결함 탐지에서 B0 의 기본 입력 해상도(224×224)는 명백한 제약이다. baseline 이 실패했을 때 그것이 **라벨 부족 때문인지 해상도 때문인지** 구분되지 않으면, 이상탐지 선택의 근거로 쓸 수 없다. [[Patch-based High-Resolution Inspection]] 을 baseline 에도 동일하게 적용해야 공정한 비교가 된다.
> Data gap: 이 페이지는 제안서에서 모델명이 언급된 것 외의 근거가 없다. EfficientNet 원논문(Tan & Le, 2019)을 ingest 하기 전까지 `confidence: low` 로 둔다.

> [!question] Open Question
> baseline 과 [[PatchCore]] 를 **어떤 조건에서 비교할 것인가?** 동일 해상도, 동일 ROI, 동일 데이터 분할이 아니면 비교 결과가 모델 차이인지 전처리 차이인지 알 수 없다.

## Related

- [[ConvNeXt]] — 함께 검토된 또 하나의 baseline 백본
- [[PatchCore]] — 이 baseline 이 대조하는 주 모델
- [[Patch-based High-Resolution Inspection]] — 공정 비교를 위해 함께 적용해야 할 전처리

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §3.5 모델 개발 전략
