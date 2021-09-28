import numpy as np
from copy import copy

class Scheduler:
  def __init__(self,first_date,presenters,avoid=[]):
    # Options.
    self.avoid=avoid
    self.next_date=first_date
    self.presenters=presenters

    # Hard code.
    self.months = ["Jan.","Feb.","March","April","May","June","July","August","Sept.","Oct.","Nov.","Dec."]
    self.day_month = [31, 28,    31,     30,     31,   30,    31,    31,      30,     31,    30,    31]
    self.midx=self.months.index(first_date[0])
    self.dates=[]

  def _step_date(self):
    self.next_date[1] += 7
    if self.next_date[1] > self.day_month[self.midx]:
      self.next_date[1] -= self.day_month[self.midx]
      self.midx = (self.midx + 1)%12
      self.next_date[0] = self.months[self.midx]


  def find_dates(self):
    for person in self.presenters:
      self.dates.append(copy(self.next_date))
      self._step_date()
      while self.next_date in self.avoid:
        self._step_date()

  def shuffle(self):
    """ Exports a suggested schedule. New for every call."""
    np.random.shuffle(self.presenters)

  def export(self, markdown=True):
    if not markdown:
      for date,presenter in zip(self.dates,self.presenters):
        date = "{0:<6} {1:>2}".format(*date)
        print("{}   {}".format(date,presenter))
    else:
      for date,presenter in zip(self.dates,self.presenters):
        date = "{0:<6} | {1:>2}".format(*date)
        print("{} | {}".format(date,presenter))

if __name__=='__main__':
  avoid = [["Oct.", 5]]
  presenters = [
      'Seher',
      'Bo',
      'Hao Xu', 
      'Zhi-Yu', 
      'Siyuan',
      'Yuan-Yao',
      'Brian',
      'Paul',
    ]
  first_date = ["Sept.",28]
  sched=Scheduler(first_date,presenters,avoid)
  sched.find_dates()
  sched.export(markdown=True)
