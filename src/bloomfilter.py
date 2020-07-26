
# Python 3 program to build Bloom Filter 
# Install mmh3 and bitarray 3rd party module first 
# pip install mmh3 
# pip install bitarray 
import math 
import mmh3 
from bitarray import bitarray 
  
class BloomFilter(object): 
  
    ''' 
    Class for Bloom filter, using murmur3 hash function 
    '''
  
    def __init__(self, size,items_count): 
        ''' 
        items_count : int 
            Number of items expected to be stored in bloom filter 
        fp_prob : float 
            False Positive probability in decimal 
        '''
        # False posible probability in decimal 
        #self.fp_prob = fp_prob 
  
        # Size of bit array to use 
        #self.size = self.get_size(size,items_count) 
  
        self.size = size

        # number of hash functions to use 
        #self.hash_count = self.get_hash_count(self.size,items_count) 
  
        self.hash_count = items_count

        # Bit array of given size 
        self.bit_array = bitarray(self.size) 
  
        # initialize all bits as 0 
        self.bit_array.setall(0) 

        # currrent element count
        self.element_count = 0

        # maximum items in the filter (from input)
        self.max_num_of_items = items_count
        
        self.values = list()

    def get_marked_bits_count(self):
        return self.bit_array.count("1")

    def get_bit_array(self):
        return self.bit_array

    def add(self, item): 
        ''' 
        Add an item in the filter 
        '''
        digests = [] 
        for i in range(self.hash_count): 
  
            # create digest for given item. 
            # i work as seed to mmh3.hash() function 
            # With different seed, digest created is different 
            digest = mmh3.hash(item,i) % self.size 
            digests.append(digest) 
  
            # set the bit True in bit_array 
            self.bit_array[digest] = True
        # increment element coount
        self.element_count += 1

        (self.values).append(item)
  
    def check_values(self, item): 
        ''' 
        Check for existence of an item in filter 
        '''
        '''for i in range(self.hash_count): 
            digest = mmh3.hash(item,i) % self.size 
            if self.bit_array[digest] == False: 
  
                # if any of bit is False then,its not present 
                # in filter 
                # else there is probability that it exist 
                return False
        '''
        if item in self.values:
            return True
        return False

    def check(self,item):
        for i in range(self.hash_count): 
            digest = mmh3.hash(item,i) % self.size 
            if self.bit_array[digest] == False: 
  
                # if any of bit is False then,its not present 
                # in filter 
                # else there is probability that it exist 
                return False
        return True


    def get_element_count(self):
        '''
        Return element counter
        '''
        return self.element_count

    def is_add_allowed(self):
        '''
        Check if insertion is allowed
        '''
        #m = -(self.max_num_of_items * math.log(self.fp_prob))/(math.log(2)**2) 
        if(self.element_count < self.max_num_of_items):
            return True
        else:
            return False

    def set_max_num_of_items(self, m):
        self.max_num_of_items = m
    
    @classmethod
    def get_size(self,n,p): 
        ''' 
        Return the size of bit array(m) to used using 
        following formula 
        m = -(n * lg(p)) / (lg(2)^2) 
        n : int 
            number of items expected to be stored in filter 
        p : float 
            False Positive probability in decimal 
        '''
        m = (abs(-(n * math.log(p))/(math.log(2)**2))) 
        return int(m) 
  
    @classmethod
    def get_hash_count(self, m, n): 
        ''' 
        Return the hash function(k) to be used using 
        following formula 
        k = (m/n) * lg(2) 
  
        m : int 
            size of bit array 
        n : int 
            number of items expected to be stored in filter 
        '''
        k = (m/n) * math.log(2) 
        return int(k) 
