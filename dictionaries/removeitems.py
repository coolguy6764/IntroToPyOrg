python_words = {'list': '''A collection of vallues that are not connected, 
but have an order''',
                'dictionary': '''A collection of key-value pairs.''',
                'function': '''A named set of instructions that defines a set
of actions in Python.''',
                }


# Show the current set of words and meanings

for w, m in python_words.items():
    print('\nWord: %s' % w)
    print('Meaning: %s' % m)

# Remove the word 'list' and its meaning.
del python_words['list']

# Show current set of words and meanings

for w, m in python_words.items():
    print('\nWord: %s' % w)
    print('Meaning: %s' % m)

