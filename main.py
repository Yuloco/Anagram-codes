# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    # [assignment] Add your code here
  word = input ("Enter word:")
  anagram = input ("Enter anagram:")
  word_sort = sorted(word)
  anagram_sort = sorted(anagram)
  if len(word) == len(anagram): 
    if word_sort == anagram_sort:
      print (word + "," + " " + anagram, True)
    else:
     print (word + "," + " " + anagram, False)
  else:
    print ("incomplete")
final = find_anagram("", "")

check = input ("Enter YES to continue NO to Stop:")
while check == "yes":
 find_anagram("", "")

