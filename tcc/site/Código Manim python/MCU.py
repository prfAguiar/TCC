from manim import *

class MCU2(Scene):
    def construct(self):

        dot = Dot(color=RED)
        dot.move_to(ORIGIN)
        self.play(Create(dot, run_time=3))
        self.wait()

        line = Line(dot.get_center(), dot.get_center() + RIGHT * 3, color=YELLOW)
        self.play(Create(line, run_time=3))
        self.wait()

        dot2 = Dot(color=BLUE)
        dot2.move_to(line.get_end())
        self.play(Create(dot2, run_time=3))
        self.wait()

        circle = Circle(color=GREEN, radius=3)
        circle.move_to(dot.get_center())
        self.play(Create(circle, run_time=3))
        self.wait(2)
        curvedArrow = CurvedArrow(start_point=np.array([1,2,3]),end_point=np.array([3,3,3])).set_color(RED).to_edge(DOWN).scale(0.5)
        omega = MathTex(r"\omega").set_color(WHITE).next_to(curvedArrow,RIGHT)
        # arrow = Arrow(start=UP,end=DOWN).set_color(RED).to_edge(UP)
        # arrow2 = Arrow(start=RIGHT*3,end=LEFT*2).set_color(RED).to_edge(RIGHT)
        # arrow3 = Arrow(start=LEFT*3,end=RIGHT*2).set_color(RED).to_edge(LEFT)
        # arrow4 = Arrow(start=DOWN,end=UP).set_color(RED).to_edge(DOWN)
        self.wait()
        self.play(Write(omega))
        self.play(Rotating(dot2, about_point=dot.get_center(), run_time=6, rate_func=rush_into), Rotating(line, about_point=dot.get_center(), run_time=6, rate_func=rush_into), Create(curvedArrow))
        self.wait(2)