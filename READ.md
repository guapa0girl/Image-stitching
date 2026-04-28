# 📸 Image Stitching

**Description:** OpenCV를 활용하여 직접 구현한 특징점 기반 자동 이미지 스티칭하기

---

## 🎯 과제 목표 (Mission)

[cite_start]본 프로젝트는 여러 장의 이미지를 자동으로 정합(Stitching)하여 하나의 넓은 시야를 가진 큰 이미지를 생성하는 것을 목표로 합니다.

### ✅ 필수 구현 사항 (Mandatory)

- **데이터 획득:** 직접 촬영한 오버랩(Overlap)이 존재하는 3장 이상의 이미지 세트를 사용하였습니다.
- **직접 구현:** `cv::Stitcher`와 같은 고수준 API를 사용하지 않고, 특징점 추출부터 최종 워핑(Warping)까지의 전 과정을 직접 구현하여 감점 요인을 제거하였습니다.
- **Planar View:** 이미지 간의 3차원 깊이 변화가 크지 않은 평면 뷰(Planar View) 방식을 적용하였습니다.

---

## ✨ 추가 기능 (Added Features)

단순한 이미지 결합을 넘어 품질을 높이기 위해 다음 기능을 추가로 구현하고 설명합니다.

- **Image Blending (가중치 기반 이미지 블렌딩):** 이미지 간의 연결 부위를 부드럽게 처리하기 위해 알파 블렌딩 기법을 적용하였습니다. 이를 통해 서로 다른 노출이나 그림자로 인해 발생하는 경계선의 이질감을 최소화하였습니다.

---

## 🛠 알고리즘 파이프라인 (Implementation Details)

[cite_start]본 프로그램은 다음과 같은 고전적인(Classical) 컴퓨터 비전 파이프라인을 따릅니다.

1.  **Feature Extraction:** SIFT(Scale-Invariant Feature Transform)를 사용하여 이미지의 고유 특징점을 추출합니다.
2.  **Image Matching:** 추출된 기술자(Descriptor)를 비교하여 이미지 간의 오버랩 영역을 찾습니다.
3.  **Homography Estimation:** RANSAC 알고리즘을 통해 신뢰할 수 있는 매칭 쌍을 선별하고 투영 변환 행렬(Homography)을 계산합니다.
4.  **Perspective Warping:** 계산된 행렬을 바탕으로 이미지를 평면상에 정합합니다.
5.  **Multi-image Stitching:** 3장 이상의 이미지를 순차적으로 결합하여 최종 파노라마를 생성합니다.

---

## 🖼 실행 결과 (Screenshots)

|        원본 이미지 1        |        원본 이미지 2        |        원본 이미지 3        |
| :-------------------------: | :-------------------------: | :-------------------------: |
| ![Source1](images/img1.jpg) | ![Source2](images/img2.jpg) | ![Source3](images/img3.jpg) |

### 🏆 최종 결과물 (Final Panorama)

![Final Result](result/panorama_result.jpg)
