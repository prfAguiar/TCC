from manim import * 
class VelocidadeEscalarMedia(Scene): 
	def construct(self): 
		line = NumberLine(x_range=[0, 10, 1], length=10, include_tip=True, include_numbers=True)
		medida = Tex('cm')
		medida.move_to(line).to_corner(RIGHT)
		dot = Dot(color=RED).move_to(line.number_to_point(2))
		self.add(line, medida, dot)
		self.play(FadeIn(line, shift=DOWN), FadeIn(dot))
		self.wait(2)
		dn = DecimalNumber(0)
		self.add(dn.next_to(line.number_to_point(0), LEFT, buff=0.5))
		self.clock = 0
		def update_timer(mob, dt):
			self.clock += dt
			if self.clock >= 5:
				self.clock = 5
			mob.set_value(self.clock)
		dn.add_updater(update_timer)
		self.add(dot)
		self.play(dot.animate.shift(RIGHT * 6), run_time=5, rate_func=linear)
		Double_arrow = DoubleArrow(start=line.number_to_point(2), end = line.number_to_point(8), buff=0 , color = BLUE)
		self.play(Write(Double_arrow), run_time = 3)
		self.play(FadeOut(line, medida, dot, dn))
		distancia = Tex('6 cm').next_to(Double_arrow, UP)
		self.play(Write(distancia))
		deslocamentoInicial = MathTex(r'S_{0} = 2 cm} ').scale(1).to_edge(DOWN)
		deslocamentoFinal = MathTex(r'S_{f} = 8 cm} ').scale(1).to_edge(DOWN)
		deslocamentoFinal.move_to(deslocamentoInicial).to_corner(RIGHT)
		deslocamentos = Group(deslocamentoInicial, deslocamentoFinal)
		self.add(deslocamentos.next_to(line, DOWN))
		self.wait(4)
		deltaDeslocamento = MathTex(r'\Delta s = 6 cm}').scale(1)
		deltaTempo = MathTex(r'\Delta t = 5 s}').scale(1).next_to(deltaDeslocamento, UP * 5)
		self.play(Transform(deslocamentos, deltaDeslocamento), Write(deltaTempo))
		self.play(FadeOut(Double_arrow, distancia))
		self.wait(5)
		calculoparcialVelocidadeEscalar = MathTex(r'V = rac{\Delta s}{\Delta t}=rac{s-s_{0}}{t-t_{0}} = rac{8 - 2cm}{5 s - 0s}').scale(2)
		calculocompletoVelocidadeEscalar = MathTex(r'V = rac{6}{5} = 1.2cm/s').scale(2)
		self.play(Write(calculoparcialVelocidadeEscalar))
		self.wait(3)
