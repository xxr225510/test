class mat:
    def demo(self):
        from matplotlib import pyplot as plt
        import matplotlib.animation as animation
        import numpy as np
        f = np.arange(0, 5, 0.1)
        # red dashes, blue squares and green triangles
        plt.plot(f, f, 'r--', f, f ** 2, 'bs', f, f ** 3, 'g^')
        plt.show()
        print f,f**2,f**3

mat().demo()