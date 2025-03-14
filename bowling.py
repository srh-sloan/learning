
def get_spare_score(frames, current_frame_index):
    next_frame = frames[current_frame_index+1]
    next_frame_score = 0
    if next_frame == "X" or "/" in next_frame:
        next_frame_score = 10
    else:
        next_frame_score = int(next_frame[0])

    return 10 + next_frame_score

def get_strike_score(frames, current_frame_index):
    next_frame = frames[current_frame_index+1]
    next_frame_score = 0
    for roll in next_frame:
        if roll.isdigit():
            next_frame_score += int(roll)
        elif roll == "/":
            next_frame_score = 10
        elif roll == "X":
            # TODO this is messy
            next_frame_score = 10
            next_next_frame = frames[current_frame_index+2]
            roll2 = next_next_frame[0]
            if roll2.isdigit():
                next_frame_score += int(roll2)
            elif roll2 == "/" or roll == "X":
                next_frame_score += 10

    return 10 + next_frame_score

# TODO spare or strike on last turn

def get_total_score(all_frames:str) -> int:
    score = 0
    frames = all_frames.split(" ")
    print(frames)

    for i, frame in enumerate(frames):
        if frame == "X":
            score += get_strike_score(frames, i)
        elif "/" in frame:
            score += get_spare_score(frames, i)
        else:
            score += int(frame[0]) + int(frame[1])


    return score
