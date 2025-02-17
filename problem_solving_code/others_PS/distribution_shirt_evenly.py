def shirts_distribution_evenly(shirts, bags):
    per_bag_shirts = shirts // bags
    
    extra_shirts = shirts % bags
 
    distribution = [per_bag_shirts] * (bags - extra_shirts) + [per_bag_shirts + 1] * extra_shirts
    
    return distribution

# Example usage:
shirts = int(input('Type your shirts number: ').strip())
bags = int(input('Type your bags number: ').strip())
result = shirts_distribution_evenly(shirts, bags)
print(result)

def test_shirts_distribution_evenly():
    # Test Case 1
    assert shirts_distribution_evenly(100, 10) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    # Test Case 2
    assert shirts_distribution_evenly(50, 7) == [7, 7, 7, 7, 7, 7, 8]

    # Test Case 3
    assert shirts_distribution_evenly(75, 5) == [15, 15, 15, 15, 15]

    # Test Case 4
    assert shirts_distribution_evenly(120, 8) == [15, 15, 15, 15, 15, 15, 15, 15]

    # Test Case 5
    assert shirts_distribution_evenly(30, 6) == [5, 5, 5, 5, 5, 5]

    # Test Case 6
    assert shirts_distribution_evenly(10, 3) == [3, 3, 4]

    # Test Case 7
    assert shirts_distribution_evenly(200, 10) == [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

    # Test Case 8
    assert shirts_distribution_evenly(80, 12) == [6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7]

    # Test Case 9
    assert shirts_distribution_evenly(55, 8) == [6, 7, 7, 7, 7, 7, 7, 7]

    # Test Case 10
    assert shirts_distribution_evenly(18, 5) == [4, 4, 4, 3, 3] or [3, 3, 4, 4, 4]

    print("All test cases passed!")

# Run the test cases
test_shirts_distribution_evenly()