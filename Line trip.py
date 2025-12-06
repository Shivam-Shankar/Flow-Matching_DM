t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    prev = 0
    ans = 0

    for i in range(n):
        a = int(input().strip())
        if a - prev > ans:
            ans = a - prev
        prev = a

    last_gap = 2 * (x - prev)
    if last_gap > ans:
        ans = last_gap

    print(ans)