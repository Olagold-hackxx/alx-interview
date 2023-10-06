def canUnlockAll(boxes):
    unlocked_boxes = {0}
    new_keys = [0]

    while new_keys:
        current_box = new_keys.pop()
        keys = boxes[current_box]
        for key in keys:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                new_keys.append(key)

    return len(unlocked_boxes) == len(boxes)
