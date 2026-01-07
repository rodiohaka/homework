



numbers = [1 , 2, 3, 4, 5]
print(numbers)
mid_index = len(numbers) // 2

if len(numbers) % 2 != 0:
    mid_index += 1

part1 = numbers[:mid_index]
part2 = numbers[mid_index:]
print(part1)
print(part2)
result = [part1, part2]
print(result)
