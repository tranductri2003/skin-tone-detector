# I've left some code in comments so that it can be easier if one wants to test and see output at various points. To make things simpler just remove the commented code !

import face_detect
import kMeansImgPy
import cv2
import allotSkinTone
import skin_detector

import csv
from collections import defaultdict 
import matplotlib.pyplot as plt


def create_map_from_csv(file_path):
    result_map = {}
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            if len(row) >= 3:  # Đảm bảo có ít nhất 3 giá trị trên hàng
                key = row[0]
                value = row[-3]
                result_map[key] = value
                image_data.append(key)
    
    return result_map

def visualize_color(rgb_values):
    # Tạo một hình ảnh với một pixel màu RGB được chỉ định
    color_image = [[rgb_values]]

    # Hiển thị hình ảnh
    plt.imshow(color_image)
    plt.axis('off')
    plt.show()



csv_file_path = "D:\Code\BachKhoa\AI Hackathon\labels.csv"
image_data = []
label_map = create_map_from_csv(csv_file_path)
image_data = image_data[1:]
image_path = "D:\Code\BachKhoa\AI Hackathon\mnt\md0\projects\sami-hackathon\private\data"



count = 0
diffusion_matrix = defaultdict(lambda: defaultdict(lambda: 0))
for img in image_data:
    print(img)
    img_link = image_path + "/" + img
    image = cv2.imread(img_link)
    cv2.imshow("Image", image)
    
    # Detect face and extract
    skin_extracted = skin_detector.process(image)
    cv2.imshow("Skin", skin_extracted)

    if skin_detector is not None:
        # Pass extracted face to kMeans and get Max color list 
        colorsList = kMeansImgPy.kMeansImage(skin_extracted)
        
        print("color list: ", colorsList)
        for i in range(3):
            colorsList[i] = int(colorsList[i])
            
        visualize_color(colorsList)

        # Allot the actual skinTone to a certain shade
        allotedSkinToneVal = allotSkinTone.allotSkin(colorsList)

        print(f"\033[91mImage: {img}. PREDICT: {allotedSkinToneVal}. LABEL: {label_map[img]}\033[0m")
        diffusion_matrix[label_map[img]][allotedSkinToneVal]+=1
        count+=1
        if count==100:
            break
    
    
    
    
print("           Dark     Mid-Dark     Mid-Light     Light")
print(f"Dark      {diffusion_matrix['dark']['dark']}           {diffusion_matrix['dark']['mid-dark']}               {diffusion_matrix['dark']['mid-light']}             {diffusion_matrix['dark']['light']}")
print(f"Mid-Dark   {diffusion_matrix['mid-dark']['dark']}           {diffusion_matrix['mid-dark']['mid-dark']}               {diffusion_matrix['mid-dark']['mid-light']}             {diffusion_matrix['mid-dark']['light']}")
print(f"Mid-Light  {diffusion_matrix['mid-light']['dark']}           {diffusion_matrix['mid-light']['mid-dark']}               {diffusion_matrix['mid-light']['mid-light']}             {diffusion_matrix['mid-light']['light']}")
print(f"Light     {diffusion_matrix['light']['dark']}           {diffusion_matrix['light']['mid-dark']}               {diffusion_matrix['light']['mid-light']}             {diffusion_matrix['light']['light']}")

