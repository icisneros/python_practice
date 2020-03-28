
import os


if __name__ == '__main__':
    os.system("clear")
    f = open('ascii_banner.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()