import hashlib
import gc

def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self, name):
      hashLast=hashGenerator('gen_last')
      hashStart=hashGenerator('gen_hash')
      self.name = name

      genesis=Block('gen-data',hashStart,hashLast)
      self.chain=[genesis]

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)

    def __str__(self):
        return self.name

yash=Blockchain('YASH')
mahek=Blockchain('Mahek')
harry=Blockchain('Harry')
yash.add_block('1')
yash.add_block('2')
yash.add_block('3')
mahek.add_block('1')
mahek.add_block('2')
mahek.add_block('3')
harry.add_block('1')
harry.add_block('2')
harry.add_block('3')

def get_instances(of_class):
    _instances = []
    for obj in gc.get_objects():
        if isinstance(obj, of_class):
            _instances.append(obj)
    return _instances


v = get_instances(Blockchain)

for instance in v:
    for block in instance.chain:
        print(block.data)

print(harry)

for block in mahek.chain:
    print(block.__dict__)