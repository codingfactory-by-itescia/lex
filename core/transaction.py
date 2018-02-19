class Transaction:
    def __init__(self):
        this.id
        this.vIn
        this.vOut

    def new_coinbase(self, to, data):
            if data == "":
                data = 'Reward to %d' % data

            txIn = TxInput(None, -1, data)
            txOut = TxOutput(subsidy, to)
            tx = Transaction(None, txIn, txOut)

            return tx
    
class TxOutput:
    def __init__(self, value, scriptPubKey):
        this.value = value
        this.scriptPubKey = scriptPubKey
        

class TxInput:
    def __init__(self, txId, vOut, sig):
        this.txId = txId
        this.vOut = vOut
        this.ScriptSig = sig