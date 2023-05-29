common = "test"

label = "eng.{}.label".format(common)
error = "eng.{}.error".format(common)

with open(label, "r") as f:
    label_lines = f.readlines()

with open(error, "w") as f:
    for line in label_lines:
        if len(line) > 1:
            a, b, c, d = line.split()
            
            if c != d:
                # print an ERROR at the 60th character at each line
                diff_length = 60 - len(line)
                f.write(line[0:-1] + " "*diff_length + "ERROR\n")
            else:
                f.write(line)
        else:
            f.write("\n")
