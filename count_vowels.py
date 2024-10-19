# count_vowels.py
def count_vowels(s):
    vowels = "aeiou"
    count = {v: 0 for v in vowels}
    
    for char in s.lower():  # Normalize to lowercase for easier counting
        if char in count:
            count[char] += 1
            
    total_vowels = sum(count.values())
    return total_vowels, count

if __name__ == "__main__":
    while True:
        string = input("Enter a string (or type 'exit' to quit): ")
        if string.lower() == 'exit':
            print("Goodbye!")
            break
            
        total, count = count_vowels(string)
        
        print(f"Total number of vowels in '{string}': {total}")
        print("Count for each vowel:")
        for vowel, cnt in count.items():
            if cnt > 0:
                print(f"  {vowel}: {cnt}")
