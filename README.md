Dataset :- https://drive.google.com/drive/folders/1uduUdFVKN-dstLMf9NcrSQasd67Mkqg5?usp=sharing
🧠 Question Similarity Checker

A lightweight and interactive web app to compare the **semantic similarity between two questions** using Sentence-BERT (SBERT). It highlights how deep learning models can understand meaning beyond exact words — ideal for paraphrase detection, duplicate question checking, and content deduplication.

🚀 Demo

Paste any two questions (like from Quora or Stack Overflow), and get a similarity score that tells you how close they are in meaning!

🔧 Features

- 🔍 Compares two questions using semantic meaning, not just keyword matching.
- ⚡ Powered by Sentence-BERT embeddings.
- 🖥️ Clean and responsive UI using Streamlit.
- 📊 Displays cosine similarity score between the input questions.


🛠️ Tech Stack

| Component        | Details                                  |
|------------------|-------------------------------------------|
| Frontend         | Streamlit                                |
| Backend          | Python                                    |
| NLP Model        | Sentence-BERT (paraphrase-MiniLM-L6-v2)   |
| Libraries Used   | sentence-transformers, torch, streamlit   |


📦 Installation

1. Clone the repo:
   git clone https://github.com/your-username/question-similarity-app.git  
   cd question-similarity-pair

2. Create a virtual environment:
   python -m venv venv

3. Activate the environment:  
   - On Windows:  
     venv\Scripts\activate  
   - On Mac/Linux:  
     source venv/bin/activate

4. Install dependencies:  
   pip install -r requirements.txt  
   *(If you don’t have a requirements.txt yet, generate it with `pip freeze > requirements.txt`)*


▶️ Run the App

   streamlit run app.py

Then open the link shown in your terminal (usually http://localhost:8501/)


🧪 Example

| Input Question 1                 | Input Question 2                              | Similarity Score |
|----------------------------------|-----------------------------------------------|------------------|
| How can I learn Python?          | What’s the best way to learn Python online?   | 0.89             |
| What is the capital of India?    | How to cook pasta at home?                    | 0.07             |



📁 Folder Structure

question-similarity-app/  
├── app.py                  # Streamlit app  
├── requirements.txt        # Python dependencies  
├── README.md               # You’re here!  
└── venv/                   # Virtual environment (not uploaded to GitHub)  



💡 Use Cases

- ❓ Detect duplicate or paraphrased questions in forums
- 📚 Academic question similarity checks
- ✍️ Content rewriting & plagiarism assistance
- 🧠 NLP demos for resume/portfolio projects


 📌 TODO (Future Improvements)

- Add support for batch comparisons or CSV upload
- Add visualization (e.g., embedding projections with PCA)
- Deploy via Streamlit Cloud or Hugging Face Spaces


🤝 Contributing

Pull requests and feedback are welcome!  
If you find a bug or want a feature, feel free to open an issue.

📄 License

MIT License.  
Feel free to use or modify this for your own use cases.

 🧑‍💻 Author

Mahi Singh  
LinkedIn: (https://www.linkedin.com/in/mahi28singh/)  
Passionate about transforming raw data into real-world solutions using ML and NLP.
