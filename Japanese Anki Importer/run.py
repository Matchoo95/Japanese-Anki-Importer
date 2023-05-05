import csv
import re
import nltk

nltk.download('punkt')

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        # Replace all consecutive (。) characters with (。\n)
        line = re.sub(r'。+', '。\n', line)
        # Tokenize the sentences using nltk
        sentences = nltk.sent_tokenize(line.strip())
        # Write each sentence to the output file with a space character after the newline character
        for sentence in sentences:
            f_out.write(sentence + "\n ")
