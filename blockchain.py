import datetime as date
import hashlib as hasher
import random as rd #will be used to generate random data

class block:
    def __init__(self,id,previous_block_hash, data):
        self.id = id
        self.date = date.datetime.now()
        self.data=data
        self.previous_block_hash = previous_block_hash
        self.hash=self.hashblock()

    def hashblock(self):
        hash_object = hasher.md5(str(self.data)+str(self.date))
        return hash_object.hexdigest()


class blockchain:
    def __init__(self, max=0):
        self.chain = [self.create_genesis_block()]
        self.max = max

    def create_genesis_block(self):
        return block(0,"blockzero","Block genesis")

    def count(self):
        return len(self.chain)

    def getpreviousblock(self) :
        return self.chain[self.count() - 1]

    def gettopblock(self) :
        return self.chain[self.count() - 1]

    def create_block(self, data):
        previousblock = self.getpreviousblock()
        return block(previousblock.id+1,previousblock.hash,data)

    def addblock(self, data):
        if self.max == 0 or self.count()+1<self.max :
            self.chain.append(self.create_block(data))
        else :
            print "Error : Maximum number of blocks exceeded."

mychain = blockchain()
for _ in xrange(0,10): #lets create 10 blocks and print the result
    b1 = mychain.gettopblock()
    print("id: {}   data : {}  \nhash : {}\nprevious hash : {}\n").format(b1.id,b1.data,b1.hash,b1.previous_block_hash)
    data = rd.random()*100 #data can be of any type
    mychain.addblock(data)

b1 = mychain.gettopblock()
print("id: {}   data : {}  \nhash : {}\nprevious hash : {}\n").format(b1.id,b1.data,b1.hash,b1.previous_block_hash)

print "Our blockchain countains {} blocks.".format(mychain.count())
