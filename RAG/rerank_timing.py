import time
from hybrid_search import hybrid_search
from rerank_fn import rerank

question = "What is multi-head attention?"

# warm-up: প্রথম call সবসময় ধীর (model গরম হয়), তাই মাপার আগে একবার চালিয়ে নাও
rerank(question, hybrid_search(question, final_k=5), top_n=3)

for candidates in [5, 10, 20, 40]:
    docs = hybrid_search(question, final_k=candidates)

    start = time.perf_counter()
    rerank(question, docs, top_n=3)
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(
        f"asked={candidates:3d} | got={len(docs):3d} | rerank time={elapsed_ms:7.1f} ms"
    )
