import time

# stopwatch start
start = time.perf_counter()

time.sleep(1.5)

# stopwatch stop
end = time.perf_counter()

# সেকেন্ডকে millisecond-এ বদলাও (× 1000)
elapsed_ms = (end - start) * 1000

print(f"elapsed: {elapsed_ms:.1f} ms")
