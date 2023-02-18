# 생성자 : 클래스는 초보자를 위해서 만듦, 근데 얘가 제대로 사용을 못해서 만들음.
class 회사프로그램:
    n1 = 0  
    n2 = 0  
    def AbsSum(self, n1, n2):
        result = 0
        if n1 < 0:
            n1 = n1 * -1
        self.n1 = n1   
        self.n2 = n2   
        abs(n2)
        result = n1 + n2
        return result

    def Last(self):     
        print(self.n1 + self.n2)
    # 생성자 __init__ : 객체화하는 순간에 사용될 메서드
    def __init__(self):
        # 생성자
        # 객체화를 하는 순간에 실행되어야하는 ㅋ노드
        # 객체화하는 순간에 클래스명 옆에 있는 ()
        print('회사프로그램 객체화를 성공했습니다!')
    def __init__(self, 수1, 수2):
        self.AbsSum(수1, 수2)

a = 회사프로그램(3, 5)
a.Last()
# 클래스 이름 옆에 있는 ()는 __init__ 를 사용하는 코드
b = 회사프로그램(5, -2) 
b.Last()

