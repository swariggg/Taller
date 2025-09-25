import time
import turtle

contraseña = "nana"
alfabeto = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=[]{};:,.<>/?|~`")
intentos = 0
encontrado = False
tiempo_inicio = time.time()
tiempos = []
contador_intentos = []

def probar(cadena):
    global intentos, encontrado, tiempos, contador_intentos
    intentos += 1
    tiempos.append(time.time() - tiempo_inicio)
    contador_intentos.append(intentos)
    if cadena == contraseña:
        encontrado = True
        return cadena
    if len(cadena) < len(contraseña):
        for letra in alfabeto:
            if encontrado:
                break
            resultado = probar(cadena + letra)
            if resultado:
                return resultado
    return None

posible = probar("")
tiempo_total = time.time() - tiempo_inicio

if posible:
    print("Contraseña encontrada:", posible)
    print("Intentos:", intentos)
    print(f"Tiempo total: {tiempo_total:.6f}")
else:
    print("No se encontró la contraseña")
    print("Intentos:", intentos)
    print("Tiempo (s):", tiempo_total)

if not tiempos or not contador_intentos:
    print("No hay datos para graficar.")
else:
    pantalla = turtle.Screen()
    pantalla.title(f"Intentos vs Tiempo - Encontrado: {posible} ({intentos} intentos)")
    pantalla.setup(width=1000, height=650)
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    left_margin = -450
    bottom_margin = -280
    width = 900
    height = 520

    t.penup()
    t.goto(left_margin, bottom_margin)
    t.pendown()
    t.forward(width)
    t.penup()
    t.goto(left_margin, bottom_margin)
    t.left(90)
    t.pendown()
    t.forward(height)
    t.penup()

    max_tiempo = max(tiempos)
    max_intentos = max(contador_intentos)
    escala_x = width / max_tiempo if max_tiempo > 0 else 1
    escala_y = height / max_intentos if max_intentos > 0 else 1

    t.color("black")
    t.penup()
    for i in range(6):
        valor = (max_tiempo / 5) * i
        x = left_margin + valor * escala_x
        t.goto(x, bottom_margin - 10)
        t.write(f"{valor:.2f}", align="center", font=("Arial", 8, "normal"))
        t.goto(x, bottom_margin)
        t.pendown()
        t.goto(x, bottom_margin + 6)
        t.penup()

    for i in range(6):
        valor = (max_intentos / 5) * i
        y = bottom_margin + valor * escala_y
        t.goto(left_margin - 8, y - 4)
        t.write(f"{int(valor)}", align="right", font=("Arial", 8, "normal"))
        t.goto(left_margin, y)
        t.pendown()
        t.goto(left_margin + 6, y)
        t.penup()

    t.goto(left_margin + width / 2, bottom_margin - 40)
    t.write("Tiempo transcurrido (s)", align="center", font=("Arial", 10, "bold"))
    t.goto(left_margin - 60, bottom_margin + height / 2)
    t.write("Intentos", align="center", font=("Arial", 10, "bold"))

    t.color("blue")
    t.penup()

    if len(tiempos) == 1:
        x0 = left_margin + tiempos[0] * escala_x
        y0 = bottom_margin + contador_intentos[0] * escala_y
        t.goto(x0, y0)
        t.dot(6)
    else:
        x0 = left_margin + tiempos[0] * escala_x
        y0 = bottom_margin + contador_intentos[0] * escala_y
        t.goto(x0, y0)
        t.pendown()
        t.dot(4)
        for i in range(1, len(tiempos)):
            x = left_margin + tiempos[i] * escala_x
            y = bottom_margin + contador_intentos[i] * escala_y
            t.goto(x, y)
            t.dot(4)
        t.penup()

    if posible:
        t.color("red")
        t.goto(left_margin + tiempos[-1] * escala_x, bottom_margin + contador_intentos[-1] * escala_y)
        t.dot(10)
        t.penup()
        t.goto(left_margin + tiempos[-1] * escala_x + 12, bottom_margin + contador_intentos[-1] * escala_y + 6)
        t.write(f"{posible} ({intentos} intentos, {tiempo_total:.4f}s)", font=("Arial", 9, "normal"))

    pantalla.mainloop()
