import random
import time
import subprocess


class BarChartTool(object):
  def __init__(self):
    self.MAX_X = 0
    self.GOOD_X = 0
    self.BAD_X = 0
    self.LINES = 0

    self.initialize()

  def initialize(self):
    # MAX_X = 80.0
    self.MAX_X = int(subprocess.check_output(['tput', 'cols']))
    self.GOOD_X = self.MAX_X / 100.0 * 50.0
    self.BAD_X = self.MAX_X - self.MAX_X / 100.0 * 3.0
    self.LINES = 3

  def plot(self):
    counter = 0
    previous_lines = 0

    for i in range(500):
      self.initialize()
      for i in (x for x in range(random.randrange(0, 100, 10))):
        x = random.randrange(0, self.MAX_X + 1)
        lines = int(subprocess.check_output(['tput', 'lines']))
        if previous_lines != lines:
          counter = 0
        previous_lines = lines

        x_str_len = len(str(x))
        x_shortened = x - x_str_len

        if x >= self.BAD_X:
          print '\033[0;41m ' * x_shortened, str(x),'\033[m'  # red
        elif x <= self.GOOD_X:
          print '\033[0;42m ' * x_shortened, str(x), '\033[m'  # green
        else:
          print '\033[0;3m ' * x_shortened, str(x), '\033[m'   # white

        # Clear half of the screen vertically.
        #
        # # if counter == LINES:
        # if counter == lines / 2:
        #     time.sleep(0.3)
        #     subprocess.call('clear')
        #     counter = 0
        # counter += 1

        # time.sleep(random.randrange(0.00, 0.05, 0.01))
        delay = float(str('0.0' + str(random.randrange(0, 9))))
        # print 'DELAY: ', delay  # DEBUG
        time.sleep(delay)
        l = 1

      # Separator
      #
      # print '\n%s\n' % ((('\033[37;35mx' * 80) + '\033[m\n') * l)
      print '%s' % ((('\033[37;46m-' * self.MAX_X) + '\033[m\n') *
                    l).rstrip()  # blue


if __name__ == '__main__':
  bar_chart_tool = BarChartTool()
  bar_chart_tool.plot()
