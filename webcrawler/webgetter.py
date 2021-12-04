from dataclasses import dataclass
from typing import List
import datetime,sys
import requests
from bs4 import BeautifulSoup as bs
import json,time,random

# bcurl = "https://www.blockchain.com/btc/"
txurl = "https://blockchain.info/rawaddr/"
balurl = "https://blockchain.info/balance?active="
offset = "&offset="

# addrMode = "address/"
# transMode = "tx/"

@dataclass
class BTCTransaction:
    hash: str           # transaction hash
    fee: float          # transaction gas fee
    sender: dict()      # Sender address and value
    receiver: dict()    # receiver address and value
    txTime: datetime.datetime # Transaction time
    TotalTxValue: float # total transaction Value

@dataclass
class BTCAddress:
    hash: str
    numTx: int
    TotRx: float
    TotTx: float
    FBalance: float


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
            # print(txurl+self.haddress+"?"+offset+str(i*50)+"&limit="+str(50 if numTx>50 else numTx))
            tx = self.__getweb(txurl+self.haddress+"?"+offset+str(i*50)+"&limit="+str(50 if numTx>50 else numTx))
            # print(tx)
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
        # print(url+self.mode+self.haddress+"?page="+str(page))
        return json.loads(str(getweb()))

if __name__ == '__main__':
    sampleaddr = "bc1qsm9m9nuhpr8sg0tzrhpkkzsl6nvn5gf4ddjvf8nymc9lufjde6lqu6rxvj"
    w = webgetter(sampleaddr)
    w.getTxs(6)
    w.saveToFile("temp.json")