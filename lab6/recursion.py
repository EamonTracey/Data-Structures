def count_evens(nums: list) -> int:
    """
    Recursive trace for count_evens([1, 2, 3, 4, 5, 6]):

    Call 1: nums = [1, 2, 3, 4, 5, 6]    return count_evens([2, 3, 4, 5, 6])     3
    Call 2: nums = [2, 3, 4, 5, 6]       return 1 + count_evens([3, 4, 5, 6])    3
    Call 3: nums = [3, 4, 5, 6]          return count_evens([4, 5, 6])           2
    Call 4: nums = [4, 5, 6]             return 1 + count_evens([5, 6])          2
    Call 5: nums = [5, 6]                return count_evens([6])                 1
    Call 6: nums = [6]                   return 1 + count_evens([])              1
    Call 7: nums = []                    return 0                                0
    """

    # Base case: list is empty.
    if len(nums) == 0:
        return 0

    if nums[0] % 2:  # Odd number.
        return count_evens(nums[1:])
    else:  # Even number.
        return 1 + count_evens(nums[1:])


def sum_evens(nums: list) -> int:
    """
    Recursive trace for sum_evens([1, 2, 3, 4, 5, 6]):

    Call 1: nums = [1, 2, 3, 4, 5, 6]    return sum_evens([2, 3, 4, 5, 6])     12
    Call 2: nums = [2, 3, 4, 5, 6]       return 2 + sum_evens([3, 4, 5, 6])    12
    Call 3: nums = [3, 4, 5, 6]          return sum_evens([4, 5, 6])           10
    Call 4: nums = [4, 5, 6]             return 4 + sum_evens([5, 6])          10
    Call 5: nums = [5, 6]                return sum_evens([6])                 6
    Call 6: nums = [6]                   return 6 + sum_evens([])              6
    Call 7: nums = []                    return 0                              0
    """

    # Base case: list is empty.
    if len(nums) == 0:
        return 0

    if nums[0] % 2:  # Odd number.
        return sum_evens(nums[1:])
    else:  # Even number.
        return nums[0] + sum_evens(nums[1:])


def print_evens(nums: list):
    """
    Recursive trace for print_evens([1, 2, 3, 4, 5, 6]):

    Call 1: nums = [1, 2, 3, 4, 5, 6]    print_evens([2, 3, 4, 5, 6])    6 4 2
    Call 2: nums = [2, 3, 4, 5, 6]       print_evens([3, 4, 5, 6])       6 4 2
                                         print(2)
    Call 3: nums = [3, 4, 5, 6]          print_evens([4, 5, 6])          6 4
    Call 4: nums = [4, 5, 6]             print_evens([5, 6])             6 4
                                         print(4)
    Call 5: nums = [5, 6]                print_evens([6])                6
    Call 6: nums = [6]                   print_evens([])                 6
                                         print(6)
    Call 7: nums = []                    return
    """

    # Base case: list is empty.
    if len(nums) == 0:
        return

    if nums[0] % 2:  # Odd number.
        print_evens(nums[1:])
    else:  # Even number.
        print_evens(nums[1:])
        print(nums[0])


def print_evens_in_order(nums: list):
    """
    Recursive trace for print_evens_in_order([1, 2, 3, 4, 5, 6]):

    Call 1: nums = [1, 2, 3, 4, 5, 6]    print_evens_in_order([2, 3, 4, 5, 6])    2 4 6
    Call 2: nums = [2, 3, 4, 5, 6]       print(2)                                 2 4 6
                                         print_evens_in_order([3, 4, 5, 6])
    Call 3: nums = [3, 4, 5, 6]          print_evens_in_order([4, 5, 6])          2 4
    Call 4: nums = [4, 5, 6]             print(4)                                 2 4
                                         print_evens_in_order([5, 6])
    Call 5: nums = [5, 6]                print_evens_in_order([6])                2
    Call 6: nums = [6]                   print(6)                                 2
                                         print_evens_in_order([])
    Call 7: nums = []                    return
    """

    # Base case: list is empty.
    if len(nums) == 0:
        return

    if nums[0] % 2:  # Odd number.
        print_evens_in_order(nums[1:])
    else:  # Even number.
        print(nums[0])
        print_evens_in_order(nums[1:])


def is_prime(num: int, divisor: int = 2) -> bool:
    """
    Recursive trace for is_prime(7):

    Call 1: n = 7, divisor = 2    return is_prime(7, 2)    False
    Call 2: n = 7, divisor = 3    return is_prime(7, 3)    False
    """

    # Base case: number is less than 2.
    if num < 2:
        return False
    # Base case: number equals 2.
    if num == 2:
        return True
    # Base case: number is divisible by divisor.
    if num % divisor == 0:
        return False
    # Base case: divisor reached the square root of the number.
    if divisor * divisor > num:
        return True

    return is_prime(num, divisor + 1)


def factor_number(num: int, factor: int = 1) -> list:
    """
    Recursive trace for factor_number(6):

    Call 1: n = 6, factor = 1    return [1] + factor_number(6, 2)    [1, 2, 3]
    Call 2: n = 6, factor = 2    return [2] + factor_number(6, 3)    [2, 3]
    Call 3: n = 6, factor = 3    return [3] + factor_number(6, 4)    [3]
    Call 4: n = 6, factor = 4    return []                           []
    """

    # Base case: factor times 2 is greater than number.
    if factor * 2 > num:
        return []

    if num % factor == 0:  # Factor.
        return [factor] + factor_number(num, factor + 1)
    else:  # Not a factor.
        return factor_number(num, factor + 1)

