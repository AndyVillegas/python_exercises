def print_formatted(number):
    max_binary_length = len(bin(number)[2:])
    for n in range(1, number + 1):
        decimal = str(n)
        octal = oct(n)[2:]
        hexadecimal = hex(n)[2:].upper()
        binary = bin(n)[2:]
        print("{} {} {} {}".format(
            decimal.rjust(max_binary_length),
            octal.rjust(max_binary_length),
            hexadecimal.rjust(max_binary_length),
            binary.rjust(max_binary_length)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)