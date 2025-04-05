# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")

default password_0 = False
default password_1 = False
default password_2 = False
default password_3 = False
default safe_password = False
default light = False

label start:

    e "당신은 문 앞에 섰다."

    menu:

        "골라라"

        "정문":
            jump mainhall

        "개구멍":
            jump room

label mainhall:
    if password_0:
        if password_1:
            if password_2:
                if password_3:
                    jump hallway
    menu:
        "어디로 가지?"

        "지하실":
            if light:
                jump underground
            else:
                "잠겨 있다"
                jump mainhall
    
        "방":
            jump room
        "식당":
            jump dining_room
        "계단":
            jump two_stair

label two_stair:
    
    menu:
        "어디로 가지?"

        "다락방":
            jump garret
        "서재":
            jump library
        "안방":
            jump inner_room
        "내려간다":
            jump mainhall

label room:

    if password_0:
        "아무것도 없다."
    else:
        $ password_0 = True
        "당신은 첫번째 비밀번호를 찾았다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump mainhall

label dining_room:

    if password_1:
        "아무것도 없다."
    else:
        $ password_1 = True
        "당신은 세번째 비밀번호를 찾았다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump mainhall    


label underground:

    "당신은 두번째 비밀번호를 찾았다."
    
    if password_2:
        "아무것도 없다."
    else:
        $ password_2 = True
        "당신은 두번째 비밀번호를 찾았다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump mainhall    

label library:

    if safe_password:
        "아무것도 없다."
    else:
        $ safe_password = True
        "당신은 금고의 비밀번호를 찾았다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump two_stair   

label inner_room:

    if safe_password:
        "당신은 네번째 비밀번호를 찾았다."
        $ password_3 = True
    else:
        "금고가 있다."
        "비밀번호가 걸려있다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump two_stair

label hallway:

    "복도의 끝이 보인다"

    menu:
        "해피엔딩":
            jump happy_ending
        "배드엔딩":
            jump bad_ending

label garret:

    "다락방이다. 불을 켰다."

    $ light = True

    menu:
        "어디로 갈까?"

        "나간다":
            jump two_stair


label happy_ending:
    "해피엔딩"

label bad_ending:
    "해피엔딩"