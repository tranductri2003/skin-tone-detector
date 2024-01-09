def allotSkin(colorsList):
    colors = [
        [59, 34, 25],   #Dark_Skin
        [161, 110, 75], #Mid_Dark_Skin
        [212, 170, 120],#Mid_Light_Skin
        [230, 188, 152],#light_Skin
    ]

    diffList = []
    for i in range(4):
        diff = diffColor(colorsList, colors[i])
        diffList.append(diff)
        # list.append(elem)
    
    indexOfMinDist = diffList.index(min(diffList))
    # print(colors[indexOfMinDist])
    allotedSkinTone = colors[indexOfMinDist]
    
    if indexOfMinDist == 0:
        color = "dark"
    elif indexOfMinDist == 1:
        color = "mid-dark"
    elif indexOfMinDist == 2:
        color = "mid-light"
    else:
        color = "light"
        
    return color


def diffColor(colorsList,colorX):
    x1 = abs(colorsList[0]-colorX[0])
    x2 = abs(colorsList[1]-colorX[1])
    x3 = abs(colorsList[2]-colorX[2])
    x = int(x1+x2+x3)
    return x
