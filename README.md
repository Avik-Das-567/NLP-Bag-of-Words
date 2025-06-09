# Bag of Words (BoW) in NLP
### App Link
- https://nlp-bag-of-words.streamlit.app/
---
### What is Bag of Words (BoW)?
- BoW is a technique that converts text into **numbers** by counting how many times each word appears.
- It doesn't consider **grammar** or **word order** – only frequency.
- Used in NLP tasks like **text classification**, **spam detection**, **sentiment analysis**, etc.
---
### Example Texts
- Text 1: **`"I love data science, I love data"`**
- Text 2: **`"Data science is future"`**
---
### Vocabulary Created
- All unique words across both sentences : **`['data', 'future', 'i', 'is', 'love', 'science']`**
---
### Bag of Words Matrix
| Sentence                         | data | future | i | is | love | science |
| -------------------------------- | ---- | ------ | - | -- | ---- | ------- |
| I love data science, I love data | 2    | 0      | 2 | 0  | 2    | 1       |
| Data science is future           | 1    | 1      | 0 | 1  | 0    | 1       |
- Each row shows how many times each word appears in the respective sentence.
---
### Required Python Packages
- **`scikit-learn`**
- **`streamlit`**
---
### How the App Works -
- **Input :**
```
texts = ["I love data science, I love data", "Data science is future"]
```
- **Output :**
```
Vocabulary: ['data' 'future' 'i' 'is' 'love' 'science']
BoW Matrix:
[[2 0 2 0 2 1]
 [1 1 0 1 0 1]]
```
- Now we can feed this matrix into machine learning models.
---
### Additional Insights :
- BoW is simple but effective for many tasks.
- It creates sparse vectors when vocabulary is large.
- BoW works best with **cleaned and preprocessed** text.
---
