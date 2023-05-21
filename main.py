import tkinter as tk
def convert_number_to_words(number):
    # Define word representations of numbers
    num_words = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 1000000: 'million',
        1000000000: 'billion', 1000000000000: 'trillion'
    }

    def convert_less_than_thousand(num):
        if num == 0:
            return ''
        if num < 20:
            return num_words[num]
        if num < 100:
            return num_words[num - num % 10] + ' ' + num_words[num % 10]
        hundreds = num // 100
        tens = num % 100
        result = num_words[hundreds] + ' hundred'
        if tens > 0:
            result += ' ' + convert_less_than_thousand(tens)
        return result

    # Handle special cases
    if number < 0:
        return 'minus ' + convert_number_to_words(abs(number))
    if number < 1000:
        return convert_less_than_thousand(number)

    # Divide number into chunks of 3 digits (thousands, millions, billions, etc.)
    chunk_count = 0
    words = ''
    while number > 0:
        if number % 1000 != 0:
            chunk_words = convert_less_than_thousand(number % 1000)
            if chunk_count == 0:
                words = chunk_words
            else:
                words = chunk_words + ' ' + num_words[1000 ** chunk_count] + ' ' + words
        number //= 1000
        chunk_count += 1

    return words

def convert_button_click():
    number = int(number_entry.get())
    words = convert_number_to_words(number)
    output_label.configure(text=f"{number} in words: {words}")

def reset_button_click():
    number_entry.delete(0, tk.END)
    output_label.configure(text="")

# Create a new window
window = tk.Tk()
window.title("Number to Words Converter")

# Create input widgets
number_label = tk.Label(window, text="Enter a number:")
number_label.pack()
number_entry = tk.Entry(window)
number_entry.pack()

# Create output widget
output_label = tk.Label(window, text="")
output_label.pack()

# Create convert button
convert_button = tk.Button(window, text="Convert", command=convert_button_click)
convert_button.pack()

# Create reset button
reset_button = tk.Button(window, text="Reset", command=reset_button_click)
reset_button.pack()

# Run the Tkinter event loop
window.mainloop()