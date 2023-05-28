def get_summ(one, two, sep='&'):
    return f'{one}{sep}{two}'

def main():
    summ = (get_summ('Learn', 'python')).upper()
    print(summ)

if __name__ == "__main__":
    main()