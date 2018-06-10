#!/usr/local/bin/python
# coding:utf-8



import matplotlib.pyplot as plt  
  
# x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  
# y1=[30,31,31,32,33,35,35,40,47,62,99,186,480]  
  
# x2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  
# y2=[32,32,32,33,34,34,34,34,38,43,54,69,116,271]  
  
# x3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# y3=[30,31,31,32,33,35,35,40,47,62]  
  
# x4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
# y4=[32,32,32,33,34,34,34,34,38,43]  
# group_labels = ['64k', '128k','256k','512k','1024k','2048k','4096k','8M','16M','32M','64M','128M','256M','512M']
group_labels = []
for i in range(1,21):
	  group_labels.append(i)
	  # print 150+150*i
# print len(group_labels)
# print len(ave)

ave = [54.83,58.56,60.04,61.75,64.11,66.47,68.70,70.33,71.99,73.29,74.57,75.55,76.40,77.18,77.90,78.53,79.09,79.64,80.23,80.73]
# plt.title('broadcast(b) vs join(r)') 
ave1 = [52.76,56.01,59.27,62.95,67.13,71.06,74.83,78.05,81.04,83.62,85.78,87.74,89.36,90.66,91.81,92.80,93.65,94.41,95.11,96.02] 
plt.xlabel('Epoch')  
plt.ylabel('Validation Accuracy (%)')  
  
# line1, = plt.plot(x+1,DeterFox,'yo-',label="DeterFox", linestyle="-", linewidth=2,color = 'Black',marker = '<',markersize = 10)
# line2, = plt.plot(x+1,Firefox, 'r.-',label="Firefox",linestyle="--", color = 'Black', marker = '>',markersize = 10)
# line3, = plt.plot(x+1, FuzzyFox, 'o-',label="FuzzyFox", linestyle="-.", linewidth=2, color = 'Black',marker = '*',markersize = 12)
# line4, = plt.plot(x+1, TorBrowser, 'yo-',label="Tor Browser", linestyle="-", color = 'Black',marker = 'D',markersize = 10)
# line5, = plt.plot(x+1, Chrome, 'yo-',label="Chrome", linestyle=":", linewidth=4,color = 'Black',markersize = 10)

#plt.plot(x1, y1,'r', label='broadcast')  
#plt.plot(x2, y2,'b',label='join')  
#plt.xticks(x1, group_labels, rotation=0)  
  
plt.plot(group_labels, ave,'yo-',label="Static Only", linestyle="-", linewidth=2,color = 'Yellow',marker = 'D',markersize = 6)  
plt.plot(group_labels, ave1,'o-',label="Static and Dynamic", linestyle="--", linewidth=2, color = 'Red',markersize = 6)  
# plt.xticks(x3, group_labels, rotation=0)  
 # plt.legend(loc='upper right')
plt.legend(bbox_to_anchor=[0.47, 1])  
# plt.grid()  
# plt.show()  
plt.savefig('vertices.eps', format='eps', dpi=1000)





