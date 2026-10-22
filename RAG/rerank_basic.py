from sentence_transformers import CrossEncoder

# 1) Reranker model load (প্রথমবার চালালে download হবে)
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

# 2) একটা question
question = "What is multi-head attention?"

# 3) চারটা chunk: প্রতিটার ধরন আলাদা
chunks = [
    # A: সরাসরি উত্তর আছে
    "Multi-head attention runs several attention functions in parallel, "
    "letting the model attend to information from different positions.",
    # B: topic একই (attention), কিন্তু এই প্রশ্নের উত্তর না
    "The Transformer was trained on the WMT 2014 English-German dataset "
    "using attention-based layers.",
    # C: প্রশ্নের শব্দ আছে (multi, head), কিন্তু মানে আলাদা
    "The committee head met with multi-department staff to review the budget.",
    # D: সম্পূর্ণ অপ্রাসঙ্গিক
    "Rice is the main crop in Bangladesh and grows best in monsoon season.",
]

# 4) (question, chunk) জোড়া বানাও
pairs = [(question, chunk) for chunk in chunks]

# 5) প্রতিটা জোড়ার score
scores = reranker.predict(pairs)

# 6) দেখো
for chunk, score in zip(chunks, scores):
    print(f"{score:8.3f} | {chunk[:60]}")
