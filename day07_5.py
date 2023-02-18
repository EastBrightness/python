# 자동차 클래스를 만들어보세요
# 속성(매개변수) : 차주인, 색상, 차종
# 기능(메서드) : 차정보를 보여주는것. (반드시 세팅이 미리 된 생성자를 만들어야함.)

class 자동차:
    차주인 = ''
    색상 = ''
    차종 = ''
    
    def __init__(self, 차주인, 색상, 차종):
        self.차주인 = 차주인 # 즉, 밑에서 받은 '아빠'를 self.차주인 으로 넣어준다는 얘기임. 
        # 이렇게 되면, 차주인 인 '아빠'는 한번 쓰고 사라지지만, self.차주인은 __init__ 공간으로 가서
        # 더 오래 가니까 다른 곳에서도 사용이 간으하겠지.
        self.색상 = 색상
        self.차종 = 차종

    def 자동차정보(self):
        print(self.차주인 + self.색상 + self.차종)
        # 위에서 넣어준 self. 에 들어가있는 친구니까, 사용해줘도 문제가 없는 것임.

    def 차운전(self):
        print(self.차주인 + " 운전을 합니다")

아빠차 = 자동차('아빠', 'black', 'gv80')
엄마차 = 자동차('엄마', 'red', 'g70')

아빠차.자동차정보()
아빠차.차운전()

엄마차.자동차정보()
엄마차.차운전()

# 메서드가 같아도 객체가 다르면, 그 객체에 해당하는 메서드와 매개변수로 사용이 된다.

