#!/usr/bin/python3
"""Implement lockboxes"""


def canUnlockAll(boxes):
    """Implement lockboxes"""
    unlocked_boxes = [0]

    for box in boxes:
        if len(box) >= 1:
            key = box[0]
        else:
            key = 0
        for j in range(1, len(boxes)):
            if key not in unlocked_boxes and key == j:
                unlocked_boxes.append(key)

    return len(unlocked_boxes) == len(boxes)
