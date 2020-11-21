import copy

def move(state, target, direction):
    state2 = copy.deepcopy(state)
    if direction == "up":
        state2[target] = [state2[target][0], state2[target][1]-1]
        if state2[target] in state:
            return state
        else:
            return state2

    if direction == "down":
        state2[target] = [state2[target][0], state2[target][1]+1]
        if state2[target] in state:
            return state
        else:
            return state2

    if direction == "right":
        state2[target] = [state2[target][0] + 1, state2[target][1]]
        if state2[target] in state:
            return state
        else:
            return state2

    if direction == "left":
        state2[target] = [state2[target][0] - 1, state2[target][1]]
        if state2[target] in state:
            return state
        else:
            return state2

def isonboard(guy):
    for cord in guy:
        if not (0 < cord < 6):
            return False
    return True

def ispatur(state):
    if state[0] == [3,3]:
        return True
    return False

def gmove(state, guy, direction):
    for i in range(5):
        state = move(state, guy, direction)
    return state


def play(seq, state):
    if len(seq) == 1:
        return

    if ispatur(state):
        print("soultion: ")
        for i in seq:
            print(i)
        print(f)
        return

    if not isonboard(state[0]):
        return

    for guy in state:
        if not isonboard(guy):
            return
            state = state.pop(state.index(guy))

    if isinstance(state[1], int):
        return

    for guy in range(len(state)):
        next = gmove(state, guy, "down")
        if next not in seq:
            seq.append(next)
            play(seq, next)
            seq.pop(-1)

    for guy in range(len(state)):
        next = gmove(state, guy, "up")
        if next not in seq:
            seq.append(next)
            play(seq, next)
            seq.pop(-1)

    for guy in range(len(state)):
        next = gmove(state, guy, "left")
        if next not in seq:
            seq.append(next)
            play(seq, next)
            seq.pop(-1)

    for guy in range(len(state)):
        next = gmove(state, guy, "right")
        if next not in seq:
            seq.append(next)
            play(seq, next)
            seq.pop(-1)

print(play([[[0,0], [0,0]],[[2,5], [1,1], [3,1], [5,1], [5,4]]], [[2,5], [1,1], [3,1], [5,1], [5,4]]))




