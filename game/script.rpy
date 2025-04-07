#이 파일에 게임 스크립트를 입력합니다.
define sounds = ['audio/Man_Typing_long.mp3', 'audio/Man_Typing_short.mp3']
define sounds2 = ['audio/Woman_Typing_long.mp3', 'audio/Woman_Typing_short.mp3']

# 사운드 관련 코드
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
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()
init python:
    def type_sound2(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            renpy.sound.queue(renpy.random.choice(sounds2))
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v

        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

#호감도 바 관련 코드
init:
    screen stat_overlay:
        # 호감도 창
        frame:
            padding (15, 15)
            background "#70798380"
            align (1.0, 0.0)
            xmaximum 250
            ymaximum 200

            vbox:
                text "기사도{space=15}[p_bar[0]]" size 16 color "#FFFFFF"
                bar:
                    value AnimatedValue(p_bar[0], 100, delay=1.0)
                    range 100
                    style "fixed_bar"

                text " " size 3

                text "호감도{space=15}[p_bar[1]]" size 16 color "#FFFFFF"
                bar:
                    value AnimatedValue(p_bar[1], 100, delay=1.0)
                    range 100
                    xalign 0.0
                    style "fixed_bar"
init -5 python:
    # 호감도 스타일
    style.fixed_bar = Style(style.default)

    style.fixed_bar.xmaximum = 200
    style.fixed_bar.ymaximum = 15
    style.fixed_bar.left_gutter = 0
    style.fixed_bar.right_gutter = 0
    style.fixed_bar.left_bar = Frame("images/bar/bar_full.png", 0, 0)
    style.fixed_bar.right_bar = Frame("images/bar/bar_empty.png", 0, 0)
    
## 앞에서 부터 이미지 차례대로 공간별로 구분해서 넣어주세요. ##
## init: <-- 폴더처럼 쓰시면 돼요(이미지, 캐릭터 정의 등 간단한것만) ##
## init python: <-- 실제로 동작하는 코드들 (함수, 계산, 복잡한 동작이 이루어지는 것들) ##

###### 아직 정리 안된 이미지들  #####
init:
    image bg dream = "images/bg/dream.png"
    image forest = "images/bg/forest.png"
    image surprise_attack = "images/event/scary.png"
    
    image black = "images/bg/black.jpg"

# 안방 이미지
init:
    image hidden_word = "hidden_word.jpg"

#특수복도 이미지
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

#특수복도 이미지 랜덤 생성 모듈    
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
    clears = 0
    current_bg = "hallway1_base.jpg"

#캐릭터 이미지
init:
    # 아르망
    #image ??? = "???"
    # 아델린
    image adeline_surprise = "images/chr/adeline_surprise.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('아르망', color="#c8ffc8")#, callback=type_sound)
define g = Character("아델린", callback=type_sound2)
define h = Character("마주", callback=type_sound2)
define n = nvl_narrator #n을 나레이터 캐릭터로 설정
define l = Character('꼬마 유령', color="#b2cd68")

default p_bar = [0, 0]
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
    scene forest
    play audio "마차끄는소리 도착.mp3"
    show screen stat_overlay

    m "사람들이 사라진다고 하는 저택, 이곳에 도대체 어떤 진실이 숨겨져 있는가…"
    $ p_bar[0] += 10
   
    m "허나 두려움에 진실을 외면하는 것은, 기사로서 가장 비겁한 일이겠지."

    h "허허… 그게 언제적 얘기요?"

    h "귀신이니 실종이니, 다 뻔한 헛소문 아닙니까."

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

    m "이를 어쩐다."

    menu:
        "골라라"

        "정문":
            if door:
                play sound "검으로 벽을 두드리는 소리.mp3"
                $ door = False
                "문을 부수지 못했다."
                jump prologue
            else:
                "다시 한번 두드려 문을 부쉈다."
                jump first_event

        "개구멍":
            jump first_event

label first_event:
    m "오래된 저택이여, 나는 벨포르 가문의 이름으로… 너의 침묵 속에 감춰진 진실을 밝히러 왔노라!"

    "그 순간, "
    play audio "old door1.mp3"

    "갑자기 저 멀리 2층 복도 끝에서 끼익 하고 문이 열리는 소리가 들렸다."

    play audio "걷는소리 구두.mp3"
    "또각… 또각… 구두 소리 같은 발걸음이 메아리친다."

    play audio "아이 웃는소리 숏.mp3"
    m "…역시, 단순한 소문은 아니였나보군?"

    m "2층 난간 위, 붉은 눈만이 어둠 속에서 번뜩인다."

    m "누구냐! 지금 당장 모습을 드러내지 않으면!"

    play audio "스크림1.mp3"
    scene surprise_attack

    "……!!"
    play audio "칼소리.mp3"
    "순간, 아르망은 비명을 지르며 칼을 휘두른다."

    scene black

    m "사라져라아아앗!! 벨포르의 이름으로!! 이 망령아아아!!"

    "그 순간—"
    play audio "여자비명.mp3"
    g "꺄아아아악!!!!!"

    "처절하고 놀란, 분명 여자아이의 비명소리가 터져나온다."

    "아르망의 검이 허공을 베었고, 그도 순간 움찔하며 눈을 뜬다."

    show adeline surprise at Transform(xalign=0.5, yalign=0.2) 

    "그리고… 거기. 눈앞에 선 채 놀란 얼굴로 그를 쳐다보는 소녀가 서 있다."

    m "…소녀…?"

    "깜짝 놀란 눈으로 그를 바라보다가, 잠시 정적이 흐른 뒤, 마치 스스로도 민망한 듯 눈을 깜빡인다."

    g "…아, 맞다. 나… 이미 죽었지…"

    show adeline embrassed at Transform(xalign=0.5, yalign=0.2) 
    
    g "후훗… 미안, 네가 그렇게까지 반응할 줄은 몰랐어. 오랜만에 만난 사람이라."
    
    g "무슨일로 왔니?"

    m "나는 벨포르 가문의 아르망 드 벨포르! 이 저택에서 귀신이 사람을 잡아간다는 이야기를 듣고 해결하러 왔다!"

    m "너가 그 귀신인가?"

    show adeline 호기심 at Transform(xalign=0.5, yalign=0.2) 

    g "아니. 나의 이름은 아델린 드 로르망. 이 저택의 주인 로르망 백작의 첫째 딸이야."

    g "그리고 너가 찾는 귀신은 아마도 저택 지하실 깊은 곳에 있는 악령일꺼야."

    m "그런 정보를 왜 나에게 알려주지?"

    show adeline sad at Transform(xalign=0.5, yalign=0.2) 

    g "그 악령은 나를 괴롭히거든......"

    g "그래서 너가 그 악령을 처리해주면 나는 좋은 일이니까."

    m "그런가. 그럼 나는 악령을 처리하러 가겠다."

    g "아. 이 집에는 많은 유령이 있어. 멀쩡한 유령은 아마 나뿐일꺼야. 조심해."

    m "헛된 걱정이다!"


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
    m "흠, 책상 위에 상자가 있군."

    play audio "걷는 소리2.mp3"

    play audio "old door3.mp3"

    m "음? 열쇠가 있군."

    l "히히히, 내꺼야~" (가져간다)

    m "이놈, 내놔라!"

    l "나 잡으면 줄게!"

    m "이 망할 유령!"

    l "여기야, 여기~"

    m "헉... 헉..."

    l "여기야 여기! 빨리~"

    m "헉... 헉..."

    # gimmick "위의 대사 랜덤 반복 5회"

    l "즐거웠어! 자, 여기 가져가~ 꺄르륵!"

    m "헉... 헉... 힘들어......"

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
        if password_3:
            "아무것도 없다."
        else:
            scene black with fade #안방 이미지
            "당신은 방 구석에서 잠긴 금고를 발견했다"
            "옆에는 수상한 종이가 함께 있다."
            jump hidden_word

            label hidden_word:
            show hidden_word with fade

            m "아까 얻은 종이에 뭔가 단서가 있을 것 같아..."
            m "단어를 찾아 입력해보자."

            $ correct_answer = "secret"

            label input_loop:
                $ player_input = renpy.input("숨겨진 단어는 무엇일까?").strip().lower()
                if player_input == correct_answer:
                    "끼익... 금고가 열리는 소리가 들린다."
                    "당신은 안방의 금고에서 네번째 일기장을 찾았다."
                    $ password_3 = True
                    jump diary4
                else:
                    m "그건 아닌 것 같아... 다시 생각해보자."
                    jump input_loop

            label diary4:
                nvl clear
                n "일기내용 어쩌고 저쩌고.."
                
                menu:
                    "어디로 갈까?"
                    
                    "나간다":
                        jump two_stair
    else:
        "금고가 있지만 열리지 않는다."
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
    scene hallway1_base
    m "이 복도..."
    jump hallway_stage

label hallway_stage:
    if progress == 1:
        jump hallway_show_answer_1
    elif progress == 2:
        jump hallway_show_answer_2
    elif progress == 3:
        jump hallway_show_answer_3

label hallway_show_answer_1:
    scene bg hallway1_base
    with dissolve
    m "이상하다. 계속 같은 곳을 돌고있는 기분이 들어."
    pause 2
    m "으윽.. 머리가.."
    scene black with fade
    pause 1
    jump hallway_loop
label hallway_show_answer_2:
    scene bg hallway2_base
    with dissolve
    m "두 번째 복도군... 눈에 익혀둬야겠어."
    pause 2
    m "크윽.. 또 머리가.."
    scene black with fade
    pause 1
    m "또인가..? 젠장!"
    jump hallway_loop
label hallway_show_answer_3:
    scene bg hallway3_base
    with dissolve
    m "이게 마지막 복도... 잘 기억해둬야 해."
    pause 2
    m "으윽.."
    scene black with fade
    pause 1
    m "익숙해지기 힘든 감각이군.."
    jump hallway_loop

label hallway_entry:
    if clears == 0:
        jump hallway_stage
    else:
        jump hallway_loop

label hallway_loop:
    $ current_data = hallway_data[progress]
    $ current_bg = random.choice(current_data["options"])

    scene expression "bg/" + current_bg
    with dissolve

    m "전이랑은 조금 다른 느낌이야. 그런데, 나만 그렇게 느끼는 건가...?"

    menu:
        "앞으로 나아간다":
            if current_bg == current_data["correct"]:
                $ clears += 1
                if clears >= 2:
                    $ progress += 1
                    $ clears = 0
                    if progress > 3:
                        jump next_room
                    else:
                        m "앞으로 나아갔더니, 또 다른 복도가 나타났다..."
                        jump hallway_entry
                else:
                    m "이 방향이 맞는 것 같다. 하지만 아직 무언가 부족해..."
                    jump hallway_loop
            else:
                m "앞으로 나아갔지만... 돌아온 것 같다. 처음부터 다시 해보자."
                $ progress = 1
                $ clears = 0
                jump hallway_entry

        "뒤로 돌아간다":
            if current_bg == current_data["correct"]:
                m "뒤로 돌아갔더니... 처음으로 돌아왔다. 다시 해보자."
                $ progress = 1
                $ clears = 0
                jump hallway_entry
            else:
                $ clears += 1
                if clears >= 2:
                    $ progress += 1
                    $ clears = 0
                    if progress > 3:
                        jump next_room
                    else:
                        m "뒤로 돌아가자... 다른 복도가 나왔다."
                        jump hallway_entry
                else:
                    m "다른 복도가 나왔군. 하지만 아직 뭔가 부족한 느낌이야."
                    jump hallway_loop

label next_room:
    scene bg dream
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
