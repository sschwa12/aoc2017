from utils import read_file

data = read_file('24')
test_data = ['0/2', '2/2', '2/3', '3/4', '3/5', '0/1', '10/1', '9/10']


def split_pipe(pipe):
    return str.split(pipe, '/')


def has_zero(s: str):
    ends = split_pipe(s)
    return '0' in ends


# just need to create this structure and i think i have the solution to p1 but how tf
paths = {
    '0/2': ['2/2', '2/3'],
    '2/2': ['2/3'],
    '3/4': ['2/3', '3/5'],
    '3/5': ['3/4'],
    '0/1': ['10/1'],
    '10/1': ['9/10']
}

root_nodes = list(filter(has_zero, test_data))


def find_path_sum(node, strength):
    strength += sum([int(str_num) for str_num in split_pipe(node)])
    if node not in paths:
        return strength
    for p in paths[node]:
        return find_path_sum(p, strength)


solution = max([find_path_sum(node, 0) for node in root_nodes])
print(solution)
