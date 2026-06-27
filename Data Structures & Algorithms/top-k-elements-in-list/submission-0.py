class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            if i not in my_dict.keys():
                my_dict.update({i:1})
            if i in my_dict.keys():
                my_dict.update({i:my_dict.get(i)+1})

        sorted_data = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        sorted_data = list(sorted_data)



        result = []
        for i in range(k):
            result.append(sorted_data[i])
        
        return result