def compute_sum(n):
    return sum(range(1, n+1))

def compute_product(n):
    product = 1
    for num in range(1, n+1):
        product *= num
    return product

def main():
    n = int(input("Enter a number: "))
    choice = input("Enter 's' to compute the sum or 'p' to compute the product: ")

    if choice == 's':
        result = compute_sum(n)
        print(f"The sum of numbers from 1 to {n} is: {result}")
    elif choice == 'p':
        result = compute_product(n)
        print(f"The product of numbers from 1 to {n} is: {result}")
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    main()








