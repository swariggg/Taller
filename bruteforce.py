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
        pantalla = t.Screen()
        pantalla.title(f"Contraseña encontrada: {encontrada}")
        tortuga = t.Turtle()
        tortuga.speed(0)
        tortuga.hideturtle()

        left_margin, bottom_margin = -250, -250
        escala_x, escala_y = 500 / max(tiempos), 500 / max(contador_intentos) 

        tortuga.penup()
        tortuga.goto(left_margin, bottom_margin)
        tortuga.pendown()
        tortuga.forward(500)  
        tortuga.penup()
        tortuga.goto(left_margin, bottom_margin)
        tortuga.setheading(90)
        tortuga.pendown()
        tortuga.forward(500)  
        tortuga.penup()
        tortuga.goto(0, -270)
        tortuga.write("Tiempo (s)", align="center", font=("Arial", 10, "bold"))
        tortuga.goto(-270, 0)
        tortuga.write("Intentos", align="center", font=("Arial", 10, "bold"))
        tortuga.penup()
        tortuga.color("blue")
        for i in range(len(tiempos)):
            x = left_margin + tiempos[i] * escala_x
            y = bottom_margin + contador_intentos[i] * escala_y
            tortuga.goto(x, y)
            if i == 0:
                tortuga.pendown()

        tortuga.color("red")
        tortuga.dot(10)
        tortuga.write(f" {encontrada} ({contador_intentos[-1]} intentos, {tiempo_total:.4f}s)",
                      font=("Arial", 8, "normal"))

    pantalla.mainloop()
