# Vowel Detector

This project was part of the AI Hackathon competition I participated in. The competition provided data for participants to build models capable of recognizing gender, race, age, mask-wearing status, skin tone, and emotions. You can refer to the project repo for this competition here: [face-analysis](https://github.com/tranductri2003/face-analysis).

## Our Results

- Our model achieved an accuracy of 77% in predicting the skin tone of individuals in images, based on four color bands: dark, mid-dark, mid-light, and light.
- Loss/Accuracy:
![Accuracy Image](https://github.com/tranductri2003/skin-tone-detector/assets/89126960/475b9fd5-0734-4b17-bbdb-22fd0b1613e9)
- Confusion Matrix and Classification Report: 
![Confusion Matrix](https://github.com/tranductri2003/skin-tone-detector/assets/89126960/8ed367f1-0019-4d31-9180-4ccd41e19b52)

(Note: In the above repo, the model reached an accuracy of 77%, but I have lost the images and data set used for evaluating the model, so I am using images with a similar accuracy - 75%.)

Other models from the competition can be found at [face-analysis](https://github.com/tranductri2003/face-analysis).

## Installation
The source code for the above problem, complete with detailed comments, is available for running and verification. If you want to predict skin tone on a different range, you can divide the data set according to the skin tones you desire and run the cell CREATE SKIN-ONLY DATA to divide the data set into the desired skin tone folders. Note that as this is only a small module of the competition, for accurate model prediction, you need to pass images after cropping the face. The face-analysis repo mentioned above has other models to determine the facial position to use as input parameters for this model. Feel free to contact me with any questions.
