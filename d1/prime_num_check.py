def prime_checker(number):
    is_prime = True
    num_list = []
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            num_list.append(num)
    if is_prime:
        print(f'{number} is a Prime number')
    else:
        print(f'{number} is not a Prime number\n' 
              f'It can be fully divided by: {num_list}')


n = int(input("Check this number: "))
prime_checker(number=n)
