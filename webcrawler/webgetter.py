from typing import List
import sys
import requests
from bs4 import BeautifulSoup as bs
import json,time,random

# bcurl = "https://www.blockchain.com/btc/"
txurl = "https://blockchain.info/rawaddr/"
balurl = "https://blockchain.info/balance?active="
offset = "&offset="


class webgetter():
    def __init__(self,hashAddr) -> None:
        self.haddress = str(hashAddr)
        bal = self.getBalance()
        assert bal[hashAddr]
        self.ntx = int(bal[hashAddr]["n_tx"])
        print("This addr ",self.haddress," contains ",self.ntx," txs.")
        self.data = None
    
    def getTxs(self,numTx:int=sys.maxsize):
        numTx = min(self.ntx,numTx)
        for i in range((numTx//50)+1):
            tx = self.__getweb(txurl+self.haddress+"?"+offset+str(i*50)+"&limit="+str(50 if numTx>50 else numTx))
            if i ==0:
                self.data = tx
            else:
                self.data["txs"].append(tx["txs"])
            time.sleep(random.uniform(0.1, 1))
        
        
    def saveToFile(self,fname):
        with open(fname, 'w') as outfile:
            json.dump(self.data, outfile)
            
    def getBalance(self):
        return self.__getweb(balurl+self.haddress)

    def __getweb(self,url):
        getweb = lambda : bs(requests.get(url).text,'html.parser')
        return json.loads(str(getweb()))

if __name__ == '__main__':
    sampleaddr = "31w8Lc9V34ZYyYMycPcQjjkuBWLn8oYmxd"
    w = webgetter(sampleaddr)
    w.getTxs()
    w.saveToFile("widthdraw.json")