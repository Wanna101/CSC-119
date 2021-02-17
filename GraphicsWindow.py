def main():
    from ezgraphics import GraphicsWindow
    win = GraphicsWindow()
    canvas = win.canvas()
    canvas.drawRect(5, 10, 20, 30)
    win.wait()
main()
