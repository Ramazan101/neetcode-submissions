class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dickt для того чтобы хранить ключ и занчение вычетаемых чисел
        seen = {}
        # проходим по данныи с пмщ loop for и даем им ключ-значение
        for idx, num in enumerate(nums):
            # здесь из target я вычитываю каждое заначение 
            # и присваиваю его в переменный difference пример target = 10 - 4(num)
            # и так до конца списка чисел
            difference = target - num
            # проверяю есть ли вычетанное число внутри словаря
            if difference in seen: # если да то переходим к выведению
                return [seen[difference], idx]
            # запоминаем текущее число и его индекс
            seen[num] = idx
        
        return []