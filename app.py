import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

texts = ["I love data science, I love data", "Data science is future"]

vectorizer = CountVectorizer(tokenizer=str.split)
X = vectorizer.fit_transform(texts)

st.write("Vocabulary:", vectorizer.get_feature_names_out())
st.write("BoW Matrix:\n", X.toarray())
