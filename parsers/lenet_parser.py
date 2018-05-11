# Python 2.7
import matplotlib.pyplot as plt
import re
import csv

INPUTS = ["../logs/lenet-training.log", "../logs/lenet-training-2.log"]

def parse_logfile():

    iterations = []
    losses = []
    for input in INPUTS:
        with open(input) as file:
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

    return iterations, losses

def graph_logfile(iterations, losses):
    plt.plot(iterations, losses)
    plt.ylabel('Losses')
    plt.xlabel('Iterations')
    plt.suptitle('LeNet')
    plt.savefig(INPUTS[0] + "-graph.png")

def write_to_file(iterations, losses):
    with open(INPUTS[0] + "_parsed", "wb") as outfile:
        csv_writer = csv.writer(outfile, delimiter=",")
        for i,iteration in enumerate(iterations):
            csv_writer.writerow((iteration, losses[i]))

def main():
    iterations, losses = parse_logfile()
    graph_logfile(iterations, losses)
    # write_to_file(iterations, losses)


if __name__ == '__main__':
    main()
