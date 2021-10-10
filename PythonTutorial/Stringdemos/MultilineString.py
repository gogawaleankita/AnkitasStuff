zenPython = ''' 
The Zen of Python, by Tim Peters 

Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea.
'''

words = zenPython.split(" ");
print(len(words))
words = [i.strip(' -*!.,') for i in words]

words.pop(0)
print(words[3])
words = [i.lower() for i in words]
print(words[3])
words = [i.strip('\n') for i in words]
unique_words = set(words)
print(len(unique_words))

word_frequency={ i:words.count(i)  for i in (unique_words) };

print(word_frequency['the'])

frequent_words={};


# frequent_word = {};

for (key, value) in word_frequency.items():
    if value > 5:
        frequent_words[key] = value

print(frequent_words)
