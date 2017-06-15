"""
Probabilistic Data Structures

See: 
    https://www.jasondavies.com/bloomfilter/
    http://billmill.org/bloomfilter-tutorial/
"""

import numpy as np
import uuid
import base64
from hashlib import sha1


class BloomFilter:

    def __init__(self, nbytes=100, nhashes=3, algo=sha1):
        self.algo = algo
        self.nbytes = nbytes
        self.array = bytearray(nbytes)
        self.update_hash_num(nhashes)
        self.count = 0

    @property
    def optimal_hash_num(self):
        return (self.nbytes / self.count) * np.log(2)

    @property
    def fpr(self):
        m = self.nbytes
        k = self.nhashes
        n = self.count
        return (1 - ((1 - (1 / m)) ** (k * n))) ** k

    def update_hash_num(self, num):
        # Approximate multiple hashing algorithms by salting
        # https://en.wikipedia.org/wiki/Salt_(cryptography)
        self.nhashes = num
        self.salts = []
        for i in range(num):
            salt = base64.urlsafe_b64encode(uuid.uuid4().bytes)
            self.salts.append(salt)

    def _hash(self, string):
        algo = self.algo()  # TODO don't repeat? how does `update` work?
        algo.update(string)
        return int(algo.hexdigest(), 16) % self.nbytes

    def add(self, string):
        enc_string = string.encode('utf-8')
        for i in range(self.nhashes):
            salt = self.salts[i]
            salted = enc_string + salt
            index = self._hash(salted)
            self.array[index] = 1
        self.count += 1

    def test(self, string):
        # Always `True` if string has already been added.
        # Either `True`/`False` if string has not.
        enc_string = string.encode('utf-8')
        in_array = []
        for i in range(self.nhashes):
            salt = self.salts[i]
            salted = enc_string + salt
            index = self._hash(salted)
            found = bool(self.array[index])
            in_array.append(found)
        return all(in_array)
