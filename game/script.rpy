# 이 파일에 게임 스크립트를 입력합니다.

define sounds = ['audio/Man_Typing_long.mp3', 'audio/Man_Typing_short.mp3']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

init:
    # 복도 1 이미지
    image bg hallway1_base = "images/bg/hallway1_base.jpg"
    image bg hallway1_diff1 = "images/bg/hallway1_diff1.png"
    image bg hallway1_diff2 = "images/bg/hallway1_diff2.jpg"

    # 복도 2 이미지
    image bg hallway2_base = "images/bg/hallway2_base.jpg"
    image bg hallway2_diff1 = "images/bg/hallway2_diff1.jpg"
    image bg hallway2_diff2 = "images/bg/hallway2_diff2.jpg"

    # 복도 3 이미지
    image bg hallway3_base = "images/bg/hallway3_base.jpg"
    image bg hallway3_diff1 = "images/bg/hallway3_diff1.jpg"
    image bg hallway3_diff2 = "images/bg/hallway3_diff2.jpg"

    image bg next_room = "images/bg/next_room.png"

init python:
    import random

    hallway_data = {
        1: {
            "correct": "hallway1_base.jpg",
            "options": ["hallway1_base.jpg", "hallway1_diff1.png", "hallway1_diff2.jpg"]
        },
        2: {
            "correct": "hallway2_base.jpg",
            "options": ["hallway2_base.jpg", "hallway2_diff1.jpg", "hallway2_diff2.jpg"]
        },
        3: {
            "correct": "hallway3_base.jpg",
            "options": ["hallway3_base.jpg", "hallway3_diff1.jpg", "hallway3_diff2.jpg"]
        }
    }

    progress = 1
    current_bg = "hallway1_base.jpg"

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('아르망', color="#c8ffc8", callback=type_sound)
define g = Character("아델린")
define h = Character("마주")

default password_0 = False
default password_1 = False
default password_2 = False
default password_3 = False
default door = True
default safe_password = False
default light = False
default dining_room_lock = True
default underground_lock = True
default garret_info = False

label start:

    play audio "마차끄는소리 도착.mp3"

    m "사람들이 사라진다고 하는 저택, 이곳에 도대체 어떤 진실이 숨겨져 있는가…"
   
    m "허나 두려움에 진실을 외면하는 것은, 기사로서 가장 비겁한 일이겠지."

    h "허허… 그게 언제적 얘기요?"

    h "귀신이니 실종이니, 다 뻔한 헛소문 아닙니까."

    h "세상 물정 모르는 이들이나 떠드는 이야기죠."

    play music "main_theme.mp3"

    m "벨포르 가의 이름으로 맹세하노니,"

    m "내가 이 저택에 깃든 모든 어둠을 밝혀내리라!!"

    h "벨포르라 했소? 그 가문도 한때 유명하긴 했지."

    h "뭐, 요즘 세상에 기사도니 명예니 따지는 양반은 선생뿐일 겁니다. 하하."

    "마차 주인은 돌아갔다."

    "나무 문은 무겁게 닫혀 있고 녹슨 자물쇠로 굳게 잠겨 있다."

    "옆 담장 아래에는 작고 허름한 구멍 하나가 있다."

    "아르망은 문 앞에서 고민에 빠진다."
   

label prologue:

    m "당신은 문 앞에 섰다."

    menu:
        "골라라"

        "정문":
            if door:
                $ door = False
                "문을 부수지 못했다."
                jump prologue
            else:
                "다시 한번 두드려 문을 부쉈다."
                jump mainhall

        "개구멍":
            jump mainhall

label mainhall:
    if password_0:
        if password_1:
            if password_2:
                if password_3:
                    jump hallway
    menu:
        "여긴 mainhall이다. 어디로 가지?"

        "지하실":
            if underground_lock:
                "지하실이 잠겨 있다."
                jump mainhall
            else:
                if light:
                    jump underground
                else:
                    "아무것도 안보인다."
                    jump mainhall
        "방":
            jump room

        "식당":
            if dining_room_lock:
                "식당 문이 잠겨있다."
                jump mainhall
            else:
                "식당 문을 열었다."
                jump dining_room
        "계단":
            jump two_stair

label two_stair:

    if garret_info:
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
    else:
        menu:
            "어디로 가지?"

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
        $ dining_room_lock = False
        "당신은 드라이버를 찾았다."

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
        $ underground_lock = False
        "당신은 지하실 문 열쇠를 찾았다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump mainhall    

label underground:

    if safe_password:
        "아무것도 없다."
    else:
        $ safe_password = True
        "당신은 금고의 비밀번호를 찾았다."
    


    menu:
        "어디로 갈까?"

        "나간다":
            jump mainhall    

label library:

    if safe_password:
        "아무것도 없다."
    else:
        $ password_2 = True
        "당신은 두번째 비밀번호를 찾았다."
        $ garret_info = True
        "당신은 다락방 정보에 대해 알았다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump two_stair   

label inner_room:

    if safe_password:
        "당신은 안방의 금고에서 네번째 비밀번호를 찾았다."
        $ password_3 = True
    else:
        "금고가 있다."
        "비밀번호가 걸려있다."

    menu:
        "어디로 갈까?"

        "나간다":
            jump two_stair

label garret:

    "다락방이다. 불을 켰다."

    $ light = True

    menu:
        "어디로 갈까?"

        "나간다":
            jump two_stair

label hallway:
    scene black
    with dissolve
    #play music "효과음" fadein 2.0

    m "여기는... 계속 같은 복도 같은데...?"
    jump hallway_loop

label hallway_loop:
    $ current_data = hallway_data[progress]
    $ current_bg = random.choice(current_data["options"])

    scene expression "bg/" + current_bg
    with dissolve

    m "이 복도... 무언가 너무너무 수상하다."

    menu:
        "앞으로 나아간다":
            if current_bg == current_data["correct"]:
                $ progress += 1
                if progress > 3:
                    jump next_room
                else:
                    m "앞으로 나아갔더니, 또 다른 복도가 나타났다..."
                    jump hallway_loop
            else:
                m "앞으로 나아갔지만... 돌아온 것 같다. 처음부터 다시 해보자."
                $ progress = 1
                jump hallway_loop

        "뒤로 돌아간다":
            if current_bg == current_data["correct"]:
                m "뒤로 돌아갔더니... 처음으로 돌아왔다. 다시 해보자."
                $ progress = 1
                jump hallway_loop
            else:
                $ progress += 1
                if progress > 3:
                    jump next_room
                else:
                    m "뒤로 돌아가자... 다른 복도가 나왔다."
                    jump hallway_loop

label next_room:
    #stop music fadeout 2.0
    scene bg next_room
    with fade
    m "여긴... 드디어 마지막 방인가...?"
    
    menu:
        "해피엔딩":
            jump happy_ending
        "배드엔딩":
            jump bad_ending

label happy_ending:
    "해피엔딩"

label bad_ending:
    "해피엔딩"



