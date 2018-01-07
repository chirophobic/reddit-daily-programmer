import re

def main():
    running = True
    while running:
        line = input('> ')

        if line == 'exit':
            running = False

        print(tokenize(line))


def tokenize(string):
    split = re.split(r'([^A-Za-z0-9_])', string)
    tokens = [item for item in split if item != ' ' and item != '']
    return tokens


if __name__ == '__main__':
    main()
