data = "Margret Mauno"
freq = {}

for r in data:
    freq[r] = freq.get(r, 0) + 1

for key in data:
    print(key + " : " + str(freq[key]))

print("2-----------------------------------")

#
# def count_freq(li):
#     freq = {}
#     for item in li:
#         if item in freq:
#             freq[item] += 1
#         else:
#             freq[item] = 1
#     print(freq)
#
#
# li = [1, 1, 3, 2, 6, 5, 3, 1, 3, 3, 1, 4, 6, 4, 4, 2, 2, 2, 2]
# count_freq(li)

print("3-----------------------------------")

our_dict = {"a": 5, "b": 9, "c": 10}
our_dict.get("a", 0) + 1
print(our_dict)

