#!/usr/bin/env python
# coding: utf-8

# In[15]:


from pprint import pprint

# This function finds hamming distance between two string, which is the number of indexes i such that str1[i] != str2[i]
def hamming_dist(str1, str2):
    i = 0
    count = 0

    while i < len(str1):
        if str1[i] != str2[i]:
            count += 1
        i += 1
    return count

# We add a number to the list only if its hamming distance from all the other numbers in the list is greater than 2
ls = ['0000']
for i in range(1, 9999 + 1):
    i_fits = 1
    i_padded = str(i).zfill(4)
    for item in ls:
        if hamming_dist(i_padded, item) < 2:
            i_fits = 0
    if i_fits:
        ls.append(i_padded)
pprint(f'List of available codes: {ls}')
print(f'Number of codes: {len(ls)}')

# Check whether the minimal Hamming distance between two different numbers in our list is indeed 3
hd = []
for i in ls:
    for j in ls:
        if i != j:
            hd.append(hamming_dist(i, j))
print(f'Minimal Hamming distance: {min(hd)}')


# In[ ]:




