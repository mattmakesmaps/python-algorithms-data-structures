import turtle
import itertools

colors = ['tan', 'yellow', 'tomato', 'violet', 'blue', 'LemonChiffon']
colorPicker = itertools.cycle(colors)

def tree(branchLen, t):
    # Base case, branchLen less then 5
    if branchLen > 5:
        t.color(colorPicker.next())
        t.forward(branchLen)
        t.right(40)
        # at the deepest level (branchLen == 15),
        # tree(15-15, t) will do nothing, allowing the
        # line after, `t.left(80)` to execute.
        tree(branchLen-15, t)
        t.left(80)
        tree(branchLen-15, t)
        t.right(40)
        # t.backward is required to reset the position
        # of the turtle for the previous tree() instance on outer frame.
        # NOTE: the same turtle is being used in every frame;
        # separate turtles are not created per frame.
        t.backward(branchLen)


if __name__ == '__main__':
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myWin.exitonclick()