import pickle
import streamlit as st
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from gensim.parsing.preprocessing import remove_stopwords
import tensorflow_hub as hub
import gensim

# Define the Streamlit app
st.title('Stack Overflow Question Tagger')

# Afficher le widget de téléchargement de fichier
fichier = st.file_uploader("Télécharger un fichier")

if fichier is None:
    st.write('Please select un file:')
