#!/usr/bin/python3
"""Implement lockboxes"""


def canUnlockAll(boxes):
    """Implement lockboxes"""
    unlocked_boxes = [0]

    for box in boxes:
        for key in box:
            for j in range(1, len(boxes)):
                if key not in unlocked_boxes and key == j:
                    unlocked_boxes.append(key)
            break

    return len(unlocked_boxes) == len(boxes)
