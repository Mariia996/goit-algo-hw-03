import turtle
import sys

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch's Snowflake: level {order}")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    try:
        level = int(input("Enter the recursion level (0 or more): "))
        if level < 0:
            print("Please enter a whole number more than 0.")
        else:
            sys.setrecursionlimit(3000 if level > 4 else 1000)
            draw_koch_curve(level)
    except ValueError:
        print("Error! Enter an integer!")

if __name__ == "__main__":
    main()
