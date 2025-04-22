def find_highest_frequency_word(file_path):
    """
    Counts the frequency of each word in a text file and returns the word with the highest frequency.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        tuple: (word, frequency) - The word with highest frequency and its count
    """
    word_frequency = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words and convert to lowercase
                words = line.lower().split()
                for word in words:
                    # Remove punctuation from the word
                    word = ''.join(char for char in word if char.isalnum())
                    if word:  # Only count non-empty words
                        word_frequency[word] = word_frequency.get(word, 0) + 1
        
        if not word_frequency:
            return None, 0
            
        # Find the word with highest frequency
        max_word = max(word_frequency.items(), key=lambda x: x[1])
        return max_word
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None, 0
    except Exception as e:
        print(f"Error: {str(e)}")
        return None, 0

# Example usage
if __name__ == "__main__":
    file_path = "sample.txt"
    word, frequency = find_highest_frequency_word(file_path)
    if word:
        print(f"The word with highest frequency is '{word}' with {frequency} occurrences.")
    else:
        print("No words found in the file.") 