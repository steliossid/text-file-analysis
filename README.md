# text-file-analysis
Command line Python scripts analyzing shakespeare.txt file

- **text_stats.py**: Module that is responsible for analyzing and getting statistical results from shakespeare.txt file about letter frequency, total number of words, number of unique words and five most common words along with the words that most commonly follow them. 
If user provides a second argument, all output is written to that file.
Example: `python text_stats.py shakespeare.txt <output-file>`


- **generate_text.py**:  Module that is responsible to generate text randomly based on the successor of a given word from shakespeare.txt. 
User must provide the first word of the sentence and the number of words of the sentence as arguments.
Example: `python generate_text.py shakespeare.txt king 500`