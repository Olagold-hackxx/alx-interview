#!/usr/bin/python3
"""Implement lockboxes"""


def canUnlockAll(boxes):
    """Implement lockboxes"""
    unlocked_boxes = [0]

    if not (isinstance(boxes, list) and
            all(isinstance(sublist, list) for sublist in boxes)):
        return False

    for box in boxes:
        for key in box:
            for j in range(1, len(boxes)):
                if key not in unlocked_boxes and key == j:
                    unlocked_boxes.append(key)
            break

    return len(unlocked_boxes) == len(boxes)
