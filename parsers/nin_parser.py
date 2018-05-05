# Python 2.7
import matplotlib.pyplot as plt
import re
import csv

INPUTS = ["../logs/nin-training.log", "../logs/nin-training-2.log"]

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

    _iterations = []
    for i in range(len(iterations)):
        iter = iterations[i]
        if iter not in _iterations:
            _iterations.append(iter)

    _iterations = _iterations[:len(losses)]

    return _iterations, losses

def graph_accuracies():
    accuracies_top_1 = []
    accuracies_top_2 = []
    accuracies_top_3 = []
    for input in INPUTS:
        with open(input) as file:
            for line in file:

                match_obj = re.search(r"accuracy_top_1 = [+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", line)
                if match_obj:
                    group_items = match_obj.group(0).split(' ')
                    accuracy = group_items[2]
                    accuracies_top_1.append(float(accuracy))

                match_obj = re.search(r"accuracy_top_2 = [+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", line)
                if match_obj:
                    group_items = match_obj.group(0).split(' ')
                    accuracy = group_items[2]
                    accuracies_top_2.append(float(accuracy))

                match_obj = re.search(r"accuracy_top_3 = [+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?", line)
                if match_obj:
                    group_items = match_obj.group(0).split(' ')
                    accuracy = group_items[2]
                    accuracies_top_3.append(float(accuracy))

    epochs = list(range(1, len(accuracies_top_1)+1))

    plt.plot(epochs, accuracies_top_1, 'r', label="Top 1 Accuracy")
    plt.plot(epochs, accuracies_top_2, 'b', label="Top 2 Accuracy")
    plt.plot(epochs, accuracies_top_3, 'g', label="Top 3 Accuracy")
    plt.legend(loc='lower right')

    plt.ylabel('Accuracies')
    plt.xlabel('Epochs')
    plt.suptitle('Network in Network')
    plt.savefig("nin-accuracies.png")



def graph_logfile(iterations, losses):
    plt.plot(iterations, losses)
    plt.ylabel('Losses')
    plt.xlabel('Iterations')
    plt.suptitle('Network in Network')
    plt.savefig(INPUTS[0] + "-graph.png")

def write_to_file(iterations, losses):
    with open(INPUTS[0] + "_parsed", "wb") as outfile:
        csv_writer = csv.writer(outfile, delimiter=",")
        for i,iteration in enumerate(iterations):
            csv_writer.writerow((iteration, losses[i]))

def main():
    iterations, losses = parse_logfile()
    # graph_logfile(iterations, losses)
    # write_to_file(iterations, losses)
    graph_accuracies()


if __name__ == '__main__':
    main()
