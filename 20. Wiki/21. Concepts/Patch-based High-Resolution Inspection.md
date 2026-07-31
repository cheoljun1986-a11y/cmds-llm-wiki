---
type: wiki-page
aliases:
  - Patch-based High-Resolution Inspection
  - 패치 기반 고해상도 검사
  - ROI 분할 분석
  - Tiled Inference
description: "Input-handling strategy for defects that occupy only a few pixels. Instead of downscaling a high-resolution photo to the network's input size, the image is cropped to a region of interest and split into tiles that are analysed at native resolution, because standard resizing destroys the very evidence being looked for."
author:
  - Claude
model: claude-opus-5
effort: high
date created: 2026-07-31
date modified: 2026-07-31
tags:
  - preprocessing
  - computer-vision
  - resolution
  - roi
source:
  - "[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]]"
related:
  - "[[PatchCore]]"
  - "[[Visual Anomaly Detection]]"
  - "[[Excel 임베디드 이미지 추출]]"
confidence: medium
layer: method
explored: false
claimType: prescriptive
evidenceScope: single-source
verificationStatus: unverified
---

# Patch-based High-Resolution Inspection

## Overview

미세 결함은 **몇 픽셀 크기**다. 일반적인 전처리 관행대로 고해상도 사진을 224×224 로 줄이면, 찾으려는 증거가 리사이즈 과정에서 사라진다.

이 페이지의 원칙은 단순하다 — **줄이지 말고 잘라라**.

## Details

### 문제의 성질

[[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서|제안서]]가 탐지 대상으로 든 것은 Particle, Scratch, 얼룩, 변색, 부식 의심 흔적이다. 이 중 앞의 둘은 전형적으로 **국소적이고 저대비**다. 밸브 전체를 담은 사진에서 스크래치 한 줄이 차지하는 면적 비율은 매우 작다.

이미지를 축소하면 이런 신호는 이웃 픽셀과 평균되어 소멸한다. 축소는 정보를 압축하는 게 아니라 **버리는** 연산이다.

### 두 단계 대응

1. **ROI 설정** — View 별로 검사 대상 영역을 지정해 배경을 제거한다. 실린더 몸통·밸브·배경이 함께 찍혀 있다면, 판정에 무관한 영역을 먼저 잘라내는 것만으로 유효 해상도가 올라간다.
2. **Patch 분할** — 필요하면 ROI 를 여러 타일로 나눠 각각을 원본 해상도로 분석한다. [[PatchCore]] 는 본래 패치 단위로 동작하므로 이 전략과 구조적으로 잘 맞는다.

### 함께 수행되는 정규화

제안서는 다음을 병행한다.

- 소폭의 회전 보정, 위치 정렬
- 밝기·명암 정규화
- 흐림·과노출·가림 여부 확인

이것들은 해상도 문제가 아니라 **정상 분포를 좁히기 위한** 처리다. 이상탐지는 정상의 변동폭이 클수록 성능이 떨어지므로, 촬영 편차를 미리 걷어내면 같은 모델로도 탐지력이 올라간다.

### 데이터 증강의 절제

제안서는 증강을 **"실제 현장에서 발생 가능한 범위 내에서만 제한적으로"** 적용한다고 못 박았다. 이상탐지에서 이는 중요한 제약이다 — 현장에서 일어나지 않는 변형까지 정상으로 학습시키면 정상 분포가 부풀려지고, 진짜 이상이 그 안에 묻힌다. 분류 모델에서 통용되는 "증강은 많을수록 좋다" 는 직관이 여기서는 역작용한다.

### 상류 조건: 원본 화질 확보

이 모든 전략은 **입력 이미지가 원본 화질을 유지하고 있을 때만** 의미가 있다. 이미지가 Excel 에 삽입되는 과정에서 이미 압축 손실이 발생했다면 복원할 수 없다. 그래서 [[Excel 임베디드 이미지 추출]] 이 단순한 파일 처리 작업이 아니라 **해상도 보존 문제**로 다뤄진다.

> [!note] Bias Check
> Counter-argument: 패치 분할은 연산량과 오탐을 함께 늘린다. 타일 수가 많아질수록 각 타일이 독립적으로 오경보를 낼 기회가 생기며, 이는 [[Multi-View Aggregation]] 에서 본 오탐 누적과 같은 구조다. 타일 수와 임계값을 함께 조정해야 한다.
> Data gap: 실제 이미지의 해상도, 결함의 전형적 픽셀 크기, 압축 품질이 확인되지 않았다. 이 수치가 나와야 타일 크기를 근거 있게 정할 수 있다.

> [!question] Open Question
> **타일 경계에 걸친 결함은 어떻게 처리하는가?** 겹침(overlap)을 두는 것이 일반적 해법이지만 연산량이 증가한다. 제안서는 Patch 분할을 언급하되 겹침 여부와 타일 크기를 정하지 않았다.

## Related

- [[PatchCore]] — 패치 단위로 동작하는 주 모델
- [[Excel 임베디드 이미지 추출]] — 원본 화질을 지키는 상류 단계
- [[Visual Anomaly Detection]] — 정상 분포를 좁히는 것이 성능인 문제 설정
- [[Multi-View Aggregation]] — 분할 수 증가가 오탐을 누적시키는 같은 구조

## Sources

- [[2026-07-31-PatchCore-반도체-특수가스-용기-표면-이상탐지-제안서]] — §3.3 이미지 전처리 및 촬영 View 정리, §6 예상 어려움
