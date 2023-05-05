#Wordcount.py
#+++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
worddict = {}
def print_top(filename):
  print('none')

def word_count(filename):
  f = open(f'{filename}.txt', 'rt')
  for line in f:
    for word in line.split():
      if word.lower() in worddict:
        worddict[word.lower()] = worddict[word.lower()] + 1
      else:
        worddict[word.lower()] = 1
  return worddict
#maybe append a copy of each key in the dictionary with same value number and then delete old one?
def print_words(filename):
  word_count(filename)
  sortdict = sorted(worddict)
  for key in sortdict:
    print(key + ' : ' + str(worddict[key]))
    
  
def remove_punct(filename): #needs some work
  import string
  string.punctuation


#-----------------------------------------------------------------------------
#list2.py
def remove_adjacent(nums):
  removed = []
  for num in nums:
    if len(removed) == 0 or num != removed[-1]:
      removed.append(num)
  print(removed)

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  full = list1 + list2
  sfull = sorted(full)
  print(sfull)

def linear_merge3(list1, list2):
  result = []
  while len(list1) and len(list2):
    if list1[0] < list2[0]:
      result.append(list1.pop(0))
    else:
      result.append(list2.pop(0))
  result.extend(list1)
  result.extend(list2)
  
#list1.py
def sort_last(tuples):
  tuples.sort(key = lambda x: x[len(x)-1])
  print(tuples)

def front_x(words):
  xfirst = []
  others = []
  for w in words:
    if w[0] == 'x': #can use w.startswith('x')
      xfirst.append(w)
      xfirst.sort()
    else:
      others.append(w)
  others.sort()
  for w in others:
    xfirst.append(w)
  print(xfirst)

def match_ends(words):
  ends = 0
  for w in words:
    if len(w) >= 2:
      if w[0] == w[len(w)-1]:
        ends = ends + 1
  print(ends)

#string2.py
def verbing(s):
    if len(s) < 3:
        print(s)
    elif s[-3:] == 'ing':
        print(s+'ly')
    else:
        print(s+'ing')

def not_bad(s):
    n = s.find('not')
    bad = s.find('bad')
    if -1 < n < bad:
        s = s[:n] + 'good' + s[bad+3:]
        print(s)

def front_back(a, b):
    la = len(a)
    lb = len(b)
    if la % 2 == 0:
        hla = la//2
    else:
        hla = la//2 + 1
    if lb % 2 == 0:
        hlb = lb//2
    else:
        hlb = lb//2 + 1
    fa = a[:hla]
    ba = a[hla:]
    fb = b[:hlb]
    bb = b[hlb:]
    print(fa + fb + ba + bb)
    
#string1.py
def donuts(count):
    if count > 10:
        print("Number of donuts: many")
    else:
        print(f"Number of donuts: {count}")
        
def both_ends(s):
    if len(s) < 2:
        print('')
    else:
        print(s[0:2] + s[-2:])

def fix_start(s):
    char = s[0]
    new = s[1:].replace(char, "*")
    print(char + new)

def mix_up(a, b):
    print(a+' '+b)
    f2a = a[0:2]
    f2b = b[0:2]
    print(f2b + a[2:] + ' ' + f2a + b[2:])
