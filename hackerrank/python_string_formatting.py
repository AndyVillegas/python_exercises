def print_formatted(number):
    max_binary_length = len(bin(number)[2:])
    for n in range(1, number + 1):
        print("{} {} {} {}".format(
            str(n).rjust(max_binary_length),
            oct(n)[2:].rjust(max_binary_length),
            hex(n)[2:].upper().rjust(max_binary_length),
            bin(n)[2:].rjust(max_binary_length)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)