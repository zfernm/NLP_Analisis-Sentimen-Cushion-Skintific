
import streamlit as st
import pandas as pd
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('indonesian'))

st.title("Analisis Sentimen Produk Cushion Skintific")

# Load Data
df = pd.read_csv("cleaned_cushion_skintific.csv")

# Labeling Sentimen berdasarkan Rating
def label_sentiment(rating):
    if "5" in rating or "4" in rating:
        return "Positif"
    elif "3" in rating:
        return "Netral"
    else:
        return "Negatif"

df['Sentimen'] = df['rating'].apply(label_sentiment)

# Preprocessing
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

df['Review Bersih'] = df['ulasan'].apply(clean_text)

# Tampilkan Tabel Review
st.subheader("1. Tabel Data Review (Setelah Preprocessing)")
st.write(df[['ulasan', 'Review Bersih', 'Sentimen']].rename(columns={'ulasan': 'Review Asli'}).reset_index(drop=True))

# Distribusi Sentimen
st.subheader("2. Distribusi Sentimen")
sentiment_counts = df['Sentimen'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Wordcloud
st.subheader("3. Wordcloud Review Positif & Negatif")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Review Positif**")
    positif_text = " ".join(df[df['Sentimen'] == 'Positif']['Review Bersih'])
    wordcloud_pos = WordCloud(width=400, height=300, background_color='white').generate(positif_text)
    st.image(wordcloud_pos.to_array())

with col2:
    st.markdown("**Review Negatif**")
    negatif_text = " ".join(df[df['Sentimen'] == 'Negatif']['Review Bersih'])
    wordcloud_neg = WordCloud(width=400, height=300, background_color='white').generate(negatif_text)
    st.image(wordcloud_neg.to_array())

# Machine Learning
st.subheader("4. Akurasi Model Machine Learning")

X = df['Review Bersih']
y = df['Sentimen']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()

st.write("**Akurasi:**", round(report['accuracy'] * 100, 2), "%")
st.dataframe(report_df[['precision', 'recall', 'f1-score']].dropna())

# Insight
st.subheader("5. Kesimpulan dan Insight")
st.markdown("""
- Mayoritas review terhadap Skintific Cushion bersifat **positif**.
- **Kekurangan** yang sering disebutkan berkaitan dengan hasil yang cakey atau tidak cocok untuk kulit tertentu.
- **Saran**: Skintific dapat meningkatkan formulasi agar lebih cocok untuk kulit kombinasi atau berminyak.
""")
