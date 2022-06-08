class Methods:
    """Класс с методами для вычисления интеграллов"""
    def sympson(self, f, n, val_b):
        """ Метод вычисления интегралов методом Симпсона(парабол).

        На вход подается необходимая функция(f), число проходов(n) и список значений верхнего предела(val_b).
        Нижний предел фиксированный и равен -1
        """
        a = -1
        sympson_val = dict()
        for b in val_b:

            h = (b - a) / (2 * n)
            tmp_sum = float(f(a)) + float(f(b))

            for step in range(1, 2 * n):
                if step % 2 != 0:
                    tmp_sum += 4 * float(f(a + step * h))
                else:
                    tmp_sum += 2 * float(f(a + step * h))

            result = tmp_sum * h / 3
            sympson_val[b] = result

        return sympson_val

    def rect(self, f, n, val_b):
        """ Метод вычисления интегралов методом прямоугольников.

        На вход подается необходимая функция(f), число проходов(n) и список значений верхнего предела(val_b).
        Нижний предел фиксированный и равен -1
        """
        a = -1
        rect_val = dict()

        for b in val_b:
            h = (b - a) / float(n)
            total = sum([f((a + (k * h))) for k in range(0, n)])
            result = h * total
            rect_val[b] = result

        return rect_val

    def trap(self, f, n, val_b):
        """ Метод вычисления интегралов методом трапеций.

        На вход подается необходимая функция(f), число проходов(n) и список значений верхнего предела(val_b).
        Нижний предел фиксированный и равен -1
        """
        a = -1
        trap_val = dict()

        for b in val_b:
            delx = (b - a) / n
            ind = a + delx
            sumfpod = 0

            while (ind < b):
                sumfpod += 2 * f(ind)
                ind += delx

            sumfpod = (sumfpod + f(a) + f(b)) * delx / 2
            trap_val[b] = sumfpod

        return trap_val
