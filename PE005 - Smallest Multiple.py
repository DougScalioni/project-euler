def smallest_positive_number_that_is_evenly_divisible_by_all_of_the_numbers_from_1_to(m):
    factors = [1]
    for i in range(2, m + 1):
        for d in factors:
            i = i / d if i % d == 0 else i
        factors.append(i)
    output = 1
    for f in factors:
        output *= f
    return output


print(smallest_positive_number_that_is_evenly_divisible_by_all_of_the_numbers_from_1_to(20))
