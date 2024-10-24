import time

def typing_speed_test():
    # Sample sentence to type
    test_sentence = "The quick brown fox jumps over the lazy dog."
    print("Typing Speed Test")
    print("Type the following sentence as fast as you can:")
    print(f"Sentence: {test_sentence}")
    
    input("Press Enter when you are ready to start...")
    
    # Record the start time
    start_time = time.time()
    
    # Get user input
    user_input = input("\nStart typing: ")
    
    # Record the end time
    end_time = time.time()
    
    # Calculate the time taken
    time_taken = end_time - start_time
    
    # Calculate typing speed in words per minute
    word_count = len(test_sentence.split())
    wpm = (word_count / time_taken) * 60
    
    # Calculate accuracy
    correct_chars = sum(1 for i, char in enumerate(user_input) if i < len(test_sentence) and char == test_sentence[i])
    accuracy = (correct_chars / len(test_sentence)) * 100
    
    # Show results
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Your typing speed is: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the typing speed test
typing_speed_test()
