import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

texts = ["i love data science, i love data", "Data science is future"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

st.write("Vocabulary:", vectorizer.get_feature_names_out())
st.write("BoW Matrix:\n", X.toarray())
