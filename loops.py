def test_loop():
    # for loop
    nums = [3, 4, 16]

    print('This is an example of for loops')

    for num in nums:
        print(num ** 2)

    # while loop
    i = 3

    print('This is an example of while loops')

    while i < 258:
        print(i)
        i = i ** 2

    print('This is an example of nested loops')

    teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
    for team in teams:
        for name in team:
            print(name)

test_loop()