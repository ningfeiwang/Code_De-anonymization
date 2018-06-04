# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


n_groups = 30

means_men = (11,10,12,15,16,1,4,7,9,1,1,5,6,2,5,2,5,10,0,0,0,0,0,0,0,0,0,0,0,0)
# means_men = (1,3,2,5,4,6,8,11,10,13,1,1,2,1,2,1,6,1,1,1,1,5,1,1,2,6,1,2,4,2)
# std_men = (2, 3, 4, 1, 2)

# means_women = (25, 32, 34, 20, 25)
# std_women = (3, 5, 2, 3, 3)

fig, ax = plt.subplots()

index = np.arange(n_groups)
my_y_ticks = np.arange(0, 18, 1) 
bar_width = 0.7

opacity = 0.4
# error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, means_men,
                alpha=opacity, color='y')

# rects2 = ax.bar(index + bar_width, means_women, bar_width,
#                 alpha=opacity, color='r', error_kw=error_config,
#                 label='Women')

ax.set_xlabel('Memory Address')
ax.set_ylabel('Operations Times')
# ax.set_title('Scores by group and gender')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('1', '2', '3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'))
# ax.set_yticklabels(('0', '','1', '2', '3', '4'))
# plt.axis([1,10,0,4])
plt.yticks(my_y_ticks)
ax.legend()

# fig.tight_layout()
# plt.show()
plt.savefig('large.eps', format='eps', dpi=1000)
# plt.savefig('small.eps', format='eps', dpi=1000)



# # Credit: Josh Hemann

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator
# from collections import namedtuple


# n_groups = 30


# # std_men = (2, 3, 4, 1, 2)

# # means_women = (25, 32, 34, 20, 25)
# # std_women = (3, 5, 2, 3, 3)

# fig, ax = plt.subplots()

# index = np.arange(n_groups)
# my_y_ticks = np.arange(0, 18, 1) 
# # my_x_ticks = np.arange(0, 29, 1) 
# bar_width = 0.7

# opacity = 0.4
# # error_config = {'ecolor': '0.3'}

# rects1 = ax.bar(index, means_men,
#                 alpha=opacity, color='y')

# # rects2 = ax.bar(index + bar_width, means_women, bar_width,
# #                 alpha=opacity, color='r', error_kw=error_config,
# #                 label='Women')

# ax.set_xlabel('Memory Address')
# ax.set_ylabel('Operations Times')
# # ax.set_title('Scores by group and gender')
# ax.set_xticks(index + bar_width / 2)

# # ax.set_yticklabels(('0', '','1', '2', '3', '4'))
# # plt.axis([1,10,0,4])
# # plt.xticks(my_x_ticks)
# plt.yticks(my_y_ticks)
# ax.legend()

# # fig.tight_layout()
# # plt.show()
# plt.savefig('large.eps', format='eps', dpi=1000)
# # plt.savefig('small.eps', format='eps', dpi=1000)