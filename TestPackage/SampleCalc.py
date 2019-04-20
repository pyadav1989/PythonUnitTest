
class Calc:
    def add(self,num1,num2):
        return num1+num2;
    def sub(self,num1,num2):
        return num1-num2
    def mul(self,num1,num2):
        return num1*num2
    def div(self,num1,num2):
        return num1/num2

if __name__=="__main__":
    cal=Calc()
    print(cal.add(1,8))
    print(cal.sub(4,4))