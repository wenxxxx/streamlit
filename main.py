import pickle
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup as bs
from sklearn.preprocessing import MultiLabelBinarizer
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
import tensorflow_hub as hub

# Define the Streamlit app
st.title('Stack Overflow Question Tagger')

# Load the Universal Sentence Encoder
use = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

y = [['android', 'c', 'c#', 'c++', 'css', 'html', 'ios', 'java', 'javascript', 'jquery', 'net', 'php', 'python', 'r']]
mlb = MultiLabelBinarizer()
y_ = mlb.fit_transform(y)

texte = st.text_area('Enter some text here')

if st.button('Predict the text'):
    soup = bs(texte, 'html.parser')
    stop_words = set(stopwords.words('english'))
    tokens = simple_preprocess(texte)
    tokens = [token for token in tokens if token not in stop_words]
    X = [" ".join(tokens)]
    X_emb = use(X)
    # importer le modele
    model = pickle.load(open('../pythonProject3/svc.pkl', 'rb'))
    prediction = model.predict(X_emb)
    tags = mlb.inverse_transform(prediction)
    df_pred = pd.DataFrame(tags)
    st.write(df_pred)

# Afficher le widget de téléchargement de fichier
fichier = st.file_uploader("Télécharger un fichier")

if st.button('Predict the file'):
    st.write()
