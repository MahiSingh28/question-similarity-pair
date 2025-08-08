import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

# Load Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

st.title("Quora Question Similarity Checker 🔍")
st.markdown("Check if two questions are duplicates using NLP techniques.")

# Input questions
q1 = st.text_area("Enter Question 1")
q2 = st.text_area("Enter Question 2")

def exact_match(q1, q2):
    return 1 if q1.strip().lower() == q2.strip().lower() else 0

def tfidf_similarity(q1, q2):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([q1, q2])
    sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return sim[0][0]

def bert_similarity(q1, q2):
    embeddings = model.encode([q1, q2], convert_to_tensor=True)
    sim_score = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    return sim_score.item()

# On button click
if st.button("Compare Questions"):
    if q1 and q2:
        exact = exact_match(q1, q2)
        tfidf_score = tfidf_similarity(q1, q2)
        sbert_score = bert_similarity(q1, q2)

        st.write("**Exact Match:**", "✅ Yes" if exact else "❌ No")
        st.write("**TF-IDF Similarity:**", round(tfidf_score, 3))
        st.write("**Sentence BERT Similarity:**", round(sbert_score, 3))

        # Final Prediction
        if sbert_score > 0.5:
            st.success("Prediction: Similar Questions ✅")
        else:
            st.warning("Prediction: Not Similar ❌")
    else:
        st.warning("Please enter both questions!")



# Dataset-based matching
st.markdown("---")
st.subheader("📁 Upload Dataset to Find Similar Questions")

uploaded_file = st.file_uploader("Upload a CSV with a 'question' or 'question1' column", type=["csv"])

top_n = st.slider("Number of top similar questions to show", 1, 10, 5)

if uploaded_file:
    data = pd.read_csv(uploaded_file)


    # Check which column is available
    question_col = None
    for col in ['question', 'question1', 'q1', 'Question1']:
        if col in data.columns:
            question_col = col
            break

    if not question_col:
        st.error("No valid question column found! Please rename one column to 'question' or 'q1'")
    elif not q1:
        st.warning("Enter a question above to find similar ones.")
    else:
        with st.spinner("Finding similar questions..."):
            input_embedding = model.encode(q1, convert_to_tensor=True)
            dataset_embeddings = model.encode(data[question_col].astype(str).tolist(), convert_to_tensor=True)
            similarities = util.pytorch_cos_sim(input_embedding, dataset_embeddings)[0]
            top_indices = similarities.topk(top_n).indices

            st.markdown(f"### 🔝 Top {top_n} similar questions:")
            for idx in top_indices:
                st.markdown(f"- {data[question_col].iloc[idx]} (Score: {round(similarities[idx].item(), 3)})")
                