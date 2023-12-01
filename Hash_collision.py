def get_index(data_list,input_string):
    hash_val=0
    for i in input_string:
        hash_val+= ord(i)
    #print (hash_val%len(data_list))
    return hash_val%len(data_list)

def get_valid_index(data_list,input_string):
        idx=get_index(data_list,input_string)
        while True:
            if data_list[idx] is None:
                return idx
            if data_list[idx][0]==input_string:
                return idx
            idx+=1
            if idx>len(data_list)-1:
                idx=0

class Hash:
    def __init__(self,len_list_you_want):
        self.data_list=[None]*len_list_you_want
    def insert(self,key,value):
        self.data_list[get_valid_index(self.data_list,key)]=(key,value)
    def update(self,key,value):
        self.data_list[get_valid_index(self.data_list,key)]=key,value
hash_1=Hash(20)
hash_1.insert('listen',23)
hash_1.insert('silent',42)
hash_1.update('listen',42)
print(hash_1.data_list[15]) #15 is a hash value of get_index
print(hash_1.data_list.index(('silent',42 )))
