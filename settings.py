import numpy as np

num_joint = 18#关节点数

# clip length帧数
L = 18
#winWidth = 1280
winWidth = 640
#winHeight = 720
winHeight = 480

move_status = ['', 'stand', 'sit', 'stand']
#move_status = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , '10', '11']

c = np.random.rand(32, 3) * 255
sort_max_age = 20
sort_min_hit = 3

