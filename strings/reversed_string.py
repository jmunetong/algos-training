
def reverse_string(sample: str):
    sample_x = sample.split(" ")
    new_string = ""
    for i in range(len(sample_x)-1, -1, -1):
        new_string = new_string + f" {sample_x[i]}"
    return new_string

if __name__ == '__main__':
    ex="i love programming very much"
    print(reverse_string(ex))