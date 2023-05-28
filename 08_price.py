def format_price(price):
    return f'Цена: {int(price)} руб.'

def main():
    current_price = format_price(56.24)
    print(current_price)

if __name__ == "__main__":
    main()