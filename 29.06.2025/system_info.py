import platform

print(f"OS: {platform.system()} {platform.release()}")
print(f"Processor: {platform.processor()}")
print(f"Architecture: {platform.architecture()[0]}")