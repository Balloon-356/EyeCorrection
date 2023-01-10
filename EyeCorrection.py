
import numpy as np

num_left = 28 + 1
num_right = 33 + 1
w_eye = 61.285

graph_num_left = [1, 5, 4, 5, 5, 4, 5]
graph_num_right = [5, 5, 4, 5, 5, 5, 4, 1]

pixel_list = list(range(-num_left+1, num_right+1))

if sum(graph_num_left) != num_left:
    print('graph_num_left != num_left !')
    exit()
if sum(graph_num_right) != num_right:
    print('graph_num_right != num_right !')
    exit()
    
graph_list_left = []
for i in range(len(graph_num_left)):
    j = i - len(graph_num_left) + 1 
    graph_list_left += [j]*graph_num_left[i]

graph_list_right = []
for i in range(len(graph_num_right)):
    j = i + 1
    graph_list_right += [j]*graph_num_right[i]

graph_list = graph_list_left + graph_list_right


# # set w_eye=61
# for d in range(200):
#     dw = (d-100) / 100.0
#     w = (w_eye + dw) / 13.0
#     lower_list = []
#     upper_list = []
#     for i in range(len(pixel_list)):
#         lower_list.append(pixel_list[i]-graph_list[i]*w)
#         upper_list.append(pixel_list[i]-(graph_list[i]-1)*w)

#     lower_bound = max(lower_list)
#     upper_bound = min(upper_list)

#     if lower_bound < upper_bound:
#     print('{0}, True, lower:{1:.4f}, upper:{2:.4f}, margin:{3:.4f}'.format(w_eye + dw, lower_bound, upper_bound, upper_bound-lower_bound))
#     rotation_per_pixel = 0.03187
#     print('correction:{0:.3f}-{1:.3f}'.format(lower_bound*rotation_per_pixel, upper_bound*rotation_per_pixel))

w = w_eye / 13.0

lower_list = []
upper_list = []

for i in range(len(pixel_list)):
    lower_list.append(pixel_list[i]-graph_list[i]*w)
    upper_list.append(pixel_list[i]-(graph_list[i]-1)*w)

lower_bound = max(lower_list)
upper_bound = min(upper_list)

flag = lower_bound < upper_bound
print('{0}, lower:{1:.4f}, upper:{2:.4f}, margin:{3:.4f}'.format(flag, lower_bound, upper_bound, upper_bound-lower_bound))

rotation_per_pixel = 0.03187
print('correction:{0:.3f}-{1:.3f}'.format(lower_bound*rotation_per_pixel, upper_bound*rotation_per_pixel))

print('Done!')
