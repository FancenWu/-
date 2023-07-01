


def majorityElement(nums: List[int]) -> int:
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)


class Solution:

    def main(self):
        # Todo: Add your code here
        pass

    if __name__ == '__main__':
        main()
