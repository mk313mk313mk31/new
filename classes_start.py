#
# Example file for working with classes
#


class myclass():
  def method1(self):
    print("ali")
  def method2(self,somestring):
    print("sala"+" "+somestring)
  

def main():
  c = myclass()
  c.method1()
  c.method2("khoobi?")
  
if __name__ == "__main__":
  main()
