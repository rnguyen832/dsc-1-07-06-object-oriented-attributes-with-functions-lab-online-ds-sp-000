class School:
  
  def __init__(self, name=None, roster={}):
    self.name = name
    self.roster = roster

  def add_student(self, student, grade):
      try:
        self.roster[grade].append(student)
      except:
        self.roster[grade] = [] 
        self.roster[grade].append(student)
  
  def grade(self, grade):
    return self.roster[grade]

  def sort_roster(self):
    for grade in self.roster.keys():
      self.roster[grade].sort()
    print(sorted(self.roster.items()))
