import pandas as pd
import re
from random import sample

def text_to_dataframe(source, destination):
    with open(source,encoding='latin') as f:
        data = f.read()
    data_list = data.split("\n\n")
    test_data = [x.split(": ") for x in data_list[0].split("\n")]
    columns = [x[0] for x in test_data]
    df = pd.DataFrame(columns=columns)
    i = 0
    for test in sample(data_list,50000):
        i = i + 1
        if i%1000 ==0:
            print(i)
        try:
            test_data = [x.split(": ") for x in test.split("\n")]
            cols = [x[0] for x in test_data]
            t_data = [x[1] for x in test_data]
            df = df.append(pd.DataFrame([t_data], columns=cols),ignore_index=True)
        except:
            pass
    print(df.shape, df.head())

    df['review/score'] = df['review/score'].apply(lambda x: float(x))
    df['set_words'] = df['review/summary'] + " " + df['review/text']

    df['set_words'] = df['set_words'].apply(lambda x: ",".join(re.sub('[^ 0-9a-zA-Z]+', '', str(x)).lower().split()))
    df[['product/productId', 'review/userId', 'review/profileName',
       'review/helpfulness', 'review/score', 'review/time', 'review/summary',
       'review/text','set_words']].to_csv(destination)
