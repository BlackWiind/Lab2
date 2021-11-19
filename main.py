from array import array

iterations = 0
n = 4
accuracy = 0.0001
difference = 0
x = array('d', [])
prev_calculation = array('d', [])
diff_calculation = array('d', [])

x.append(2.5)
x.append(-2.43)
x.append(-0.88)
x.append(0.74)

while True:
    iterations += 1
    for i in range(n):
        prev_calculation = x
        x[0] = 2.5 - 0.3 * prev_calculation[1] - 0.13 * prev_calculation[2] + 0.31 * prev_calculation[3]
        x[1] = -2.43 + 0.08 * prev_calculation[0] + 0.3 * prev_calculation[2] + 0.35 * prev_calculation[3]
        x[2] = -0.88 + 0.17 * prev_calculation[0] + 0.29 * prev_calculation[1] + 0.2 * prev_calculation[3]
        x[3] = 0.74 - 0.23 * prev_calculation[0] - 0.19 * prev_calculation[1] + 0.4 * prev_calculation[2]

        for j in range(n):
            if abs(x[i] - prev_calculation[i] > difference):
                difference = abs(x[i] - prev_calculation[i] > difference)

        if difference > accuracy:
            break

print("\tОтвет:")
for i in range(n):
    print("\tx", i, "= %.4f" % x[i])
print("Количество итераций = ", iterations)
input("Нажмите любую клавишу...")
