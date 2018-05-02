# Python 2.7
import matplotlib.pyplot as plt
import re
import csv

INPUT = "../logs/alexnet-training.log"

def parse_logfile():

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

    _iterations = []
    _losses = []
    for i in range(len(iterations)):
        iter = iterations[i]
        if iter not in _iterations:
            _iterations.append(iter)
            _losses.append(losses[i])

    return _iterations, _losses

def get_accuracies():
    iterations = []
    accuracies = []
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
                accuracy = group_items[2]
                accuracies.append(float(loss))

    _iterations = []
    _accuracies = []
    for i in range(len(iterations)):
        iter = iterations[i]
        if iter not in _iterations:
            _iterations.append(iter)
            _accuracies.append(accuracies[i])

    return _iterations, _accuracies

def graph_logfile(iterations, losses):
    plt.plot(iterations, losses)
    plt.savefig(INPUT + "-graph.png")

def graph_logfile(iterations, accuracies):
    plt.plot(iterations, accuracies)
    plt.savefig(INPUT + "-accuracies-graph.png")

def write_to_file(iterations, losses):
    with open(INPUT + "_parsed", "wb") as outfile:
        csv_writer = csv.writer(outfile, delimiter=",")
        for i,iteration in enumerate(iterations):
            csv_writer.writerow((iteration, losses[i]))

def main():
    iterations, accuracies = get_accuracies()
    graph_accuracies(iterations, accuracies)


if __name__ == '__main__':
    main()
