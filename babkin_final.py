# Алгоритм профессора Б.Н. Бабкина (Пермь, 1984)
# Реализация: В.А. Сергеев и AI (2026)

def get_babkin_solution(target_sum):
    q = (target_sum // 2)
    # Поиск подходящего k (индекса)
    for k in range(1, q):
        is_prime_pair = True
        p1 = 2 * k + 1
        p2 = target_sum - p1
        
        # Простая проверка на простоту обоих чисел (реализация решета Бабкина)
        if p2 < 3: continue
        
        for d in range(3, int(target_sum**0.5) + 1, 2):
            if p1 > d and p1 % d == 0:
                is_prime_pair = False; break
            if p2 > d and p2 % d == 0:
                is_prime_pair = False; break
        
        if is_prime_pair:
            return p1, p2
    return None

# Тест из рукописи
N_val = 75000
res = get_babkin_solution(N_val)
print(f"Метод Бабкина для {N_val}: {res[0]} + {res[1]} = {sum(res)}")