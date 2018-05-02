# Python 2.7
import matplotlib.pyplot as plt
import re
INPUT = "./logs/alexnet-training.log"

iterations = []
losses = []
with open(INPUT) as file:
    for line in file:
        match_obj = re.search(r"Iteration [+-]?\d+(?:\.\d+)?", line)
        if match_obj:
            group_items = match_obj.group(0).split(' ')
            iter_num = group_items[1]
            iterations.append(int(iter_num))

        match_obj = re.search(r"loss = [+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", line)
        if match_obj:
            group_items = match_obj.group(0).split(' ')
            loss = group_items[2]
            losses.append(float(loss))


plt.plot(iterations, losses)
plt.show()
