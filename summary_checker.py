import os

def count_test_functions(file_path):
    count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("def test_"):
                count += 1
    return count

def scan_tests_directory():
    test_dir = "tests"
    total_tests = 0
    print("📦 Test Function Summary:\n")
    for filename in os.listdir(test_dir):
        if filename.startswith("test_") and filename.endswith(".py"):
            path = os.path.join(test_dir, filename)
            count = count_test_functions(path)
            total_tests += count
            print(f"{filename}: {count} test(s)")
    print(f"\n✅ Total collected tests: {total_tests}")

if __name__ == "__main__":
    scan_tests_directory()