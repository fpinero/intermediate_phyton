def test_error_handling():
    nums = [5, 2, 3, 10]

    try:
        avg = sum(nums) / len(nums)
        print('The average of the list is: ', avg)

    except:
        print('Cannot compute average - make sure you enter a list of integers!')

    finally:
        print('Feel free to rerun the code with another list of integers!')


def forcing_exception():
    nums = ['x', 'y', 'z']

    print('\nforncing an exception summing strings\n')
    try:
        print(sum(nums))

    except:
        print('Cannot print the sum! Your variables are not numbers.')

    finally:
        print('Hope you got the result you want!')


test_error_handling()
forcing_exception()
