def loading_bar(num):
    if num in range(0, 101) and num % 10 == 0:
        if num < 100:
            reps = num // 10
            bar = f"{num}% [{'%' * reps}{'.' * (10 - reps)}]\nStill loading..."
            return bar
        else:
            bar = f"100% Complete!\n[{'%' * 10}]"
            return bar

num = int(input())
print(loading_bar(num))