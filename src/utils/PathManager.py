import traceback
import os


def to_absolute(path: str) -> str:
    stack = traceback.extract_stack()
    base_dir = os.path.dirname(stack[0].filename)
    absolute_path = os.path.normpath(os.path.join(base_dir, path))

    return absolute_path
