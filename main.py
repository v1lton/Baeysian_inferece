import pandas as pd

df = pd.read_table('SMSSpamCollection', sep='\t', header=None, names=["label", "sms_message"])
print(df.head(5))

df['label'].replace('ham', 0, inplace=True)
df['label'].replace('spam', 1, inplace=True)
print(df.shape)