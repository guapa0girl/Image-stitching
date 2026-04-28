import cv2 as cv
import numpy as np

class SimpleStitcher:
    def __init__(self):
        # SIFT 특징점 검출기 생성
        self.finder = cv.SIFT_create()

    def stitch(self, img_left, img_right):
        # 1. 특징점 찾기 및 기술자(Descriptor) 계산
        kp1, des1 = self.finder.detectAndCompute(img_left, None)
        kp2, des2 = self.finder.detectAndCompute(img_right, None)

        # 2. 특징점 매칭 (Brute-Force Matcher)
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des2, des1, k=2)

        # 3. 좋은 매칭점 선별 (Lowe's ratio test)
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)

        if len(good_matches) > 4:
            # 4. Homography 행렬 계산
            src_pts = np.float32([kp2[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp1[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            H, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

            # 5. 이미지 워핑 (Warping)
            h1, w1 = img_left.shape[:2]
            h2, w2 = img_right.shape[:2]
            
            # 결과 이미지 크기 설정 (오른쪽으로 확장된다고 가정)
            result = cv.warpPerspective(img_right, H, (w1 + w2, h1))
            
            # 6. 이미지 합성 및 가산점용 간단 블렌딩 (Alpha Blending 효과)
            # 왼쪽 이미지를 결과 이미지의 왼쪽 부분에 덮어씌움
            result[0:h1, 0:w1] = img_left
            
            return result
        else:
            print("매칭점이 부족합니다.")
            return None

# 실행 예시
if __name__ == "__main__":
    # 이미지 로드 (직접 찍은 사진 파일명으로 변경하세요)
    img1 = cv.imread('image1.jpg')
    img2 = cv.imread('image2.jpg')
    img3 = cv.imread('image3.jpg')

    stitcher = SimpleStitcher()
    
    # 1단계: 1번과 2번 합성
    intermediate = stitcher.stitch(img1, img2)
    
    # 2단계: 결과물과 3번 합성
    if intermediate is not None:
        final_result = stitcher.stitch(intermediate, img3)
        
        if final_result is not None:
            cv.imshow("Final Panorama", final_result)
            cv.imwrite("stitching_result.jpg", final_result)
            cv.waitKey(0)