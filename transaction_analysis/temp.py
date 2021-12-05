import json,copy

depositData = "../data/deposite.json"
wdData = "../data/widthdraw.json"


fname = depositData

with open(fname) as f:
    content = json.load(f)

pcon = copy.deepcopy(content)
pcon["txs"] = []

for tx in list(content["txs"]):
    if type(tx) is list:
        pcon["txs"].extend(tx)
    else:
        pcon["txs"].append(tx)

print(pcon["n_tx"],len(pcon["txs"]))
with open("deposite.json", 'w') as outfile:
    json.dump(pcon, outfile)