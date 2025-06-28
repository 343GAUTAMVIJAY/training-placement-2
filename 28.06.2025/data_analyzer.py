# Analyzes a list of numbers and returns basic statistics
def analyze_data(numbers):
    return {
        "count": len(numbers),
        "mean": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

if __name__ == "__main__":
    data = [1, 5, 3, 8, 2, 9, 4]
    stats = analyze_data(data)
    print("Data Analysis:", stats)