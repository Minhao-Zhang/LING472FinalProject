common = "test"

label = "eng.{}.label".format(common)
error = "eng.{}.error".format(common)

with open("eng.train.sentences", "r") as f:
    sentence_lines = f.readlines()
    all_words = set()
    for line in sentence_lines:
        all_words.update([w.lower() for w in line.split()])

with open(label, "r") as f:
    label_lines = f.readlines()

A_count = 0
O_count = 0
FP_count = 0
FN_count = 0
E_count = 0
line_count = 0
with open(error, "w") as f:
    for line in label_lines:
        if len(line) > 1:
            a, b, c, d = line.split()
            line_count += 1
            if c != d:
                # print an ERROR at the 60th character at each line
                diff_length = 60 - len(line)
                if c[0] == d[0] and c[0] == "I":
                    f.write(line[0:-1] + " "*diff_length + "AMBIGUITY\n")
                    A_count += 1
                elif a.lower() not in all_words:
                    f.write(line[0:-1] + " "*diff_length + "OOV_ERROR\n")
                    O_count += 1
                elif c == "O":
                    f.write(line[0:-1] + " "*diff_length + "FP_ERROR\n")
                    FP_count += 1
                elif d == "O":
                    f.write(line[0:-1] + " "*diff_length + "FN_ERROR\n")
                    FN_count += 1
                else:
                    f.write(line[0:-1] + " "*diff_length + "ERROR\n")
                    E_count += 1
            else:
                f.write(line)
        else:
            f.write("\n")
print("Total lines: {}".format(line_count))
print("Total errors: {}".format(A_count + O_count + FP_count + FN_count + E_count))
print("Ambiguity: {}".format(A_count))
print("OOV: {}".format(O_count))
print("FP: {}".format(FP_count))
print("FN: {}".format(FN_count))
print("Others: {}".format(E_count))
