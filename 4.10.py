import time

shapes = [
    """
     *
    ***
   *****
    """,

    """
    ***
   *   *
    ***
    """,

    """
    *   *
     * *
      *
    """,

    """
    *****
    *   *
    *****
    """
]

for i, shape in enumerate(shapes, 1):
    print(f"Hình {i}:\n{shape}")
    time.sleep(5)
