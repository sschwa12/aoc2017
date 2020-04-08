with open('aoc2017-12.data') as f:
    lines = f.read().splitlines()
    parsed = [str.split(ln, ' <-> ') for ln in lines]
    pipes = {p[0]: str.split(p[1], ', ') for p in parsed}

count = 0
num_groups = 1  # start at 1 because we'll run it once for part 1
seen = set()


# part 1
def get_num_programs(group_id):
    if group_id not in seen:
        seen.add(group_id)
        global count
        count += 1
        for gid in pipes[group_id]:
            get_num_programs(gid)


get_num_programs('0')
print(count)

# part 2
for gid in pipes.keys():
    if gid not in seen:
        get_num_programs(gid)
        num_groups += 1

print(num_groups)
