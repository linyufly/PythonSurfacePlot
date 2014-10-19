from pylab import *
from mpl_toolkits.mplot3d import Axes3D

def main():
  # x = linspace(0, 5, 10)
  # y = x * x

  # print x

  # figure()
  # plot(x, y, 'r')
  # xlabel('x')
  # ylabel('y')
  # title('test')
  # show()

  a = 0.75
  b = 1.5
  def f(x, y):
    return cos(a * x) * cos(b * y)

  x_axis = linspace(0, 2 * pi, 100)
  y_axis = linspace(0, 2 * pi, 100)
  X, Y = meshgrid(x_axis, y_axis)
  Z = f(X, Y)

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1, projection = '3d')
  p = ax.plot_surface(X, Y, Z, rstride = 4, cstride = 4, linewidth = 0)

  # ax = fig.add_subplot(1, 2, 2, projection = '3d')
  # p = ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = cm.coolwarm, linewidth = 0, antialiased = False)

  # cb = fig.colorbar(p, shrink = 0.5)

  show()

  # fig, ax = subplots()
  # xlabel('x')
  # ylabel('y')
  ## p = ax.pcolor(X, Y, Z, cmap = cm.RdBu, vmin = Z.min(), vmax = Z.max())
  ## cb = fig.colorbar(p, ax = ax)
  # cnt = ax.contour(Z, cmap = cm.RdBu, vmin = Z.min(), vmax = Z.max(), extent = [0, 2 * pi, 0, 2 * pi])
  # show()

if __name__ == '__main__':
  main()
