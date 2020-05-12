def pow(num, power):
    if (power == 1):
        return num
    return num * pow(num, power-1)

if __name__ == '__main__':
    v=pow(3,4)
    print('{}'.format(v))