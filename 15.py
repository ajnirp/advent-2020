with open('15.txt') as f:
    spoken = [int(x) for x in f.read().split(',')]

# stores [second_most_recent_idx, most_recent_idx]
last_spoken = {num : [idx] for idx, num in enumerate(spoken)}

def update_last_spoken(num, new_idx, last_spoken):
    if num not in last_spoken:
        last_spoken[num] = [new_idx]
        return
    last_spoken[num].append(new_idx)
    if len(last_spoken[num]) > 2:
        last_spoken[num] = last_spoken[num][1:]

def speak(num, spoken, last_spoken):
    update_last_spoken(num, len(spoken), last_spoken)
    spoken.append(num)

def step(spoken, last_spoken):
    temp = last_spoken[spoken[-1]]
    if len(temp) == 1:
        speak(0, spoken, last_spoken)
    else:
        speak(temp[1] - temp[0], spoken, last_spoken)

for i in range(30000000):
    if i % 1000000 == 0:
        print(i)
    step(spoken, last_spoken)

print('Part 1', spoken[2020 - 1])
print('Part 1', spoken[30000000 - 1]) # this takes a while