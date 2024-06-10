#return the number of indices where heights[i] != expected[i].


def height_checker(heights):
    expected = sorted(heights)
    total_unmatched = 0

    for i in range(len(heights)):
        if heights[i] != expected[i]:
            total_unmatched += 1

    return total_unmatched


#alternatively#
def height_checker(heights):
    return sum(h != s for h, s in zip(heights, sorted(heights)))

#testing#
heights = [1,1,4,2,1,3]
print(height_checker(heights))