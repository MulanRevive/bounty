class 人:
  def __init__(self):
    self.姓, self.名 = "", ""

  @property
  def 取姓(self):
    return self.姓

  @property
  def 全名(self):
    return self.姓 + self.名

  @全名.setter  # 下面的 def 可不用`全名`
  def 全名(self, 姓名):
    self.姓 = 姓名[0:1]
    self.名 = 姓名[1:]

木兰 = 人()
木兰.全名 = "花木兰"
print("全名: " + 木兰.全名 +
  ", 姓: " + 木兰.取姓 +
  ", 名: " + 木兰.名)