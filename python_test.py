def digit_sum(nums: int) -> int:
    sum_nums = 0
    for num in str(abs(nums)):
        sum_nums += int(num)

    return sum_nums


print(digit_sum(123))  #6  (1 + 2 + 3)
print(digit_sum(-456))  #15 (4 + 5 + 6)
print(digit_sum(0))  #0 (0)



def unique_once(list_nums: list[int]) -> list[int]:
    count_unique_nums = {}

    for num in list_nums:
        # if num in count_unique_nums:
        count_unique_nums[num] = count_unique_nums.get(num, 0) + 1

    return [n for n in count_unique_nums if count_unique_nums[n] == 1]

print(unique_once([1,2,2,3,4,4]))  #[1,3]
print(unique_once([5,5,6,7]))  #[6,7]
print(unique_once([9,9])) #[]



def char_count(text: str) -> dict:
    count_unique_char = {}

    for char in text:
        count_unique_char[char] = count_unique_char.get(char, 0) + 1


    return count_unique_char


print(char_count("hello")) #{'h':1,'e':1,'l':2,'o':1}
print(char_count("banana")) #{'b':1,'a':3,'n':2}
print(char_count("")) #{}



l = ["cat", "elephant", "dog"]
print(len(l[0]))

def longest_word(texts: list[str]) -> str:
    max_lenght = ""

    for char in texts:
        if len(char) > len(max_lenght):
            max_lenght = char


    return max_lenght


print(longest_word(["cat", "elephant", "dog"]))  # elephant
print(longest_word(["hi", "hello"]))             # hello
print(longest_word([]))                          # None



def sort_employees(key_values: list[dict]) -> list[dict]:
    return sorted(key_values, key=lambda key_s: (-key_s["salary"], key_s["name"]))


print(sort_employees([
    {"name": "Bek", "salary": 500},
    {"name": "Aida", "salary": 700},
    {"name": "Azat", "salary": 500},
]))
# [
#     {"name": "Aida", "salary": 700},
#     {"name": "Azat", "salary": 500},
#     {"name": "Bek", "salary": 500},
# ]



sort_employees = [
    {"name": "Bek", "salary": 500},
    {"name": "Aida", "salary": 700},
    {"name": "Azat", "salary": 500},
]

dicts = {}

for dictt in sort_employees:
    for key, value in dictt.items():
        dicts[key, value] = value, key

sorted_s = sorted(dicts)

print(dicts)
print(sorted_s)

print(dir(dicts))