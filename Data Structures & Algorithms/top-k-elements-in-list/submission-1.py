from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        data = Counter(nums)
        for elem in data:
            heap_elem = (data[elem], elem)
            if len(heap) < k:
                heapq.heappush(heap, heap_elem)
            else:
                if heap[0][0] < heap_elem[0]:
                    heapq.heappushpop(heap, heap_elem)
        return list(map(lambda x: x[1], heap))
        