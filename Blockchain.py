import hashlib
import json
import time

class Block:
	blockNo = 0
	data = None
	next = None
	hash = None
	pow = 0
	previous_hash = 0x0
	time = time.time()

	def __init__(self,data):
		self.data = data

	def block_data(self):
		block = {
			"index": str(self.blockNo),
			"data": str(self.data),
			"pow": str(self.pow),
			"time": str(time.strftime("%D %H:%M", time.localtime(int(self.time)))),
			"previous_hash": str(self.previous_hash),
		}
		return json.dumps(block, sort_keys=True, indent=4)

	def hash(self):
		h = self.block_data().encode()
		return hashlib.sha256(h).hexdigest()

	def __str__(self):
		return("Block Hash: " + str(self.hash())+ 
			"\nindex: " + str(self.blockNo) + 
			"\nBlock Data: " + str(self.block_data()) + 
			"\nPoW: " + str(self.pow) + 
			"\nPrevious Hash: " + str(self.previous_hash) + 
			"\n--------------")


class Blockchain:

	diff = 20
	maxpow = 2**32
	target = 2 ** (256-diff)

	block = Block("Ziad")
	dummy = head = block

	def add(self,block):
		block.previous_hash = self.block.hash()
		block.blockNo = self.block.blockNo + 1

		self.block.next = block
		self.block = self.block.next

	def mine(self,block):
		for n in range(self.maxpow):
			if int(block.hash(), 16) <= self.target:
				self.add(block)
				print(block)
				break
			else:
				block.pow += 1


blockchain = Blockchain()

for n in range(10):
	blockchain.mine(Block("Block "+str(n+1)))

while blockchain.head != None:
	print(blockchain.head)
	blockchain.head = blockchain.head.next
