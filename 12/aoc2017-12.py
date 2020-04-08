with open('aoc2017-12.data') as f:
    lines = f.read().splitlines()
    parsed = [str.split(ln, ' <-> ') for ln in lines]
    pipes = {p[0]: str.split(p[1], ', ') for p in parsed}

count = 0


def get_num_programs(group_id, seen=set()):
    if group_id not in seen:
        seen.add(group_id)
        global count
        count += 1
        for gid in pipes[group_id]:
            get_num_programs(gid, seen)


get_num_programs('0')
print(count)
