def tmp(input_file, output_file):
    sentences = []
    current_sentence = []

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:  # Empty line indicates end of a sentence
                if current_sentence:
                    sentences.append(' '.join(current_sentence))
                    current_sentence = []
            else:
                words = line.split(' ')
                if words:
                    current_sentence.append(words[0])

    if current_sentence:
        sentences.append(' '.join(current_sentence))

    with open(output_file, 'w') as file:
        file.write('\n'.join(sentences))

common = "testa"

input_filename = '../dataset/eng.' + common
output_filename = './eng.' + common + '.sentences'

tmp(input_filename, output_filename)
