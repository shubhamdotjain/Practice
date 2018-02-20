
import pandas as pd
import re
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn_pandas import DataFrameMapper
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

lmtzr = WordNetLemmatizer()

train_data = pd.read_csv("train.csv")

test_data = pd.read_csv("test.csv")

def text_process(mess):
    mess = re.sub("[^a-zA-Z]", " ", str(mess).lower())
    list_cell_content = str(mess).split()
    cell_content = [lmtzr.lemmatize(word) for word in list_cell_content]
    cell_content = " ".join(cell_content)
    return cell_content

def data_preprocess(data):
    data = data.fillna("")
    data['title_words'] = data['name'].apply(lambda x : len(str(x).split(" ")))
    data['des_words'] = data['desc'].apply(lambda x : len(str(x).split(" ")))
    data['duration_c'] = data['deadline'] - data['created_at']
    data['duration_l'] = data['deadline'] - data['launched_at']
    data['duration'] = data['launched_at'] - data['created_at']
    data['dead_state'] = data['deadline'] - data['state_changed_at']
    data['desc'] = data.desc.apply(lambda x: text_process(x))
    data['keywords'] = data.keywords.apply(lambda x: text_process(x))
    data['name'] = data.name.apply(lambda x: text_process(x))
    data['text'] = data['desc'] + data['keywords'] + data['name']
    return data


train_data = data_preprocess(train_data)

test_data = data_preprocess(test_data)


result = train_data['final_status']
# data = data[['name','desc','goal','duration','title_words','des_words']]


# X_train, X_test, y_train, y_test = train_test_split(
    # train_data,result, test_size=0.55, random_state=42)

mapper = DataFrameMapper([
     ('text', TfidfVectorizer(stop_words='english',max_df=0.9,min_df=50)),
     ('goal',None),
     ('duration_c',None),
    ('dead_state',None),
    ('disable_communication',LabelEncoder()),
    ('duration',None),
    ('duration_l',None),
    ('currency',CountVectorizer()),
     ('country',CountVectorizer()),
     ])

feature = mapper.fit_transform(X_train)
test = mapper.transform(X_test)
final_test = mapper.transform(test_data)

from sklearn.ensemble import RandomForestClassifier,BaggingClassifier
model = RandomForestClassifier(
 n_estimators = 250)

print (feature.shape)


model.fit(feature,y_train
         )

# from sklearn.metrics import accuracy_score
# accuracy = accuracy_score(y_test,model.predict(test))
# print (accuracy)

ans = model.predict(final_test)

test_df = test_data

test_df['final_status'] = pd.DataFrame(ans)

df = test_df[['project_id','final_status']]

# df[df.project_id == "kkst1000002330"]

df.to_csv("submission.csv",index=False)
