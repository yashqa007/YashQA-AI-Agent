def save_to_file(content, filename="output/test_cases.txt"):
    with open(filename, "w") as f:
        f.write(content)

    print(f"✅ Saved to {filename}")