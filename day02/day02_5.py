'''
*****************
Date: 2020-04-13
Author: Allen
*****************
'''

namesList = ['林青霞','张曼玉','胡慧中']
name = namesList[1]
print(name)

for name in namesList:
    print(name)

namesList.append('高圆圆')
print(namesList)

namesList = ['林青霞','张曼玉','胡慧中']
namesList.remove('张曼玉')
print(namesList)

namesList = ['林青霞','张曼玉','胡慧中']
namesList[1] = '高圆圆'
print(namesList)

namesList = ['林青霞','张曼玉','胡慧中']
ele = namesList[1]
print(ele)

namesList = ['林青霞','张曼玉','胡慧中']
index = namesList.index('张曼玉')
print(index)

ageList = [90,10,30,20,50,70]
#ageList.sort()
ageList.sort(reverse=True)
print(ageList)

ageList.reverse()
print(ageList)

students = [['林青霞','狄龙','郑少秋'],
            ['张曼玉','梁朝伟']]
student = students[0][2]
print(student)

students[1][0] = '高圆圆'
print(students)