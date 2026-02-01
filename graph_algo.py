
# The graph algorithm used for experiments 1, 7, and 8

import matplotlib
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

def experiment(callbacks, datas):
    results = {} 
    for callback in callbacks:
        datas_ = [[*data] for data in datas]
        result = [[], []]
        for i in range(len(datas_)):
            start = timeit.default_timer()
            callback(datas_[i])
            elapsed = timeit.default_timer() - start
            result[0].append(len(datas_[i]))
            result[1].append(elapsed)
        results[callback.__name__] = result
        
    return results

def graph(*callbacks, filePath, title, colors, datas):
    results = experiment(callbacks, datas=datas)
    i = 0
    for result in results:
        plt.plot(results[result][0], results[result][1], color=colors[i], label=result)
        i += 1
    plt.title(title)
    plt.xlabel('Input Size')
    plt.ylabel('Runtime')
    plt.legend()
    plt.savefig(filePath)

