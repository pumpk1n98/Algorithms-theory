def schedule_triathlon(participants):
    """
    participants — список кортежей (id, swim, bike, run)
    """

    # считаем "хвост" (велосипед + бег)
    participants_sorted = sorted(
        participants,
        key=lambda x: x[2] + x[3],
        reverse=True
    )
    time_swim = 0
    finish_times = []

    # моделируем процесс
    for pid, swim, bike, run in participants_sorted:
        time_swim += swim  # следующий стартует после предыдущего
        finish_time = time_swim + bike + run
        finish_times.append((pid, finish_time))
    total_time = max(finish_times, key=lambda x: x[1])[1]
    return participants_sorted, total_time, finish_times
######################################################################
# пример использования
participants = [
    ("A", 5, 20, 10),
    ("B", 6, 15, 12),
    ("C", 4, 25, 8),
]
order, total, finishes = schedule_triathlon(participants)

print("Оптимальный порядок:")
for p in order:
    print(p[0])

print("\nВремя завершения:", total)
print("\nФиниши участников:")
for f in finishes:
    print(f)