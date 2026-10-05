from langchain_core.documents import Document

docs = [
    Document(
        page_content="BERT uses masked language modeling: random tokens are hidden and predicted.",
        metadata={"source": "bert.pdf", "page": 3},
    ),
    Document(
        page_content="BERT is pre-trained on BooksCorpus and English Wikipedia.",
        metadata={"source": "bert.pdf", "page": 4},
    ),
    Document(
        page_content="Decoder self-attention uses masking so a position cannot see future tokens.",
        metadata={"source": "attention.pdf", "page": 5},
    ),
    Document(
        page_content="Multi-head attention lets the model attend to different positions.",
        metadata={"source": "attention.pdf", "page": 4},
    ),
]


from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    collection_name="topk_filter_practice",
)
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 2,
        "filter": {"source": "bert.pdf"},
    }
)

results = retriever.invoke("How does masking work?")

for doc in results:
    print(doc.metadata["source"], "| page", doc.metadata["page"])
    print(doc.page_content)
    print("---")
retriever_no_filter = vectorstore.as_retriever(search_kwargs={"k": 2})

for doc in retriever_no_filter.invoke("How does masking work?"):
    print(doc.metadata["source"], "|", doc.page_content[:60])
