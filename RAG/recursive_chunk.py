# from langchain_text_splitters import RecursiveCharacterTextSplitter

# text = """Attention lets the model focus on relevant tokens.

# Transformers use self-attention to process all tokens in parallel. This makes training much faster than RNNs, which process tokens one by one.

# BERT  is a pretrained model built from the Transformer encoder."""

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=20,
#     separators= ["\n\n\n", "\n", ". ", " ", ""],
#     keep_separator= "end"
#     )

# chunks = splitter.split_text(text)

# for i, chunk in enumerate(chunks):
#     print(f"--- Chunk {i} ({len(chunk)} chars) ---")
#     print(chunk)


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("RAG/1706.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=30,
    separators=["\n\n", "\n", ". ", " ", ""],
    keep_separator="end",
)

chunks = splitter.split_documents(docs)

print(f"Document length: {len(docs)}")
print("chunk:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print(f"{i}: {chunk.page_content}")
    print(chunk.metadata)
