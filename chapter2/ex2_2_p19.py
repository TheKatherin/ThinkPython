import math

# part 1
r = 5
volume = 4/3 * math.pi * r**3
print('part 1: Volume of sphere with radius 5 ? %d' % volume)

# part 2
cover_price = 24.95
discount = 0.4
shipping_cost_1 = 3
shipping_cost_n = 0.75
copies_amount = 60

whole_cost = (cover_price - cover_price * discount) * copies_amount + shipping_cost_1 + shipping_cost_n * (copies_amount - 1)
print('part 2: The total whole sale cost for 60 copies is %d$' % whole_cost)

# part 3
time_start = 6 * 60 + 52

interval_1 = 1
pace_1 = 8 + 15/60
interval_2 = 3
pace_2 = 7 + 12/60
interval_3 = 1
pace_3 = 8 + 15/60

time_1 = interval_1 * pace_1
time_2 = interval_2 * pace_2
time_3 = interval_3 * pace_3

time_finish = time_start + time_1 + time_2 + time_3
print('part 3: I will be at home at %d:%d' % (int(time_finish//60), int(time_finish%60)))




