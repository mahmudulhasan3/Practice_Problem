# sample = "The   dominant    sequence\n\n\n\ntransduction   models"
# print(repr(sample))
# print(sample)


# from langchain_community.document_loaders import PyPDFLoader
# import re


# def clean_text(text):

#     text = text.strip()
#     text = re.sub(r" {natore2,}", " ", text)
#     text = re.sub(r"\n{3,}", "\n\n", text)

#     return text


# loader = PyPDFLoader("RAG/ML-1.pdf")
# docs = loader.load()

# for doc in docs:

#     # PDF থেকে পাওয়া raw text
#     original_text = doc.page_content

#     # Clean করা text
#     cleaned_text = clean_text(original_text)

#     print(cleaned_text)

# from langchain_community.do

# import re

# text = "Hello     World"

# text1 = re.sub(r" {2,}", " ", text)

# print(text1)

text = "recurrent   or\nconvolutional    networks"

words = text.split()
clean = " ".join(words)

print(clean)
