def func():
    value = "not-none"

    <caret>if value is None:
        print("None")
        raise RuntimeError()