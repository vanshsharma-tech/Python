# Q15. Print a checkerboard pattern (like a chessboard) using `*` and spaces.

rows, cols = 8, 8  # change size if you like

for i in range(rows):
    row_chars = []
    for j in range(cols):
        row_chars.append("*" if (i + j) % 2 == 0 else " ")
    print(" ".join(row_chars))
