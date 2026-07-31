---
type: wiki-page
aliases:
  - ConvNeXt
  - ConvNeXt-Tiny
  - 컨브넥스트
description: "Convolutional image-classification backbone family redesigned by borrowing architectural choices from vision transformers while staying fully convolutional. Tiny is the smallest variant and serves as a modern, pretrained baseline alongside older CNNs."
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
  - "[[EfficientNet]]"
  - "[[PatchCore]]"
  - "[[Visual Anomaly Detection]]"
confidence: low
layer: entities
explored: false
claimType: definition
evidenceScope: single-source
verificationStatus: unverified
---

# ConvNeXt

## Overview

Vision Transformer 계열에서 효과가 확인된 설계 요소들을 **CNN 구조 안으로 다시 가져온** 백본 계열이다. 어텐션을 쓰지 않고 합성곱만으로 구성되어 있으면서 트랜스포머급 성능을 목표로 한다.

`Tiny` 는 가장 작은 변형으로, [[EfficientNet]]-B0 와 비슷한 위치 — 즉 **사전학습 가중치를 이용한 빠른 baseline** — 에서 쓰인다.

## Details

### 이 프로젝트에서의 역할

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|현업과제 제안서]]는 ConvNeXt-Tiny 를 [[EfficientNet]]-B0 와 함께 분류 baseline 후보로 명시했다. 둘 중 하나를 고르는 것이 아니라 **"사전학습된 분류기" 라는 접근 자체**를 대표하는 대조군으로 보는 편이 정확하다.

두 모델을 나란히 두는 실질적 이득은 백본 세대 차이를 통제하는 데 있다 — 구형(2019 계열)과 신형(2022 계열) 모두에서 실패한다면, 실패 원인이 특정 아키텍처가 아니라 **데이터·라벨 조건**에 있다는 진단이 강해진다.

> [!note] Bias Check
> Counter-argument: baseline 을 두 개 두는 것이 항상 정보를 늘리지는 않는다. 둘 다 ImageNet 사전학습 CNN 이라 실패 양상이 유사할 가능성이 높고, 5 주 일정에서 두 번째 baseline 의 한계 효용은 낮을 수 있다.
> Data gap: 제안서는 모델명만 언급하며 선택 근거를 밝히지 않았다. ConvNeXt 원논문(Liu et al., 2022)이 ingest 되기 전까지 `confidence: low` 로 둔다.

> [!question] Open Question
> ConvNeXt-Tiny 를 [[PatchCore]] 의 **특징 추출 백본**으로도 쓸 것인가? PatchCore 는 사전학습 백본의 중간 계층 특징을 사용하므로 백본 선택이 이상탐지 성능에도 직접 영향을 준다. 제안서는 이를 분류 baseline 맥락에서만 언급했다.

## Related

- [[EfficientNet]] — 함께 검토된 또 하나의 baseline 백본
- [[PatchCore]] — 특징 추출 백본으로도 연결될 수 있는 주 모델
- [[Visual Anomaly Detection]] — 이 baseline 들이 대조하는 문제 설정

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §3.5 모델 개발 전략
