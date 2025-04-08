#이 파일에 게임 스크립트를 입력합니다.
define sounds = ['audio/Man_Typing_long.mp3', 'audio/Man_Typing_short.mp3']
define sounds2 = ['audio/Woman_Typing_long.mp3', 'audio/Woman_Typing_short.mp3']
define sounds3 = ['', '']

# 메인홀 브금 재생 관련 코드 
init python:
    def bgm_not_playing():
        return renpy.music.get_playing(channel="music") != "bgm_main.mp3"

    def bgm_not_playing2():
        return renpy.music.get_playing(channel="music") != "bgm_piano.mp3"
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
            
    def type_sound3(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
            renpy.sound.queue(renpy.random.choice(sounds3))
init python:
    renpy.music.register_channel("laugh1", "sfx", loop=False)
    renpy.music.register_channel("laugh2", "sfx", loop=False)     
#좌/우 사운드 기믹
init python:
    import random
    left_sounds = ["audio/laughmech_left1.mp3","audio/laughmech_left2.mp3","audio/laughmech_left3.mp3"]
    right_sounds = ["audio/laughmech_right1.mp3","audio/laughmech_right2.mp3","audio/laughmech_right1.mp3"]

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
    image surprise_attack2 = "images/event/scary2.png"
    image black = "images/bg/black.jpg"
    image 저택 = "images/bg/저택.png"
    image 자물쇠 = "images/bg/자물쇠.png"
    image 샹들리에 = "images/obj/샹들리에.png"

# 안방 이미지

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

#캐릭터 이미지 변경
init:
    # 아델린
    image adeline_surprise = "images/chr/adeline_surprise.png"
    image 마주 = "images/chr/마차 주인.png"
    image 마주생각 = "images/chr/마차 주인 생각.png"



# 게임에서 사용할 캐릭터를 정의합니다.
define h = Character("마부", callback=type_sound2)
define m = Character('아르망', color="#044604", font="tway_sky.ttf", what_font="tway_fly.ttf", callback=type_sound)
define g = Character("아델린", callback=type_sound2, what_font="tway_air.ttf")
define n = nvl_narrator #n을 나레이터 캐릭터로 설정
define l = Character('꼬마 유령', color="#d4840b")
define l2 = Character('꼬마 유령', color="#d4840b")
define G = Character('???')
define s = Character("오르골 유령",)
default p_bar = [0, 0]
default diary_0 = False
default diary_1 = False
default diary_2 = False
default diary_3 = False
default door = True
default safe_info = False
default light = False
default room_first_visit = True
default dining_room_lock = True
default underground_lock = True
default inner_room_lock = True
default garret_info = False
default chandelier_count = 0
default dining_room_first = True
default first_event_check = True
default library_first = True
default garret_to_first = True
default underground_first = True
default safe_password = False
default photo_count = 0
default inner_room_first = True
default garret_first = True
# $ p_bar[0] += 10 기사도 증가
# $ p_bar[1] += 10 호감도 증가

label start:
    stop music 
    play audio "마차소리.mp3"
    scene black 
    centered "{size=+40}{font=tway_sky.ttf}1 9 X X{/font}{/size}"
    stop audio 
    play audio "마차소리 도착.mp3"
    scene black 
    play music "bgm_garden.mp3"
    centered "{size=+40}{font=tway_sky.ttf}영국, 어느 지방{/font}{/size}"
    stop audio
    play audio "비.mp3"
    scene black 
    scene forest with fade
    
    show screen stat_overlay
    h "도착이오"
    h "이 곳이 바로 ??? 저택이오"
    m "......"
    m "이 곳인가..."
    m "{alpha=*0.5}사람들이 계속 사라진다는 대저택...{/alpha}"
    m "{alpha=*0.5}이곳엔 대체 어떤 진실이 숨겨져 있는가...{/alpha}"
   
    m "{alpha=*0.5}두려움으로부터 진실을 외면하는 것은, 기사로서 가장 비겁한 일{/alpha}"
    m "벨포르 가의 이름으로 맹세하노니"
    scene 저택 with vpunch

    m "{size=+10}내가 이 저택에 깃든 모든 어둠을 밝혀내리라!{/size}"
    
    show 마주생각 at Transform(xalign=0.5, yalign=0.2) 
    h "음...?"
    h "벨포르 가문이라고 했소?"
    h "벨포르라… 오랜만에 듣는 이름이로군"
    h "허허, 그 가문도 한때는 꽤 이름을 날렸지"
    h "하지만 요즘은 그 이름을 아는 이조차 많지 않겠소만"
    
    m "저 저택 근처에서는 귀신이 나타나서 사람을 잡아간다고 들었소"
    m "그대는 혹시 이 이야기에 대해 알고있는가?"
    hide 마주생각
    show 마주 at Transform(xalign=0.5, yalign=0.2) 
    h "하하 그게 언제적 얘기요?"
    h "귀신이니 실종이니, 다 뻔한 헛소문 아니오"
    h "물론 이 근방에 사는 사람들이라면 모두 알고있는 내용이네만"
    h "이제는 다들 웃어넘기는 옛 소문일뿐이오"
    h "귀신보다는 세금이 더 무섭지"    

    h "요즘 세상에 기사도니 명예니 따지는 양반은 아마 선생밖에 없을거요."
    h "하하하"
    
    hide 마주 with dissolve

    "마차 주인은 돌아갔다."
    
    scene 자물쇠 
    "나무 문은 무겁게 닫혀 있고 녹슨 자물쇠로 굳게 잠겨 있다."

    "옆 담장 아래에는 작고 허름한 구멍 하나가 있다."

    "아르망은 문 앞에서 고민에 빠진다."

label prologue:

    m "이를 어쩐다."

    menu:
        "선택하자"

        "정문":
            if door:
                
                $ door = False
                
                m "하등한 자는 담장을 넘고, 도둑은 어둠을 틈타지만… 그러나 나는 기사."
                m "벨포르 가문의 아르망! 명예로운 자는 언제나 정문으로 들어가는 법"
                play audio "검으로 벽을 두드리는 소리.mp3"
                "검을 들어 자물쇠를 단숨에 내리친다."
                "자물쇠와 문은 끄떡도 하지 않는다."
                
                jump prologue
            else:
                
                m "이깟 문조차 내 의지로 열지 못한다면, 이 검은 무얼위해 존재한단 말인가!"
                
                play audio "검으로 벽을 두드리는 소리.mp3"
                "다시 한번 검을 들어 자물쇠를 단숨에 내리친다." 

                "문이 쾅 소리와 함께 열리며 먼지가 풀풀 날린다."
                
                play audio "철문여는소리.mp3"
                "문이 열렸다."
                jump first_event

        "개구멍":
            m "생각해보면 큰 문제도 작게 보이는 법"
            m "무리하게 정문을 부수는 것은 경박함의 상징이 될 수도 있으니."
            "아르망은 조심스레 개구멍 앞에 쪼그려 앉는다."
            scene black
            play audio "기어가다.mp3"
            m "명예란 때로…"
            extend "상황에 따라 형태를 바꾸는 법이지… "
            extend "하아…"
            jump first_event

label first_event:
    stop music 
    stop audio

    scene black
    m "오래된 저택이여, 나는 벨포르 가문의 이름으로…"
    m "{size=+10}너의 침묵 속에 감춰진 진실을 밝히러 왔노라!{/size}"

    "그 순간, "
    play audio "old door1.mp3"

    "갑자기 저 멀리 2층 복도 끝에서 끼익 하고 문이 열리는 소리가 들렸다."

    play audio "걷는소리 구두.mp3"
    "또각… 또각… 구두 소리 같은 발걸음이 메아리친다."

    play music "여자 콧노래.mp3"
    
    m "이 소리는 뭐지...?"
    m "......"
    m "역시, 단순한 헛소문은 아니였던 모양이로군"

    "2층 난간 위, 어둠 속 소녀의 콧노래만이 들릴 뿐이다."

    m "누구냐! 지금 당장 모습을 드러내라!"
    
    stop music 
    play audio "스크림1.mp3"

    scene surprise_attack

    "……!!"
    play audio "칼소리.mp3"
    "순간, 아르망은 비명을 지르며 칼을 휘두른다."

    scene black
    play audio "칼 휘두름.mp3"
    m "사라져라아아앗!! 벨포르의 이름으로!! 이 망령아아아!!"

    "그 순간—"
    
    play audio "여자비명.mp3"
    g "꺄아아아악!!!!!"

    "처절하고 놀란, 분명 여자아이의 비명소리가 터져나온다."

    "아르망의 검이 허공을 베었고, 그도 순간 움찔하며 눈을 뜬다."
    scene mainhall
    show adeline surprise at Transform(xalign=0.5, yalign=0.2) with dissolve

    play music "bgm_main.mp3"
    "그리고… 거기. 눈앞에 선 채 놀란 얼굴로 그를 쳐다보는 소녀가 서 있다."

    m "…소녀…?"

    "깜짝 놀란 눈으로 그를 바라보다가, 잠시 정적이 흐른 뒤, 마치 스스로도 민망한 듯 눈을 깜빡인다."

    g "…아, 맞다. 나… 이미 죽었지…"

    show adeline embrassed at Transform(xalign=0.5, yalign=0.2) 
    
    g "후훗… 미안, 네가 그렇게까지 반응할 줄은 몰랐어. 오랜만에 만난 사람이라."
    
    g "무슨일로 왔니?"

    m "나는 벨포르 가문의 아르망 드 벨포르! 이 저택에서 귀신이 사람을 잡아간다는 이야기를 듣고 해결하러 왔다!"

    m "너가 그 귀신인가?"

    show adeline idle at Transform(xalign=0.5, yalign=0.2) 

    g "아니. 나의 이름은 아델린 드 로르망. 이 저택의 주인 로르망 백작의 첫째 딸이야."

    g "그리고 너가 찾는 귀신은 아마도 저택 지하실 깊은 곳에 있는 악령일꺼야."

    m "그런 정보를 왜 나에게 알려주지?"

    show adeline sad at Transform(xalign=0.5, yalign=0.2) 

    g "그 악령은 나를 괴롭히거든......"

    g "그래서 너가 그 악령을 처리해주면 나는 좋은 일이니까."

    m "그런가. 그럼 나는 악령을 처리하러 가겠다."
    
    show adeline idle at Transform(xalign=0.5, yalign=0.2) 

    g "아. 이 집에는 많은 유령이 있어. 멀쩡한 유령은 아마 나뿐일꺼야. 조심해."

    m "헛된 걱정이다!"

    jump mainhall

label mainhall:
    scene mainhall
    # 엔딩 조건 
    if diary_0 and diary_1 and diary_2 and diary_3:
        jump hallway

    # 샹들리에 이벤트
    if chandelier_count == 5:
        $ chandelier_count += 1
        show 샹들리에 at Transform(xalign=0.5, yalign=0.2) 

        menu:
            "샹들리에가 떨어져있다."

            "떨어진 샹들리에를 확인해본다":
                $ safe_password = True
                m "이건.."
                show 단어퍼즐 at Transform(xalign=0.5, yalign=0.2) 
                m "어딘가의 암호처럼 보이는데"
                play audio "item1.ogg"
                "당신은 비밀번호 힌트를 획득 했다."
                hide 단어퍼즐
        hide 샹들리에

    if bgm_not_playing():
        play music "bgm_main.mp3"

    menu:       
        "자, 그럼 이제 어디로 가볼까?"

        "지하실":
            if underground_lock:
                play audio "자물쇠 잠긴소리.mp3"
                m "굴욕적이지만 여긴 지금 나로선 갈수가 없다...."
                jump mainhall
            else:
                if light:
                    stop music
                    jump underground
                else:
                    stop music
                    play audio "old door2.mp3"
                    "끼이익 하고 문이 열린다."
                    scene black with dissolve
                    play audio "돌풍.mp3"
                    "칠흑 같은 어둠속엔 바람 소리만 들리며,"
                    extend "한 치 앞도 보이지 않는다."
                    "어둠 속으로 들어가려 한 그 순간," 
                    play audio "Monster5.ogg"
                    scene 지하실괴물
                    "괴물의 울음소리가 들리며 무언가가 아르망을 덮쳤다"
                    scene black
                    "아르망은 어떠한 힘에 의해 뒤로 밀려 넘어져 들어가지 못하였다."
                    m "크윽... 내가 이런 굴욕을 받다니..."
                    scene mainhall
                    g "지하실은 위험해"  ## 대사 내용 수정 필요
                    m "저 괴물의 정체는 뭐야?"
                    g "나도 모르겠어"
                    jump mainhall
        "방":
            play audio "Open door.mp3"
            jump room

        "식당":
            if dining_room_lock:
                play audio "자물쇠 잠긴소리.mp3"
                m "문이 굳게 잠겨있다. 부술 순 있겠지만 먼지가 많이 날 것 같다. 열쇠를 찾아보자"
                jump mainhall
            else:
                jump dining_room
        "계단":
            play audio "걷는소리 구두.mp3"
            scene black with fade
            jump two_stair

label two_stair:
    scene mainhall2 with fade

    if chandelier_count == 4:
        play audio "샹들리에 박살.mp3"
        m "!!"
        m "뭐지? 1층에서 난 소리 같은데."
        $ chandelier_count += 1
    elif chandelier_count == 5:
        m "아까 들린 소리가 신경쓰인다."
        m "1층으로 내려가보자."
        jump mainhall
    else:
        $ chandelier_count += 1

    if garret_info:
        if garret_to_first:
            menu:
                "어디로 가지?"

                "천장을 살펴본다":
                    jump garret_first

                "서재":
                    jump library

                "안방":
                    if inner_room_lock:
                        play audio "자물쇠 잠긴소리.mp3"
                        m "문이 굳게 잠겨있다. 부술 순 있겠지만 먼지가 많이 날 것 같다. 열쇠를 찾아보자"
                        jump two_stair
                    else:
                        jump inner_room

                "내려간다":
                    play audio "걷는소리 구두.mp3"
                    scene black with fade
                    jump mainhall
        else:            
            menu:
                "어디로 가지?"

                "다락방":
                    "사다리를 조심스레 밟고 올라간다."
                    jump garret

                "서재":
                    jump library

                "안방":
                    if inner_room_lock:
                        play audio "자물쇠 잠긴소리.mp3"
                        m "문이 굳게 잠겨있다. 부술 순 있겠지만 먼지가 많이 날 것 같다. 열쇠를 찾아보자"
                        jump two_stair
                    else:
                        jump inner_room

                "내려간다":
                    play audio "걷는소리 구두.mp3"
                    scene black with fade
                    jump mainhall
    else:
        menu:
            "어디로 가지?"

            "서재":
                jump library

            "안방":
                if inner_room_lock:
                    play audio "자물쇠 잠긴소리.mp3"
                    m "문이 굳게 잠겨있다. 부술 순 있겠지만 먼지가 많이 날 것 같다. 열쇠를 찾아보자"
                    jump two_stair
                else:
                    jump inner_room

            "내려간다":
                play audio "걷는소리 구두.mp3"
                scene black with fade
                jump mainhall

label garret_first:
        $ garret_to_first = False
        "천장을 유심히 보니 뭔가 이상한 곳이 있다"
        menu: 
            "강하게 두드려본다.":
                play audio "문두들기는소리.mp3"
                scene mainhall2 with vpunch
                "천장을 쌔게 쳐보니 계단이 내려온다"
                scene 다락방계단 with dissolve
        m "호오, 이런 곳에 정말 다락방이 있었군."
        jump two_stair

label room:
    stop music
    scene room
    play audio "old door2.mp3"

    if room_first_visit:
        $ room_first_visit = False
        "책상 위에 상자가 놓여있다."
        m "어디보자, 열쇠는..."
        m "이건가...?"
        play audio "뛰는소리 구두.mp3"

        show 열쇠 at Transform(xalign=0.5, yalign=0.2) 
        "바닥에 떨어진 열쇠를 주우려는 순간"

        show 꼬마 유령 at Transform(xalign=1.2, yalign=0.2)
        hide 열쇠 
        show 꼬마 유령 at Transform(xalign=-1.2, yalign=0.2) with move
        "어둠 속 무엇인가, 내 손을 낚아챘다."

        play audio "아이 웃는소리 숏.mp3"
    
        l "히히히, 내꺼야~" 
        m "이놈, 내놔라!"
        l "메롱, 잡을 수 있으면 잡아봐!" 
        m "뭐?! 당장 이리내!"
        jump ghost_chase_game
    else:
        if not diary_0:
            $ diary_0 = True
            m "다시 이 방에 돌아왔다..."
            show 일기 at Transform(xalign=0.5, yalign=0.2)
            "구석에서 아까 못보던 일기장을 발견했다."
            m "음? 일기장..? 누구의 일기장이지?"
            n "유모의 일기장"
            n "오늘 도련님이 태어났다."
            n "백작 부부는 날이 갈수록 도련님에게만 신경을 쏟는다."
            n "아가씨는 자꾸 혼잣말을 하거나, 거울을 오래 바라본다."
            nvl clear
        else:
            m "이제 더 이상 찾을 건 없는 것 같다."
    menu:
        "어디로 갈까?"
        "나간다":
            jump mainhall

label ghost_chase_game:
    $ correct_guesses = 0
    $ wrong_guesses = 0
    $ directions = ["left", "right"]

    scene black
    with fade
    
    "열쇠를 가로챈 유령이 어둠 속으로 사라졌다..."
    "소리를 잘 듣고 위치를 찾아야 해..."

    jump ghost_chase_loop

label ghost_chase_loop:
    $ direction = random.choice(directions)

    if direction == "left":
        $ sound_file = random.choice(left_sounds)
        stop laugh1
        play laugh1 sound_file
        $ renpy.music.set_pan(-1.0, 0.0, channel="laugh1")

    else:
        $ sound_file = random.choice(right_sounds)
        stop laugh2
        play laugh2 sound_file
        $ renpy.music.set_pan(1.0, 0.0, channel="laugh2")

    menu:
        "어디서 소리가 났을까?"
        "왼쪽":
            $ choice = "left"
        "오른쪽":
            $ choice = "right"
    stop laugh1
    stop laugh2

    if choice == direction:
        $ ghost_lines = [
            "여기야~ 여기~!",
            "아슬아슬했는걸~?",
            "으하하! 잡아봐라~!"
            ]
        $ player_lines = [
            "헉... 헉... 거기냐?!",
            "이제 잡을 수 있을 것 같아!",
            "거기 서!! 이번엔 놓치지 않아!"
            ]
        $ correct_guesses += 1
        $ g_line = random.choice(ghost_lines)
        $ p_line = random.choice(player_lines)
        l "[g_line]"
        m "[p_line]"
    else:
        $ ghost_lines = [
            "유령: 엇~ 틀렸어~ ㅋㅋ",
            "유령: 반대쪽이야~ 바보~",
            "유령: 캬하하! 아직 멀었는걸~"
            ]
        $ player_lines = [
            "주인공: 이런... 놓쳤다...",
            "주인공: 다시 집중해야겠어...",
            "주인공: 어디로 간 거지...?"
            ]
        $ wrong_guesses += 1
        $ g_line = random.choice(ghost_lines)
        $ p_line = random.choice(player_lines)
        l "[g_line]"
        m "[p_line]"

    if correct_guesses >= 5:
        jump ghost_chase_success
    elif wrong_guesses >= 2:
        jump ghost_chase_fail
    else:
        jump ghost_chase_loop

label ghost_chase_success:
    scene room
    show 꼬마 유령 at Transform(xalign=0.5, yalign=0.2) with dissolve
    l "즐거웠어! 자, 여기 가져가~ 꺄르륵!"
    show 열쇠 at Transform(xalign=0.5, yalign=0.2) 
    play audio "item1.ogg"    
    "당신은 열쇠를 되찾았다."
    hide 열쇠
    m "헉... 헉... 힘들어......"
    hide 꼬마 유령 with dissolve
    $ dining_room_lock = False
    m "이건.. 식당 열쇠인가?"
    m "한번 확인해봐야겠군."

    menu:
        "어디로 갈까?"
        
        "나간다":
            scene mainhall
            g "어때? 숨바꼭질은 재밌었어?"
            m "장난해? 웬 꼬마 덕분에 힘들어 죽기 직전이야"
            g "그럼 죽어."
            jump mainhall

label ghost_chase_fail:
    l2 "너.. 제대로 안하지?"
    l2 "..재미 없어졌어"
    play audio "여자비명2.mp3"
    scene surprise_attack2
    "..!!!"
    jump ghost_chase_retry

label ghost_chase_retry:
    scene black with dissolve
    $ correct_guesses = 0
    $ wrong_guesses = 0
    m "크윽.. 잠시 정신을 잃었었나 봐..."
    m "하지만 열쇠는 반드시 찾아야 해..."

    "유령의 숨소리가 다시 들리기 시작했다..."

    jump ghost_chase_loop

label dining_room:
    if dining_room_first:
        $ dining_room_first = False
        play audio "열쇠로 문따는 소리.mp3"
        "방에서 얻은 열쇠로 문을 연다"

        play audio "철문여는소리.mp3"
        "묵직한 소리와 함께 문이 열린다"

        m "식당 문 열쇠였군"

        scene 식당 with fade

        "어둡고 넓은 식당 내부, 오래된 식탁과 의자들이 줄지어 놓여있다."

        m "(천천히 안으로 걸으며) 기묘하군... 의자가 모두 붙어 있는데, 저 하나만 왜 저렇게 떨어져 있지?"
    
    scene 식당

    menu:
        "어디를 찾아볼까"

        "선반을 뒤져본다":
            if underground_lock:
                play audio "서랍소리1.mp3"
                $ underground_lock = False
                "서랍 안에 무언가 있다."
                show 열쇠 at Transform(xalign=0.5, yalign=0.2) 
                m "이건.. 지하실 문 열쇠인가?"
                play audio "item1.ogg"
                "당신은 지하실 열쇠를 획득 했다."
                jump dining_room
            else:
                "여기엔 더 이상 볼 것이 없다."
                jump dining_room
            
        "식기서랍을 뒤져본다":
            if diary_1:
                "여기엔 더 이상 볼 것이 없다."
                jump dining_room
            else:
                $ diary_1 = True
                play audio "서랍소리1.mp3"
                "식기서랍 안에 무언가 있다."
                show 일기 at Transform(xalign=0.5, yalign=0.2) 
                "이건 일기인가?"

                n "주방장의 일기장"

                n "오늘 아가씨는 혼자 밥을 먹는다."

                n "백작님은 회의로 바쁘시고 백작부인은 아들만 돌보신다."

                n "아가씨가 웃는걸 본적이 언제였던가...."

                nvl clear
                    
                play audio "item1.ogg"
                "당신은 주방장의 일기를 획득 했다."
                jump dining_room

        "나간다":
            jump mainhall 

label underground:
    
    if bgm_not_playing2():
        play music "bgm_piano.mp3"

    if underground_first:
        $ underground_first = False
        scene black with dissolve

        play audio "돌풍.mp3"
        "지하실로 들어가려 하자 또다시 바람이 불어온다."

        play audio "등불 점화.mp3"
        scene 지하실 with dissolve
        "바람을 등지고 등불에 불을 켜고 앞으로 나아가자 바람이 멈췄다."

        m "이 불빛만이... 어둠 속 길을 비춰주리라...."

        play audio "걷는소리 구두.mp3"

        "등불을 켠 채 지하실 안으로 들어서자, 발소리가 메아리치며 울려 퍼진다."

        "차가운 기운이 바닥에서부터 올라오는 듯, 그의 몸을 감싼다."

        m "나의 발걸음 소리마저... 이곳의 침묵을 깨트리는군...."

        "무언가 발에 걸린다"

        m "뭐지 이건..?"

        show 피일기 at Transform(xalign=0.5, yalign=0.2) 

        "낡고 피 묻은 일기장이다."

        play audio "등불 점화2.mp3"
        
        "등불에 비춰 읽어보자"

        hide 피일기

        window show
        play audio "책넘김.mp3"
        n "18xx년 4월 3일"
        n "나에게 임무가 내려왔다."
        n "저택이 유령에 저주받았다는 이야기였다."
        n "나는 퇴마를 위해 성수를 준비했다."
        nvl clear

        play audio "책넘김.mp3"
        n "18xx년 4월 6일"
        n "나는 오늘 유령을 퇴치하러 왔다."
        n "그러나 실패했다."
        n "나는 유령의 기습을 받고, 배에 구멍이 뚫린 채로 이 지하실로 도망쳐왔다."
        n "다행히 중요한 부위는 비껴나가 치료가 가능할 것 같다."
        n "나는 여기서 치료를 하고 다시 유령을 퇴치하기로 했다."
        nvl clear

        play audio "책넘김.mp3"
        n "18xx년 4월 10일"
        n "상처가 회복되지 않는다."
        n "아마 유령의 저주 탓일 것이다."
        n "지하실에는 누군가의 생활 흔적이 있다…"
        n "혹시 그녀의 공간이었던 걸까."
        nvl clear

        play audio "책넘김.mp3"
        n "18xx년 4월 11일"
        n "\"그녀는 단순한 유령이 아니다.\""
        n "\"‘감정’이, ‘고독’이 실체가 되어 움직이고 있다.\""
        n "\"누구든… 이 일기를 본다면… 제발… 그녀를…"
        nvl clear
        window hide
        pause(1.5)
        a "……감정이 실체가 된 유령? 이건..."
        scene black with fade
        show adeline idle with dissolve
        "아델린을 말하는 건가…"
        hide adeline idle with dissolve

        "그 순간, 지하의 어둠 속에서 희미한 숨소리가 들려온다."
        "조심스레 안으로 들어서자, 고요한 어둠 속에서 짐승의 울음소리가 울려퍼진다."

        m "……크르르르릉……"

        "거대한 그림자. 사람보다 크고, 형체가 일그러진 괴물이 서서히 모습을 드러낸다."
        "괴물이 포효하며 전속력으로 달려든다."

        "아르망은 옆으로 구르며 칼을 휘둘러 괴물의 어깨를 긋는다."
        "비명과 함께 피가 튀고, 괴물이 반격하듯 발톱을 휘두른다."

        m "키에에에에엑!"

        a "악령이든 짐승이든…"
        a "너 따위에게 무너질 내가 아니야!!"

        "괴물의 발톱에 어깨가 긁혀 피가 흐르지만, 그는 몸을 낮추며 괴물의 밑을 파고든다."
        "마지막 일격—칼을 힘껏 들어 괴물의 심장을 찔러 꽂는다!"

        a "사라져라!!!"

        "칼끝이 박히며, 괴물의 몸이 뒤틀린다."
        "괴성, 그리고 한 줄기 연기와 함께 괴물의 육체가 무너지기 시작한다."

        m "외....로.....워...."

        "괴물의 형체가 녹아 사라진다. 아르망은 거친 숨을 쉬며 바닥에 주저앉는다."
        "검 끝에 묻은 피가 천천히 사라지고, 주위는 다시 고요해진다."

        "지하실 안쪽 끝, 낡은 옷장과 책상, 침대가 놓여있다. 누군가가 생활했던 흔적이 있다."   

    scene 지하실
    menu:        
        "주변을 뒤져볼까?":
            if inner_room_lock:
                $ inner_room_lock = False
                m "이건.."
                show 열쇠 at Transform(xalign=0.5, yalign=0.2) 
                m "안방 열쇠인 것 같군."
                play audio "item1.ogg"
                "당신은 안방열쇠를 획득 했다."
                hide 열쇠
                jump underground
            else:                
                "아무것도 없다."
                jump underground
        "나간다":
            jump mainhall    

label library:
    if library_first:
        $ library_first = False
        play audio "old door2.mp3"
        "문고리를 당기니 서재의 문이 천천히 열렸다."
        play audio "돌풍.mp3"
        "문을 열자 바람이 불며 먼지가 날린다"
        scene 서재 with dissolve
        m "음... 서재가 많이 크군"

    scene 서재

    menu:
        "어디를 찾아볼까."

        "책장의 책을 살펴본다":
            if garret_info == False:
                $ garret_info = True
                play audio "책 꺼내는 소리1.mp3"
                "당신은 책장의 책을 꺼냈다."
                play audio "책넘김.mp3"
                m "이건.."
                show 메모 at Transform(xalign=0.5, yalign=0.2) 
                "책을 넘기는 도중 메모를 발견했다."
                n "다락방 구석의 작은 창문이 다시 열리지 않습니다."
                n "지난번 비로 나무틀이 휘어진 듯하니, 다음 수리 일정에 포함해야 할 듯합니다."
                nvl clear

                m "호오, 이 집에 다락방이 있었군."
                m "다시 확인해봐야겠어."
                play audio "item1.ogg"
                "당신은 다락방에 관한 정보를 획득 했다."
                jump library
            else:
                "여기엔 더 이상 볼 것이 없다."
                jump library
            
        "책장 위를 살펴본다":
            if diary_2 == False:
                $ diary_2 = True
                play audio "책 꺼내는 소리2.mp3"
                "책장 위를 살펴보니 그곳엔 책이 1권 있었다."
                show 일기 at Transform(xalign=0.5, yalign=0.2) 
                m "이건 일기장인가?"

                n "집사의 일기장"

                n "백작님은 도련님에게만 관심을 갖지고 계신다."

                n "업무가 많아 요즘 아가씨를 뵙지 못하였다."

                n "아가씨를 마지막으로 본게 언제 였더라...."

                nvl clear
                play audio "item1.ogg"
                "당신은 집사의 일기를 획득 했다."
                jump library
            else:
                "여기엔 더 이상 볼 것이 없다."
                jump library

        "서랍을 뒤져본다":
            if safe_info == False:
                $ safe_info = True
                play audio "서랍소리2.mp3"
                show 메모 at Transform(xalign=0.5, yalign=0.2) 
                "서랍 안에 메모가 있다."
                n "주인님의 건망증이 점점 심해지고 있습니다."
                n "안방의 금고 비밀번호를 계속 까먹으셔서 따로 메모 해둬야겠습니다."
                m "안방에 금고가 있었군."
                m "다시 한번 찾아봐야겠어."
                nvl clear

                play audio "item1.ogg"
                "당신은 안방 금고에 관한 정보를 획득 했다."
                jump library
            else:
                "여기엔 더 이상 볼 것이 없다."
                jump library

        "나간다":
            jump two_stair

label inner_room:

    stop music

    if inner_room_first:
        $ inner_room_first = False
        play audio "old door3.mp3"
        "안방의 문을 열어 들어갔다."
        scene 안방 with dissolve
        m "음... 여기가 안방인가."
    
    scene 안방

    menu:
        "초상화를 살펴본다.":
            if photo_count == 0:
                $ photo_count += 1
                scene 초상화 with dissolve
                m "흠, 이상하게 생긴 초상화군"
                jump inner_room
            elif photo_count == 1:
                $ photo_count += 1
                scene 초상화_눈 with dissolve
                m "음? 저 초상화 원래 눈을 뜨고 있었나?"
                jump inner_room
            else:
                play audio "스크림1.mp3"
                scene 초상화_공포 
                m "으악!"
                "아르망은 정신을 잃었다."
                scene mainhall
                g "정신이 좀 들어? 너 갑자기 기절했더라고."  ## 대사 수정 필요?
                m "헉..헉.. 방금 그건 뭐였지?"
                g "뭘 봤길래 호들갑이야?"
                m "안방에 걸려있는 초상화말이야!"
                g "응? 우리 집엔 안방에는 초상화가 없는데?"
                m "뭐..?"
                g "잘못본거겠지 안좋은 꿈이라도 꾼거야?"
                m "아니야 그럴리가 없어.. 다시 확인해보자."
                jump mainhall

        "주변을 살펴본다.":
            if safe_info:
                if safe_password:
                    scene 안방 with fade #안방 이미지
                    "당신은 방 구석에서 잠긴 금고를 발견했다"
                    show 금고 at Transform(xalign=0.5, yalign=0.2)
                    m "아까 얻은 종이에 뭔가 단서가 있을 것 같아..."
                    show 단어퍼즐 at Transform(xalign=0.5, yalign=0.2) with dissolve
                    m "단어를 찾아 입력해보자."
                    $ correct_answer = "adeline"       
                    jump input_loop
                else:
                    "금고가 있지만 비밀번호를 모르겠다."
                    jump inner_room
            else:
                "주변에 아무것도 안보인다."
                jump inner_room
        "나간다" :
            jump two_stair

label input_loop:
    $ player_input = renpy.input("숨겨진 단어는 무엇일까?").strip().lower()

    if player_input == correct_answer:
        show 단어퍼즐답 at Transform(xalign=0.5, yalign=0.2) with dissolve
        "끼익... 금고가 열리는 소리가 들린다."
        "당신은 안방의 금고에서 네번째 일기장을 찾았다."
        hide 단어퍼즐
        hide 단어퍼즐답
        $ diary_3 = True
        jump diary4
    else:
        m "그건 아닌 것 같아... 다시 생각해보자."
        jump input_loop

label diary4:

    play music "bgm_반전.mp3"

    n "금고 -일기장"

    n "18xx년 4월 6일"

    n "오늘, 저택에 낯선 이가 찾아왔다."

    n "검은 수도복을 입고, 커다란 성경을 들고,"

    n "십자가를 흔들며 중얼거리는 남자."

    n "사람들은 그를 ‘신부님’이라 불렀다."

    n "처음엔, 그가 나를 구하러 온 줄 알았다."

    n "그는 어쩌면… 내 외로움을 이해해줄지도 모른다고 생각했다."

    n "하지만 그는 나를 구원하러 온 게 아니었다."

    n "그의 입은 ‘악령 퇴치’만을 말했고,"

    n "그의 눈엔… 내가 사람이 아니었다."

    n "그래서… 나는 그를 멈췄다."

    n "그의 목은 너무 가늘었고, 심장은 너무 여렸어."

    n ""

    n "18xx년 9월 18일"

    n "신부가 죽은 그날 이후, 사람들은 더 이상 이 집에 오지 않게 되었다."

    n "그 신부가 죽기 전 집에 무슨 짓을 한 게 분명하다."

    n "나는 매일 문 앞을 지켰고, 매일 누구도 오지 않았다."

    n "가끔 그 신부의 얼굴이 떠오른다."

    n "그때 그냥… 잠시만 참았더라면…"

    n ""

    n "19xx년 1월 6일"

    n "웃는 연습을 했다."

    n "말하는 연습도 했다."

    n "혹시라도 누군가 오면… 반갑게 맞이하고 싶었으니까."

    n "하지만 오지 않았다."

    n "거울에 비친 내 얼굴이 낯설다."

    n "나는 아직 웃고 있는 걸까?"

    n "아니면 울고 있는 걸까?"

    n ""

    n "19xx년 4월 6일"

    n "오늘, 누군가 왔다."

    n "거창하게 명예니 뭐니 외치더니,"

    n "살짝 놀래켜주니 놀라서 마구잡이로 칼을 휘둘렀다."

    n "정말이지. 웃겨서 죽을 뻔했잖아."

    n "아, 난 이미 죽었지. 참."

    n "정말 이상한 사람이다."

    n "시끄럽고 허세도 많고… 좀 무례하고…"

    n "그런데 묘하게, 따뜻했다."

    n "정말 오랜만에, 무언가가 내 안에서 움직이는 느낌이 들었다."

    n ""

    n "생각해봤다."

    n "이번엔… 놓치지 않을 거야."

    n "어차피 이 집은 나 혼자 쓰기엔 너무 넓고, 너무 외로우니까."

    n "그러니, 그 남자를 여기에 남겨버리자."

    n "영원히. 나와 함께."

    nvl clear

    jump inner_room

label garret:

    scene 다락방 with dissolve

    stop music
    stop audio

    if garret_first:
        $ garret_first = False
        "갑자기 안쪽에서 오르골 소리가 들려온다."
    
        show 오르골 at Transform(xalign=0.5, yalign=0.2)
        m ".....날 환영하는 소린가?"
    
        "후후 잘 들어봐"

        "집중해서 잘 들어보자."

        play audio "기믹_오르골_단어1.mp3"

        window hide

        $ renpy.pause(10.0, hard=True)

        m "첫 번째 노래군"

        play audio "기믹_오르골_단어2.mp3"

        window hide

        $ renpy.pause(10.0, hard=True)

        m "두 번째 노래군"

        play audio "기믹_오르골_단어3.mp3"

        window hide

        $ renpy.pause(10.0, hard=True)

        m "이게 끝인가"

        s "어때? 노래는?"

        m "음.. 노래를 듣다보니"

        $ correct_answer = "정화수"

        jump garret_input_loop

    menu:
        "어디로 갈까?"

        "나간다":
            jump two_stair

label garret_input_loop:
    $ player_input = renpy.input("숨겨진 단어는 무엇일까?").strip().lower()

    if player_input == correct_answer:
        m "정화수."
        m "정화수라는 단어가 생각나던데?"
        s "너 정말 열심히 들었구나?"
        $ light = True
        show 등불 at Transform(xalign=0.5, yalign=0.2)
        "자 이건 선물이야."
        "그렇게 귀신은 사라졌다."
        jump garret
    else:
        s "너.. 제대로 안들었구나?"
        jump garret_input_loop

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
    scene bg dream with dissolve
       
    m "여긴... 대체...?"
    g "어때, 이 꽃? 정말 예쁘지 않아?"
    g "어렸을 땐 부모님이 날 이 꽃밭에 데려다 주셨어. 햇살 가득한 날, 엄마가 내 머리에 꽃을 꽂아주며 웃으셨지."
    g "그때는 세상이 다 따뜻하고, 모든 게 가능할 것 같았어."
    g "하지만 남동생이 태어난 이후로, 모든 것이 끝나버렸어."
    g "부모님의 관심은 전부 남동생에게로 가버렸어."
    g "그 후로 난 늘 외로웠고, 차가운 현실 속에 홀로 남겨졌어."

    m "아델린..."

    g "이 어둠 속, 이 쓸쓸한 곳에 너가 와준 건 마치 한 줄기 빛 같았어."
    g "처음엔 네 시끄럽고 거칠게 들리는 말투, 허세 섞인 태도에 나도 모르게 마음을 닫으려 했어."
    g "그런데, 네가 점차 보여준 항상 당당한 모습, 그리고 눈빛 속에 숨겨진 고독을 알게 된 후, 내 심장은 미친 듯이 뛰기 시작했어."
    g "나와 함께 하자. 영원히.....!"

    menu:
        "해피엔딩이다":
            jump happy_ending
        "배드엔딩이다":
            jump bad_ending

label happy_ending:

    play music "bgm_감동.mp3"

    "성수를 든다"

    g "어....어째서...?"
    g "넌....넌 날 이해한 게 아니였어....?"

    m "아델린, 넌 지금도 과거에 사로잡혀 있어."
    m "세상을 외면한 채, 여전히 그때에 머물고 있잖아."
    m "너는 혼자였던 적이 없어."

    g "거짓말이야! 아빠도, 엄마도... "
    g "항상 동생만 바라보고, 나에겐 차갑기만 했어!"

    m "그래, 백작부부는 그랬겠지."
    m "하지만... 다른 사람들은?"

    g "...다른 사람들?"

    m "그래, 집사. 유모. 주방장."
    m "그들은 너에게 어떤 존재였지?"

    g "집사... 유모.... 주방장...."

    m "그들은 네 곁에 항상 있었어."
    m "널 혼자 두지 않기 위해, 조용히, 묵묵히 곁을 지켰지."
    m "하지만 넌 백작부부의 시선에만 갇혀,"
    m "그들의 마음은 보지 못했던 거야."

    g "......유모.....집사....."

    m "자... 이 일기들을 봐."
    m "너를 걱정하고, 너를 아끼던 사람들의 마음이 여기 담겨 있어."

    "(아델린, 일기장을 끌어안고 흐느낀다)"

    g "아르망......"
    g "그 성수로...... 날....... 해방시켜줘...."
    g "나도.....이제.....그들의 곁으로 가고 싶어......"

    m "......그래."

    "성수를 뿌린 뒤, 아르망은 조용히 칼을 들어 올린다."
    "칼에 베인 아델린은 평온한 미소를 지으며 서서히 사라진다."

    "그 후, 아르망은 일기와 일기장을 모아 정원나무 밑에 묻고,"
    "자신의 칼을 꽂아 작은 무덤을 만들어 준 뒤 저택을 떠난다."

    m "……안녕, 아델린."
    m "나도...... 너처럼 나아가야겠지."

label bad_ending:
    
    "성수를 든다"

    g "그렇구나.....너도...."
    g "너도.....날 버렸구나!"

    m "미안하다....아델린!"
    m "살아있는 사람이 어찌 죽은 사람을 위해 죽을 수 있겠느냐!"
    m "나 벨포르 가의 아르망! 이 이름에 맹세하노니,"
    m "내가 이 저택에 깃든 어둠을 베어 부정하리!"

    g "너도 다른 사람이랑 다를 바가 없는 이기적인 인간이였어!!!"
    g "꺄아아아악"

    m "이기적인 인간이라......헛소리군. 나는 기사로서의 의무를 다한 것이다"

    "칼을 다시 허리에 차고 정문으로 아르망은 나간다"
    "그 후 아르망은 자신이 대저택의 유령을 베어 해치웠으며"
    "앞으로 그 대저택에서 실종 사건이 없을 것이라고 외치고 다닌다"
    "마을 사람은 그를 보고 실성한 사람 취급했으며"
    "아르망은 자신을 이해해주는 사람도 없이 과거에 집착하며 살아간다"

    "-END-"