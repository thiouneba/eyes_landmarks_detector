# Eyes Landmarks Predictor

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white)
![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=w3c&logoColor=white)
![dlib](https://img.shields.io/badge/dlib-008000?style=for-the-badge&logo=c%2B%2B&logoColor=white)

> **Academic context:** This project was completed between October 2022 and March 2023 as a 6-month supervised project (*projet tutoré*) as part of an MSc in Computer Science — Images & Multimedia Data track.

---

## Project Overview

This project focuses on training a **custom dlib shape predictor** to detect and localize eye landmarks on facial images. The trained model is then applied to predict the precise (x, y)-coordinates of eye keypoints on unseen input images.

**Shape predictors** (also known as landmark predictors) are supervised machine learning models designed to locate specific structural keypoints within a region of interest in an image. The most widely known application is dlib's **68-point facial landmark detector**, which can localize the following facial structures:

- Eyes
- Eyebrows
- Nose
- Lips / Mouth
- Jawline

While facial landmark detection is the canonical use case, shape predictors can be trained to localize any set of structural points — this project demonstrates that by training a **specialized eye-only predictor** from scratch using custom annotated data.

---

## Motivation & Applications

Eye landmark detection is a foundational building block for a wide range of computer vision applications, including:

- **Eye alignment** — normalizing eye positions across images to improve face recognition accuracy
- **Drowsiness detection** — monitoring eye openness (Eye Aspect Ratio) for driver safety systems
- **Gaze estimation** — inferring where a person is looking
- **Augmented reality** — anchoring virtual elements (glasses, effects) to the eye region
- **Medical imaging** — detecting ocular conditions from facial or ophthalmic images

---

## Methodology

### 1. Data Annotation

Eye landmark positions were manually annotated using XML-based annotation files compatible with dlib's training pipeline. Each annotation defines the bounding box of the face/eye region and the (x, y) coordinates of each landmark point.

### 2. Model Training

A custom dlib shape predictor was trained using the annotated dataset. Key training parameters (tree depth, number of trees, oversampling factor, regularization) were tuned to balance accuracy and inference speed.

### 3. Landmark Prediction

The trained `.dat` model file was then used to run inference on new input images, returning the predicted eye landmark coordinates overlaid on the original image for visual validation.

### 4. Evaluation & Visualization

Results were analyzed and visualized using both **Python** (OpenCV, dlib) and **MATLAB** to assess prediction quality across different face orientations, lighting conditions, and eye states (open/closed).

---

## Results

The figures below illustrate the predictor's output at various stages of the pipeline — from raw detection to precise landmark localization on diverse input images.

<img src="https://github.com/thiouneba/eyes_landmarks_detector/blob/main/eyesland1.PNG" width="500" />

<img src="https://github.com/thiouneba/eyes_landmarks_detector/blob/main/eyesland2.PNG" width="500" />

<img src="https://github.com/thiouneba/eyes_landmarks_detector/blob/main/eyesland3.PNG" width="500" />

<img src="https://github.com/thiouneba/eyes_landmarks_detector/blob/main/eyesland4.PNG" width="500" />

<img src="https://github.com/thiouneba/eyes_landmarks_detector/blob/main/eyesland5.PNG" width="500" />

<img src="https://github.com/thiouneba/eyes_landmarks_detector/blob/main/eyesland6.PNG" width="500" />

<img src="https://github.com/thiouneba/eyes_landmarks_detector/blob/main/eyesland7.PNG" width="500" />

---

## Tech Stack

| Tool / Library | Role |
|----------------|------|
| Python | Main development language — training pipeline, inference, visualization |
| dlib | Shape predictor training and facial landmark detection |
| OpenCV | Image loading, preprocessing, and landmark overlay |
| MATLAB | Data analysis and result visualization |
| XML | Annotation format for dlib training data |

---

## Project Structure

```
eyes_landmarks_predictor/
├── data/
│   ├── annotations/        # XML annotation files (dlib format)
│   └── images/             # Training and test images
├── train/
│   └── train_predictor.py  # Training script with configurable hyperparameters
├── predict/
│   └── predict_landmarks.py # Inference script on new images
├── models/
│   └── eyes_predictor.dat  # Trained dlib shape predictor
└── results/                # Output images with predicted landmarks
```

---

## References

- King, D.E. (2009). Dlib-ml: A Machine Learning Toolkit. *Journal of Machine Learning Research*, 10, 1755–1758.
- Kazemi, V., & Sullivan, J. (2014). One millisecond face alignment with an ensemble of regression trees. *CVPR 2014*.
- Soukupová, T., & Čech, J. (2016). Real-time eye blink detection using facial landmarks. *CVWW 2016*.
