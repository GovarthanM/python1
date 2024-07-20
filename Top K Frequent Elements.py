from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return [item for item, _ in count.most_common(k)]

print(topKFrequent([1,1,1,2,2,3], 2))
