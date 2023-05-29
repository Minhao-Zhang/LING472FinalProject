def tmp(original, parse, output):
    sentences = []
    current_sentence = []

    with open(parse, 'r') as file:
        all_lines = file.readlines()
        all_lines = [line.strip().split(" ") for line in all_lines]

    l = 0
    w = 0

    with open(output, 'w') as output_f:
        with open(original, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:  # Empty line indicates end of a sentence
                    l += 1
                    w = 0
                else:
                    words = line.split(' ')
                    words[2] = words[3]
                    to_replace = all_lines[l][w].split("__")[1]
                    if to_replace[0] == "B":
                        to_replace = "I" + to_replace[1:]
                    words[3] = to_replace
                    w += 1
                    output_f.write(' '.join(words) + '\n')

    if current_sentence:
        sentences.append(' '.join(current_sentence))

common = "testa"

original = f'./dataset/eng.{common}'
parse = f'./testing/eng.{common}.result'
output = f'./testing/eng.{common}.label'

tmp(original, parse, output)
