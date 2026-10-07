# rag-practice/citation_map.py
import re

# Retrieve হওয়া chunk-গুলো (metadata সহ)
chunks = [
    {
        "text": "We employ 8 parallel attention layers...",
        "source": "paper1.pdf",
        "page": 5,
    },
    {
        "text": "Retrieval-augmented generation combines...",
        "source": "paper2.pdf",
        "page": 12,
    },
    {
        "text": "Multi-head attention allows the model to jointly attend...",
        "source": "paper1.pdf",
        "page": 9,
    },
]

# Step 1: নম্বর -> metadata map বানানো
citation_map = {}
for i, chunk in enumerate(chunks, start=1):
    citation_map[i] = {"source": chunk["source"], "page": chunk["page"]}

# LLM-এর answer (এখন হাতে লেখা, আসলে LLM দেবে)
answer = "8টা head ব্যবহার করা হয়েছে [1]। Head-গুলো আলাদা subspace-এ attend করে [3]। এটা খুব দ্রুত [7]।"

# Step 2: answer থেকে নম্বরগুলো বের করা
used = re.findall(r"\[(\d+)\]", answer)  # ['1', '3', '7'] (string হিসেবে)
used = [int(n) for n in used]  # [1, 3, 7] (number হিসেবে)

# Step 3: সত্যিকারের নম্বর আর fake নম্বর আলাদা করা
valid = [n for n in used if n in citation_map]
invalid = [n for n in used if n not in citation_map]

# Step 4: user-কে দেখানো
print(answer)
print("\nSources:")
for n in sorted(set(valid)):
    meta = citation_map[n]
    print(f"[{n}] {meta['source']}, page {meta['page']}")

print("\nসন্দেহজনক citation:", invalid)
