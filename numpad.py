keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

for rows in keys:
    for columns in rows:
        print(columns, end=' ')
    print()
