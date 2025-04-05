# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
# define e = Character('아이린', color="#c8ffc8")
# define e1 = Character("신승환")
# define e2 = Character("정승원")

# default password_0 = False
# default password_1 = False
# default password_2 = False
# default password_3 = False
# default safe_password = False
# default light = False

# label start:

#     e "당신은 문 앞에 섰다."

#     menu:

#         "골라라"

#         "정문":
#             jump mainhall

#         "개구멍":
#             jump room

# label mainhall:
#     if password_0:
#         if password_1:
#             if password_2:
#                 if password_3:
#                     jump hallway
#     menu:
#         "어디로 가지?"

#         "지하실":
#             if light:
#                 jump underground
#             else:
#                 "잠겨 있다"
#                 jump mainhall
    
#         "방":
#             jump room
#         "식당":
#             jump dining_room
#         "계단":
#             jump two_stair

# label two_stair:
    
#     menu:
#         "어디로 가지?"

#         "다락방":
#             jump garret
#         "서재":
#             jump library
#         "안방":
#             jump inner_room
#         "내려간다":
#             jump mainhall

# label room:

#     if password_0:
#         "아무것도 없다."
#     else:
#         $ password_0 = True
#         "당신은 첫번째 비밀번호를 찾았다."

#     menu:
#         "어디로 갈까?"

#         "나간다":
#             jump mainhall

# label dining_room:

#     if password_1:
#         "아무것도 없다."
#     else:
#         $ password_1 = True
#         "당신은 세번째 비밀번호를 찾았다."

#     menu:
#         "어디로 갈까?"

#         "나간다":
#             jump mainhall    


# label underground:

#     "당신은 두번째 비밀번호를 찾았다."
    
#     if password_2:
#         "아무것도 없다."
#     else:
#         $ password_2 = True
#         "당신은 두번째 비밀번호를 찾았다."

#     menu:
#         "어디로 갈까?"

#         "나간다":
#             jump mainhall    

# label library:

#     if safe_password:
#         "아무것도 없다."
#     else:
#         $ safe_password = True
#         "당신은 금고의 비밀번호를 찾았다."

#     menu:
#         "어디로 갈까?"

#         "나간다":
#             jump two_stair   

# label inner_room:

#     if safe_password:
#         "당신은 네번째 비밀번호를 찾았다."
#         $ password_3 = True
#     else:
#         "금고가 있다."
#         "비밀번호가 걸려있다."

#     menu:
#         "어디로 갈까?"

#         "나간다":
#             jump two_stair

# label hallway:

#     "복도의 끝이 보인다"

#     menu:
#         "해피엔딩":
#             jump happy_ending
#         "배드엔딩":
#             jump bad_ending

# label garret:

#     "다락방이다. 불을 켰다."

#     $ light = True

#     menu:
#         "어디로 갈까?"

#         "나간다":
#             jump two_stair


# label happy_ending:
#     "해피엔딩"

# label bad_ending:
#     "해피엔딩"


# 특수복도 기믹 - 8번출구 모티브
# image 문을 사용해 이미지를 정의합니다.
init:
    # 복도 1 이미지
    image bg hallway1_base = "images/bg/hallway1_base.png"
    image bg hallway1_diff1 = "images/bg/hallway1_diff1.png"
    image bg hallway1_diff2 = "images/bg/hallway1_diff2.png"

    # 복도 2 이미지
    image bg hallway2_base = "images/bg/hallway2_base.png"
    image bg hallway2_diff1 = "images/bg/hallway2_diff1.png"
    image bg hallway2_diff2 = "images/bg/hallway2_diff2.png"

    # 복도 3 이미지
    image bg hallway3_base = "images/bg/hallway3_base.png"
    image bg hallway3_diff1 = "images/bg/hallway3_diff1.png"
    image bg hallway3_diff2 = "images/bg/hallway3_diff2.png"

    image bg next_room = "images/bg/next_room.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define p = Character("나")

init python:
    import random

    hallway_data = {
        1: {
            "correct": "hallway1_base.png",
            "options": ["hallway1_base.png", "hallway1_diff1.png", "hallway1_diff2.png"]
        },
        2: {
            "correct": "hallway2_base.png",
            "options": ["hallway2_base.png", "hallway2_diff1.png", "hallway2_diff2.png"]
        },
        3: {
            "correct": "hallway3_base.png",
            "options": ["hallway3_base.png", "hallway3_diff1.png", "hallway3_diff2.png"]
        }
    }

    progress = 1
    current_bg = "hallway1_base.png"

label start:
    scene black
    with dissolve
    #play music "효과음" fadein 2.0

    p "여기는... 계속 같은 복도 같은데...?"
    jump hallway_loop

label hallway_loop:
    $ current_data = hallway_data[progress]
    $ current_bg = random.choice(current_data["options"])

    scene expression "bg/" + current_bg
    with dissolve

    p "이 복도... 무언가 이상하다."

    menu:
        "앞으로 나아간다":
            if current_bg == current_data["correct"]:
                $ progress += 1
                if progress > 3:
                    jump next_room
                else:
                    p "앞으로 나아갔더니, 또 다른 복도가 나타났다..."
                    jump hallway_loop
            else:
                p "앞으로 나아갔지만... 돌아온 것 같다. 처음부터 다시 해보자."
                $ progress = 1
                jump hallway_loop

        "뒤로 돌아간다":
            if current_bg == current_data["correct"]:
                p "뒤로 돌아갔더니... 여전히 같은 복도다."
                $ progress = 1
                jump hallway_loop
            else:
                $ progress += 1
                if progress > 3:
                    jump next_room
                else:
                    p "뒤로 돌아가자... 다른 복도가 나왔다."
                    jump hallway_loop

label next_room:
    #stop music fadeout 2.0
    scene bg next_room
    with fade
    p "여긴... 드디어 마지막 방인가...?"
    return

