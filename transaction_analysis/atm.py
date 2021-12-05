import matplotlib.pyplot as plt
import matplotlib.dates

import collections as col
from datetime import date, datetime
import json

from heristics import txOutputs

depositData = "../data/deposite.json"
wdData = "../data/widthdraw.json"
sampleD = "../data/sample.json"

approxUSD = 60000
bitV = 1e8

def readJson(jsf):
    with open(jsf) as f:
        return json.load(f)

def getTimeVsValue(jsc):
    d = {}
    u2t = lambda ut : datetime.utcfromtimestamp(ut) # strftime('%Y-%m-%d %H:%M:%S')
    for tx in jsc["txs"]:
        d[u2t(tx["time"])] = [x/bitV*approxUSD for x in txOutputs(tx).values()]
    return dict(sorted(d.items()))

def plottxTvsV(data):
    # f,b = None,None
    res = {}
    for k,v in data.items():
        d = k.strftime('%Y-%m-%d')
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
        # if not f or not b:
        #     f = k
        #     b = k
        # if k < f:
        #     f = k
        # if k > b:
        #     b = k
    print(res)
    plt.plot(list(res.keys()), list(res.values()))
    plt.show()

    
def plotInterval(sortedData):
    pre = list(sortedData.keys())[0]
    inter = []
    for k,v in sortedData.items():
        inter.append((k-pre).seconds/60)
        pre = k
    
    plt.hist(inter,bins=24*60)
    plt.show()

def plotToD(data):
    res = {}
    for d in data.keys():
        h = d.hour
        if h in res:
            res[h] +=1
        else:
            res[h] = 1
    res = dict(sorted(res.items()))
    plt.plot(list(res.keys()),list(res.values()))
    plt.show()


if __name__ == '__main__':
    # plottxTvsV(getTimeVsValue(readJson(depositData)))
    # plottxTvsV(getTimeVsValue(readJson(wdData)))
    # plotInterval(getTimeVsValue(readJson(wdData)))
    plotToD(getTimeVsValue(readJson(wdData)))