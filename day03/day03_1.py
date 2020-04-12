import random

'''
classroomList = [[],[],[]]
teachers = ['袁腾飞','罗永浩',
            '俞洪敏','李永乐','王芳芳'
            ,'马云','李彦宏','马化腾']
for teacher in teachers:
    index = random.randint(0, 2)
    classroom = classroomList[index]
    classroom.append(teacher)
print(classroomList)
'''

classroomList = [[],[],[]]
teachers = ['袁腾飞','罗永浩',
            '俞洪敏','李永乐','王芳芳'
            ,'马云','李彦宏','马化腾']
for classroom in classroomList:
    classroom.append(teachers.pop(random.randint(0, len(teachers)-1)))

for teacher in teachers:
    index = random.randint(0, 2)
    classroom = classroomList[index]
    classroom.append(teacher)

teachers.clear()

print(classroomList)
print(teachers)