import matplotlib.pyplot as plt
import matplotlib.dates
from scipy.io import savemat

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

def plottxTvsV(data,matname):
    res = {}
    for k,v in data.items():
        d = k.strftime('%Y-%m-%d')
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    savemat(matname+".mat",{"x":list(res.keys()), "y":list(res.values())})
    # print(res)
    # plt.plot(list(res.keys()), list(res.values()))
    # plt.show()

    
def plotInterval(sortedData,matname):
    pre = list(sortedData.keys())[0]
    inter = []
    for k,v in sortedData.items():
        inter.append((k-pre).seconds/60)
        pre = k
    savemat(matname+".mat",{"x":inter})
    # plt.hist(inter,bins=24*60)
    # plt.show()

def plotToD(data,matname):
    res = {}
    for d in data.keys():
        h = d.hour
        if h in res:
            res[h] +=1
        else:
            res[h] = 1
    res = dict(sorted(res.items()))
    savemat(matname+".mat",{"x":list(res.keys()), "y":list(res.values())})
    # plt.plot(list(res.keys()),list(res.values()))
    # plt.show()


if __name__ == '__main__':
    dData = getTimeVsValue(readJson(depositData))
    wData = getTimeVsValue(readJson(wdData))

    plottxTvsV(dData,"trend_dep")
    plottxTvsV(wData,"trend_width")

    plotInterval(dData,"interval_dep")
    plotInterval(wData,"interval_width")

    plotToD(dData,"timeofday_dep")
    plotToD(wData,"timeofday_width")