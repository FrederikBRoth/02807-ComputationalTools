# Week 04
# ## Similar Items, Minhashing and Locality Sensitive Hashing
# Time for dank
# [Exercise Sheet](https://courses.compute.dtu.dk/02807/2023/exercises/week4/week4.pdf)
# This exercise is gonna use the same file all through the exercises so it will be done in one cell
# %%
import sys
import os
import mmh3
import numpy as np
from numpy.core.numeric import allclose

#################### Utilities ######################
# hashes a list of strings
def listhash(l, seed):
    val = 0
    for e in l:
        val = val ^ mmh3.hash(e, seed)
    return val


def clean_text(aString):
    # Removed newline
    output = aString.replace('\n', '')
    # Splits at spaces
    outputs = output.split()
    # Removes all non-alfanumeric symbols and joins the remaining symbols into one word
    outputs = [
        ''.join(char for char in world if char.isalnum()) for world in outputs
    ]
    # Removes all uppercase letters
    outputs = [s.lower() for s in outputs]
    # Garbage way to remove double spaces
    output = ' '.join(outputs)
    return ' '.join(output.split())


################### Similarity ######################
q = 2   # length of shingle
k = 1000   # number of minhashes
docs = {}   # dictionary mapping document id to document contents

# read data sets
srcfolder = os.path.dirname(os.path.abspath(__file__))
datafolder = os.path.join(
    srcfolder, 'ats_corpus_small'
)   # change to ats_corpus for large data set

for file in os.listdir(datafolder):
    filepath = os.path.join(datafolder, file)
    f = open(filepath, 'r')
    docs[file] = f.read()
    docs[file] = clean_text(docs[file])
    print('read document ' + file)
    f.close()


def shingle(aString, q, delimiter=' '):
    all_shingles = []
    if delimiter != '':
        words_list = aString.split(delimiter)
    else:
        words_list = aString
    for i in range(len(words_list) - q + 1):
        all_shingles.append(delimiter.join(words_list[i : i + q]))
    return list(set(all_shingles))


def minhash(shingles_list, seed):
    minhash_value = None
    for aShingle in shingles_list:
        hashcode = listhash([aShingle], seed)
        if minhash_value == None or hashcode < minhash_value:
            minhash_value = hashcode
    return minhash_value


def minhashes(shingles_list, k):
    all_minhash = []
    for i in range(k):
        all_minhash.append(minhash(shingles_list, i))
    return all_minhash


def better_minhash(shingle, k):
    all_minhash = []
    for i in range(k):
        all_minhash.append(listhash(shingle, i))
    return all_minhash


def better_sig(document):
    shingle_dict = {str(): list()}
    for i, e in document.items():
        shingle_dict[i] = shingle(e, q)
    all_shingles = sum(shingle_dict.values(), [])
    for s in all_shingles:
        minhash = better_minhash(s, k)
        for key, value in document.items():
            if s in value:
                for i in range(k):
                    shingle_dict[key][i] = min(
                        minhash[i], shingle_dict[key][i]
                    )
    return shingle_dict


print(better_sig(docs))


def signatures(document, q=q, k=k):
    signatures = {}
    for i, e in document.items():
        print('Processing: ' + i)
        shingles = shingle(e, q)
        minhash = minhashes(shingles, k)
        signatures[i] = minhash
    return signatures


def jaccard(doc1, doc2, docs):
    sig1 = np.array(docs[doc1])
    sig2 = np.array(docs[doc2])

    intersect = np.intersect1d(sig1, sig2)
    return len(intersect) / len(np.union1d(sig1, sig2))


def similar(signatures):
    sig_keys = list(signatures.keys())
    similar = {}
    for i in range(len(sig_keys) - 1):
        for j in range(i + 1, len(sig_keys)):
            if j != i:
                score = jaccard(sig_keys[i], sig_keys[j], signatures)
                print(score)
                if score > 0.6:
                    similar[(sig_keys[i], sig_keys[j])] = score

    return similar


test = 'This is a test'
better_sig(docs)

# shingles = shingle(test, 2)
# signature_dict = signatures(docs)

# doc1 = list(docs.keys())[0]
# doc2 = list(docs.keys())[1]
# print(f'Jaccard: ', jaccard(doc1, doc2, signature_dict))
# print(similar(signature_dict))
