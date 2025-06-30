import time

input("Press Enter to start...")
start = time.time()
input("Press Enter to stop...")
elapsed = time.time() - start
print(f"Elapsed time: {elapsed:.2f} seconds")