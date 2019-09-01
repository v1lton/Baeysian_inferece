import pandas as pd
import re

df = pd.read_table('SMSSpamCollection', sep='\t', header=None, names=["label", "sms_message"])
print(df.head(5))

df['label'].replace('ham', 0, inplace=True)
df['label'].replace('spam', 1, inplace=True)
print(df.shape)

documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']
lower_case_documents = []
i = 0
for x in documents:
    lower_case_documents.append(x.lower())
print(lower_case_documents)

sans_punctuation_documents = []
for i in lower_case_documents:
    sans_punctuation_documents.append(re.sub(r'[^\w\s]','',i))
print(sans_punctuation_documents)

preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split())
print(preprocessed_documents)

frequency_list = []
import pprint
from collections import Counter
for i in preprocessed_documents:
    frequency_list.append(Counter(i))
pprint.pprint(frequency_list)
