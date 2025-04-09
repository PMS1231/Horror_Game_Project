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
                text "호감도{space=15}[p_bar[0]]" size 16 color "#FFFFFF"
                bar:
                    value AnimatedValue(p_bar[0], 100, delay=1.0)
                    range 100
                    style "fixed_bar"

                text " " size 3

                # text "호감도{space=15}[p_bar[1]]" size 16 color "#FFFFFF"
                # bar:
                #     value AnimatedValue(p_bar[1], 100, delay=1.0)
                #     range 100
                #     xalign 0.0
                #     style "fixed_bar"
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
    image bg hallway1_base = "images/bg/hallway1_base.png"
    image bg hallway1_diff1 = "images/bg/hallway1_diff1.png"
    image bg hallway1_diff2 = "images/bg/hallway1_diff2.png"
    image bg hallway1_diff3 = "images/bg/hallway1_diff3.png"

    # 복도 2 이미지
    image bg hallway2_base = "images/bg/hallway2_base.png"
    image bg hallway2_diff1 = "images/bg/hallway2_diff1.png"
    image bg hallway2_diff2 = "images/bg/hallway2_diff2.png"
    image bg hallway2_diff3 = "images/bg/hallway2_diff3.png"

#특수복도 이미지 랜덤 생성 모듈    
init python:
    import random

    hallway_data = {
        1: {
            "correct": "hallway1_base.png",
            "options": ["hallway1_base.png", "hallway1_diff1.png", "hallway1_diff2.png", "hallway1_diff3.png"]
        },
        2: {
            "correct": "hallway2_base.png",
            "options": ["hallway2_base.png", "hallway2_diff1.png", "hallway2_diff2.png", "hallway2_diff3.png"]
        }
    }

    progress = 1
    clears = 0
    current_bg = "hallway1_base.png"

#캐릭터 이미지 변경
init:
    # 아델린
    image adeline_surprise = "images/chr/adeline_surprise.png"
    image adeline = "images/chr/adeline_idle.png"
    image adeline 폭소 = "images/chr/adeline_폭소.png"
    image 마주 = "images/chr/마차 주인.png"
    image 마주생각 = "images/chr/마차 주인 생각.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define h = Character("마부", callback=type_sound2, font="tway_sky.ttf", what_font="tway_fly.ttf")
define m = Character('아르망', color="#044604", font="tway_sky.ttf", what_font="tway_fly.ttf", callback=type_sound)
define g = Character("아델린", color="#bdaa00", callback=type_sound2, font="tway_sky.ttf", what_font="tway_air.ttf")
define n = nvl_narrator #n을 나레이터 캐릭터로 설정
define l = Character('꼬마 유령', color="#879c0d", font="tway_sky.ttf", what_font="tway_fly.ttf")
define l2 = Character('꼬마 유령', color="#d4840b", font="tway_sky.ttf", what_font="tway_fly.ttf")
define G = Character('???')
define s = Character("오르골 유령",)
define M = Character("괴물")

default p_bar = [50, 0]
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
default holy_water = False
default orgel_try = True
default room_event = False
default orgel_adeline = True
default underground_event = True
default inner_room_event = True
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
    
    h "도착이오"
    h "이 곳이 바로 로르망 백작의 저택이오"
    m "......"
    m "이 곳인가..."
    m "{alpha=*0.5}사람들이 계속 사라진다는 대저택...{/alpha}"
    m "{alpha=*0.5}이곳엔 대체 어떤 진실이 숨겨져 있는가...{/alpha}"
   
    m "{alpha=*0.5}두려움으로부터 진실을 외면하는 것은, 기사로서 가장 비겁한 일{/alpha}"
    m "벨포르 가의 이름으로 맹세하노니"
    scene 저택 with vpunch
    play audio "쿵.mp3"
    m "{size=+10}내가 이 저택에 깃든 모든 어둠을 밝혀내리라!{/size}"
    
    show 마주생각 at Transform(xalign=0.5, yalign=0.2) 
    h "음...?"
    play audio "궁금.mp3"
    h "벨포르 가문이라고 했소?"
    h "벨포르라… 오랜만에 듣는 이름이로군"
    h "허허, 그 가문도 한때는 명망이 높았지"
    h "하지만 요즘은 그 이름을 아는 이조차 많지 않겠소만"
    
    m "저택 근처에서는 유령이 나타나서 사람을 잡아간다고 들었소"
    m "그대는 혹시 이 이야기에 대해 알고있는가?"
    hide 마주생각
    show 마주 at Transform(xalign=0.5, yalign=0.2) 
    h "하하 그게 언제적 얘기요?"
    h "유령이니 실종이니, 다 뻔한 헛소문 아니오"
    h "물론 이 근방에 사는 사람들이라면 모두 알고있는 내용이네만"
    h "이제는 다들 웃어넘기는 옛 소문일뿐이오"
    h "유령보다는 세금이 더 무섭지"    

    h "요즘 세상에 기사도니 명예니 따지는 양반은 아마 선생밖에 없을거요."
    h "하하하"
    
    hide 마주 with dissolve

    "마차 주인은 돌아갔다."
    
    scene 자물쇠 
    "정문은 무겁게 닫혀 있고 녹슨 자물쇠로 굳게 잠겨 있다."

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
                
                play audio "자물쇠 부숨.mp3"
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
    "또각… 또각… 구두굽 소리가 허공에 메아리친다."

    play music "여자 콧노래.mp3"
    
    m "이 소리는 뭐지...?"
    m "......"
    m "역시, 단순한 헛소문은 아니였던 모양이로군"

    "2층 난간 위, 어둠 속 소녀가 부르는 콧노래가 울려퍼진다."

    m "누구냐! 지금 당장 모습을 드러내라!"
    
    stop music 
    play audio "스크림1.mp3"

    scene surprise_attack

    "……!!"
    play audio "칼소리.mp3"
    "순간, 아르망은 비명을 지르며 칼을 휘두른다."

    scene black
    play audio "칼 휘두름.mp3"
    m "사라져라아앗!! 벨포르의 이름으로!! 이 망령아!!"

    "그 순간—"
    
    play audio "여자비명.mp3"
    g "꺄아아아악!!!!!"

    "처절하고 놀란, 분명 여자아이의 비명소리가 터져나온다."

    "아르망의 검은 허공을 베었고, 그도 순간 움찔하며 눈을 뜬다."
    
    scene mainhall
    show adeline surprise at Transform(xalign=0.5, yalign=0.2) with dissolve

    play music "bgm_main.mp3"
    "그리고… 거기. 눈앞에 선 채 놀란 얼굴로 그를 쳐다보는 소녀가 서 있다."

    m "…소녀…?"
    
    "깜짝 놀란 눈으로 그를 바라보다가, 잠시 정적이 흐른 뒤, 마치 스스로도 민망한 듯 눈을 깜빡인다."
    show adeline embrassed at Transform(xalign=0.5, yalign=0.2) 
    g "…아, 맞다. 나… 이미 죽었지…"
    
    g "후훗… 미안, 네가 그렇게까지 반응할 줄은 몰랐어. 오랜만에 만난 사람이라."
    
    play audio"아델린 웃음소리.mp3"

    g "무슨일로 왔니?"

    menu:
        "내 이름은 아르망 드 벨포르": 
            m "내 이름은 아르망 드 벨포르!"
            m "벨포르 가문의 기사다!"
            m "이 저택의 불길한 소문을 듣고 해결하러 왔다"
 
        "어째서 그런걸 묻는거지..?":
            m "어째서 그런걸 묻는거지..?"
            m "네 정체부터 먼저 밝혀라!"
            m "네가 소문의 악령인가?"     
     
    play audio"아델린 웃음소리.mp3"
    g "나의 이름은 아델린. 이 저택의 관리자야!."
    m "너가 소문의 악령인가?"

    show adeline idle at Transform(xalign=0.5, yalign=0.2) 

    g "아니. 로르망 백작가의 하녀지!."
    
    g "너가 찾는 유령은 아마도 저택 깊은 곳에 있는 악령일꺼야."

    m "그런 정보를 왜 나에게 알려주지?"

    show adeline sad at Transform(xalign=0.5, yalign=0.2) 
    
    g "너가 그 악령을 처리해준다면..." 
    g "나에게도 좋은 일이니까..."
    play audio "우는소리 숏.mp3"
    g "그 악령은... 나를 괴롭히거든..."

    m "그런가..." 
    m "그렇다면 나는 악령을 처리하러 가겠다."
    
    show adeline idle at Transform(xalign=0.5, yalign=0.2) 

    g "후훗..." 
    g "이 집에는 많은 유령들이 있어." 
    g "그들은 너를 괴롭히고 해치려 할거야. 괜찮겠어?"

    m "헛된 걱정이다!"
    play audio "아델린 웃음소리.mp3"
    hide adeline idle with dissolve
    g "{size=+40}{alpha=*0.5}조심해{/alpha}{/size}"

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
        "샹들리에가 떨어져있다."
        hide 샹들리에
        show adeline surprise at Transform(xalign=0.5, yalign=0.2)
        g "아, 깜짝 놀랐네!"

        menu:
            "아델린의 상태를 확인한다.":
                m "어디 다친데는 없나?"
                show adeline embrassed at Transform(xalign=0.5, yalign=0.2)
                g "아니 다치고 자시고 난 이미 죽었다니까.."
                m "{size=+10}그럼에도!! {/size}"
                extend "{size=+10}확인하는 것이!! {/size}"
                m "{size=+20}기사도다!!{/size}"
                g "하하하.."
                show screen stat_overlay with dissolve
                $ p_bar[0] += 20
                play audio "호감도 상승.mp3"
                "아델린의 호감도가 20 상승했다."
                hide adeline embrassed with dissolve
                hide screen stat_overlay with dissolve
            "샹들리에를 바라본다.":
                hide adeline surprise
                show 샹들리에 at Transform(xalign=0.5, yalign=0.2)
                m "뭐야, 샹들리에가 떨어진거였나."             
        show 샹들리에 at Transform(xalign=0.5, yalign=0.2)   

        menu:
            "떨어진 샹들리에를 확인해본다":
                $ safe_password = True
                m "이건.."
                show 단어퍼즐 at Transform(xalign=0.5, yalign=0.2) 
                "정체불명의 종이를 주웠다."
                m "어딘가의 암호처럼 보이는데"
                play audio "item1.ogg"
                "당신은 비밀번호 힌트를 획득 했다."
                hide 단어퍼즐
        hide 샹들리에

    if bgm_not_playing():
        play music "bgm_main.mp3"

    # 아델린 호감도 이벤트
    if orgel_try == False:
        if garret_first == False:
            if orgel_adeline:
                $ orgel_adeline = False
                show adeline 무표정 at Transform(xalign=0.5, yalign=0.2) with dissolve
                g "2층에서 오르골 소리 같은게 들리던데.."
                g "무슨 일 있었어?"
                
                menu:
                    "오르골에 대해 얘기한다.":
                        m "아, 다락방에 손님이 있더군."
                        m "나에게 아름다운 오르골 소리를 들려줬다네"
                        g "..."
                        show adeline 웃음 at Transform(xalign=0.5, yalign=0.2) with dissolve
                        g "잘됐네, 그거."
                        show screen stat_overlay with dissolve
                        $ p_bar[0] += 10
                        play audio "호감도 상승.mp3"
                        "아델린의 호감도가 10 상승했다."
                        hide adeline embrassed with dissolve
                        hide screen stat_overlay with dissolve
                        jump mainhall
                    "유령에 대해 얘기한다.":
                        m "아, 소름끼치는 유령이 있더군."
                        m "자네도 위험할 수 있으니 조심하게."
                        g "..."
                        show adeline 비웃음 at Transform(xalign=0.5, yalign=0.2) with dissolve
                        g "알겠어, 조심할게."
                        show screen stat_overlay with dissolve
                        $ p_bar[0] -= 10
                        play audio "호감도 하락.mp3"
                        "아델린의 호감도가 10 하락했다."
                        hide adeline embrassed with dissolve
                        hide screen stat_overlay with dissolve
                        jump mainhall
                        
    menu:       
        "자, 그럼 이제 어디로 가볼까?"

        "지하실":
            if underground_lock:
                play audio "자물쇠 잠긴소리.mp3"
                m "문이 단단히 잠겨있어... 여긴 지금 갈수가 없다...."
                jump mainhall
            else:
                if light:
                    stop music
                    jump underground
                else:
                    if underground_event:
                        $ underground_event = False
                        stop music
                        play audio "old door2.mp3"
                        "끼이익 하고 문이 열린다."
                        scene black with dissolve
                        play audio "돌풍.mp3"
                        "칠흑 같은 어둠속엔 바람 소리만 들리며,"
                        extend "한 치 앞도 보이지 않는다."
                        "어둠 속으로 들어가려한 그 순간," 
                        play audio "Monster5.ogg"
                        scene 지하실괴물
                        "괴물의 울음소리가 들리며 무언가가 아르망을 덮쳤다"
                        scene black
                        "아르망은 어떠한 힘에 의해 뒤로 밀려 넘어져 들어가지 못하였다."
                        m "크윽... 내가 이런 굴욕을 받다니..."
                        scene mainhall
                        show adeline surprise at Transform(xalign=0.5, yalign=0.2) with hpunch
                        g "괜찮아, 너??"
                        m "저 괴물의 정체는 뭐야?"
                        show adeline 의문 at Transform(xalign=0.5, yalign=0.2)
                        g "나도 잘 모르겠어, 지하에는 갈 일이 없으니까"
                        show adeline idle at Transform(xalign=0.5, yalign=0.2)
                        g "위험하니까 지하에는 가지마."
                        g "나처럼 되고 싶은게 아니라면 "
                        extend "알겠지?"
                        menu:
                            "기사로서 그럴 수 없다.":
                                m "위험하다고?"
                                m "{size=+20}그렇기에 가야하는 것이다!! {/size}"
                                m "기사로서, 사람들을 겁주는 괴물을 보고 어찌 못본 척 하겠는가!"
                                show adeline 황당 at Transform(xalign=0.5, yalign=0.2)
                                g "아니.. 사람이고 자시고 여긴 유령 밖에 없는데.."
                                m "그럼에도 타협하지 않는 것이 기사도다!!"
                                show adeline embrassed at Transform(xalign=0.5, yalign=0.2)
                                g "하하.."
                                g "살아 생전 받아본 적 없는 걱정을 죽어서 받을 줄은 몰랐는데.."
                                show screen stat_overlay with dissolve
                                $ p_bar[0] += 10
                                play audio "호감도 상승.mp3"
                                "아델린의 호감도가 10 상승했다."
                            "뭐지? 날 무시하나?":
                                m "{size=+20}이놈!! {/size}"
                                extend "지금 벨포르가의 명예로운 기사."
                                m "{size=+20}아르망 드 벨포르를 무시하는거냐!!!!{/size}"
                                show adeline 황당 at Transform(xalign=0.5, yalign=0.2)
                                g "뭐??"
                                g "무슨 소릴 하는거야?"
                                show adeline 삐짐 at Transform(xalign=0.5, yalign=0.2)
                                g "하아.."
                                g "기껏 걱정해줬더니..."
                                show screen stat_overlay with dissolve
                                $ p_bar[0] -= 10
                                play audio "호감도 하락.mp3"
                                "아델린의 호감도가 10 하락했다."
                        m "{alpha=*0.5}우선은 지하를 밝힐 불이 필요하겠군.{/alpha}"
                        hide screen stat_overlay with dissolve
                        jump mainhall
                    else:
                        play audio "Monster5.ogg"
                        m "흠 다른 방법을 찾아봐야겠군."
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
    if bgm_not_playing():
        play music "bgm_main.mp3"
    scene mainhall2 with fade

    if chandelier_count == 4:
        play audio "샹들리에 박살.mp3"
        m "!!"
        m "뭐지? 1층에서 난 소리 같은데."
        $ chandelier_count += 1
    elif chandelier_count == 5:
        m "방금 들린 소리가 신경쓰인다."
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
                    jump inner_room

                "내려간다":
                    play audio "걷는소리 구두.mp3"
                    scene black with fade
                    jump mainhall
        else:            
            menu:
                "어디로 가지?"

                "다락방":
                    scene 다락방계단 with fade
                    play audio "사다리.mp3"
                    "사다리를 밟고 조심스레 올라간다."
                    scene black with fade
                    jump garret

                "서재":
                    jump library

                "안방":
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
        play audio "뛰는소리 숏.mp3"

        show 열쇠 at Transform(xalign=0.5, yalign=0.2) 
        "바닥에 떨어진 열쇠를 주우려는 순간"

        show 꼬마 유령 at Transform(xalign=1.2, yalign=0.2)
        hide 열쇠 
        show 꼬마 유령 at Transform(xalign=-1.2, yalign=0.2) with move
        play audio "천소리.mp3"
        "어둠 속 무엇인가, 열쇠를 낚아챘다."

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
            "구석에서 아까는 보지 못했던 일기장을 발견했다."
            m "…이건 뭐지? 일기장인가? 누구의 일기지…?"
            play audio "책넘김.mp3"
            n "유모의 일기장"
            n "오늘은 도련님이 태어나셨다."
            n "백작님과 부인께선 갈수록 도련님에게만 신경을 쏟는다."
            n "아가씨는 자꾸 혼잣말을 하거나, 거울을 오래 바라보신다."
            n "아가씨가 걱정된다..."
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
            "엇~ 틀렸어~ ㅋㅋ",
            "반대쪽이야~ 바보~",
            "캬하하! 아직 멀었는걸~"
            ]
        $ player_lines = [
            "이런... 놓쳤다...",
            "다시 집중해야겠어...",
            "어디로 간 거지...?"
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
    "당신은 열쇠를 받았다."
    hide 열쇠
    play audio "거친 숨소리.mp3"
    m "헉... 헉... 이게 무슨......"
    hide 꼬마 유령 with dissolve
    $ dining_room_lock = False
    m "이건... 열쇠로군"
    m "근처에 사용할만한 곳을 확인해봐야겠어"

    menu:
        "어디로 갈까?"
        
        "나간다":
            if room_event == False:
                $ room_event = True
                scene mainhall
                play music "bgm_main.mp3"
                show adeline 호기심 at Transform(xalign=0.5, yalign=0.2) with dissolve
                play audio "아델린 웃음소리.mp3"
                g "후훗, 꼬마애랑 재밌어 보이던데"
                g "어때? 숨바꼭질은 재밌었어?"
                menu:
                    "재밌었다.":
                        m "상대가 꼬마라 하여 힘을 아끼는 건, 기사로선 부끄러운 일이네."
                        m "누구든 정정 당당하게 마주하는 것. 그것이 곧 기사의 길이지"
                        g "풉"
                        show adeline 폭소 at Transform(xalign=0.5, yalign=0.2)
                        g "하하하하하하하"
                        g "무슨 소릴 하는거야 진짜. 하하하"
                        show screen stat_overlay with dissolve
                        $ p_bar[0] += 10
                        play audio "호감도 상승.mp3"
                        "아델린의 호감도가 10 상승했다."
                    "재미없었다":
                        m "장난하나?"
                        m "웬 이상한 꼬마의 장난 덕분에 힘들어 죽기 직전이다."
                        g "...."
                        show adeline 정색 at Transform(xalign=0.5, yalign=0.2)
                        g "기사라 할 땐 언제고"
                        g "엄살은."
                        show screen stat_overlay with dissolve
                        $ p_bar[0] -= 10
                        play audio "호감도 하락.mp3"
                        "아델린의 호감도가 10 하락했다."
            hide screen stat_overlay with dissolve
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

        m "(테이블을 바라보며) 기묘하군... 의자가 모두 붙어 있는데,"
        extend "저 하나만 왜 저렇게 떨어져 있지?"
    
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
                play audio "책넘김.mp3"
                n "오늘도 아가씨는 혼자서 밥을 드신다."
 
                n "백작님은 회의로 바쁘시고 부인은 아들을 돌보시는데 열중이다."

                n "아가씨가 웃는걸 본적이 언제였던가...."

                n "너무 안타깝다"

                nvl clear
                    
                play audio "item1.ogg"
                "당신은 주방장의 일기를 획득 했다."
                m "일기라..."
                m "아까 전 방도 확인해 볼 필요가 있겠군"
                jump dining_room

        "나간다":
            jump mainhall 

label underground:
    
    if bgm_not_playing2():
        play music "bgm_piano.mp3"

    if underground_first:
        scene black with dissolve

        play audio "돌풍.mp3"
        "지하실 입구에 다다르자, 거센 돌풍이 몰아쳤다."

        play audio "등불 점화.mp3"
        scene 지하실 with dissolve
        "몸을 낮추고, 바람을 등진 채 등불에 불을 붙였다."
        "작은 불꽃이 깜빡이며 피어오르자, 거짓말처럼 주변이 고요해진다."

        m "이 불빛만이... 어둠을 가르고 길을 밝혀주리라...."

        play audio "걷는소리 구두.mp3"

        "등불을 높이 든 채 지하실 안으로 발을 들이자, 그의 걸음이 적막한 공기를 갈라내며 울려 퍼진다."

        "차디찬 기운이 바닥 너머에서부터 스며올라와, 갑옷 너머로 그의 몸을 조용히 휘감는다."

        m "내 발걸음조차...이곳의 침묵에 흠집을 내는구나..."

        "그때, 무언가 발끝에 걸린다."

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
        n "저택이 어떤 유령에의해 저주받았다는 이야기였다."
        n "나는 퇴마를 위해 성수를 준비했다."
        nvl clear

        play audio "책넘김.mp3"
        n "18xx년 4월 6일"
        n "나는 오늘 그 유령을 퇴치하러 왔다."
        n "그러나 실패했다."
        n "나는 유령의 기습을 받고, 배에 구멍이 뚫린 채로 이 지하실로 도망쳤다."
        n "다행히 중요한 부위는 비껴나가 치료가 가능할 것 같다."
        n "나는 여기서 치료를 하고 다시 유령을 퇴치하기로 했다."
        nvl clear

        play audio "책넘김.mp3"
        n "18xx년 4월 10일"
        n "성수를 사용해봤지만 상처가 아물지 않는다."
        n "아마 유령의 저주때문 일것이다."
        n "지하실에는 누군가가 생활한 흔적이 있다…"
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
        m "‘감정’이, ‘고독’이 실체가 되어 움직이고 있다...? 이건..."
        scene black with fade
        show adeline idle at Transform(xalign=0.5, yalign=0.2) with dissolve 
        "아델린을 말하는 건가…?"
        hide adeline idle with dissolve

        "그 순간, 지하의 어둠 속에서 희미한 숨소리가 들려온다."
        scene 지하실괴물 with dissolve
        play audio "monster5.ogg"
        "조심스레 안으로 들어서자, 고요한 어둠 속에서 짐승의 울음소리가 울려퍼진다."
        
        M "……크르르르릉……"

        "거대한 그림자. 사람보다 크고, 형체가 일그러진 괴물이 서서히 모습을 드러낸다."
        "괴물이 포효하며 전속력으로 달려든다."
        
        play audio "칼소리.mp3"
        "아르망은 옆으로 구르며 칼을 뽑았다."

        scene 괴물싸움 with hpunch
        play audio "Monster 2.mp3"
        M "키에에에에엑!"

        m "악령이든 짐승이든…"
        m "너 따위에게 무너질 내가 아니야!!"
        play audio "칼 휘두름.mp3"
        play aduio "검으로 벽을 두드리는 소리.mp3"
        play audio "칼 휘두름.mp3"
        scene black
        "괴물의 발톱에 어깨가 긁혀 피가 흐르지만, 그는 몸을 낮추며 괴물의 밑을 파고든다."
        "마지막 일격—칼을 힘껏 들어 괴물의 심장을 찔러 꽂는다!"
        play audio "칼찔리는 소리.mp3"
        m "사라져라!!!"
        
        scene 괴물죽음 with fade
        "칼끝이 박히며, 괴물의 몸이 뒤틀린다."
        "괴성, 그리고 한 줄기 연기와 함께 괴물의 육체가 무너지기 시작한다."

        scene black
        M "외....로.....워...."

        "괴물의 형체가 녹아 사라진다. 아르망은 거친 숨을 쉬며 바닥에 주저앉는다."

        hide 괴물죽음 with fade
        "검 끝에 묻은 피가 천천히 사라지고, 주위는 다시 고요해진다."

        scene 지하실  with dissolve
        menu:
            "더 깊은 곳으로 들어가볼까?":
                if underground_first:
                    $ underground_first = False
                    "지하실의 안쪽 끝, 낡은 옷장과 책상, 침대가 놓여있다." 
                    "분명.. 이곳은 누군가가 생활했던 공간으로 보인다."
                    m "일기의 내용대로 누군가 살았던 흔적이 있군."
                    "희미한 빛이 벽장 너머에서 반사되어 새어나온다.."  
                    show 성수 at Transform(xalign=0.5, yalign=0.2) 
                    m "이게 일기에 적혀있던 성수인가..."
                    "성수가 있다."
    
    scene 지하실

    menu:
        "더 깊은 곳으로 들어가볼까?":
            if underground_first:
                $ underground_first = False
                scene 지하실깊 with dissolve
                "지하실 안쪽 끝, 낡은 옷장과 책상, 침대가 놓여있다. 누군가가 생활했던 흔적이 있다."
                m "일기의 내용대로 누군가 살았던 흔적이 있군."
                "희미한 빛이 벽장 너머에서 반사되어 새어나온다."  
                show 성수 at Transform(xalign=0.5, yalign=0.2) 
                m "이게 일기에 적혀있던 성수인가..."
            jump underground_deep
            
        "돌아간다":
            jump mainhall

label underground_deep:
        scene 지하실깊
        
        if holy_water == False:
            menu:
                "성수를 어떻게 할까."

                "성수를 가지고 간다":
                    $ holy_water = True
                    play audio "item1.ogg"
                    "당신은 성수를 획득 했다."
                    "돌아가자."
                    jump underground

                "그냥 돌아간다":
                    jump underground
        else:
            menu:
                "주변을 둘러봐도 더 이상 챙길 건 없는듯 하다.":
                    jump underground

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

                play audio "책넘김.mp3"

                n "집사의 일기장"

                n "백작님은 여전히 도련님에게만 관심을 가지고 계신다."

                n "업무가 많아 요즘은 아가씨를 뵙지 못하였다."

                n "아가씨를 마지막으로 본게 언제 였더라...."
                
                n "건강은 좀 나아지셨으려나..."
                
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
                n "안방의 금고 비밀번호를 계속 까먹으셔서 따로 메모 해두겠습니다."
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
        m "흠?"
        scene 초상화
        m "이상하게 생긴 초상화가 있군"
        menu:
            "초상화를 자세히 들여다본다.":
                $ photo_count += 1
                "...."
                m "소름끼치게도 생겼군 그래."
                scene 안방 with dissolve
                play audio "아이 웃는소리.mp3"
                m "음? 무슨 소리가 들린 것 같은데?"

            "무시한다":
                jump inner_room

    scene 안방 with dissolve

    menu:
        "초상화를 살펴본다.":
            if photo_count == 0:
                $ photo_count += 1
                scene 초상화 with dissolve
                "...."
                m "소름끼치게도 생겼군 그래."
                scene 안방 with dissolve
                play audio "아이 웃는소리 숏.mp3"
                m "음? 무슨 소리가 들린 것 같은데?"
                jump inner_room

            elif photo_count == 1:
                $ photo_count += 1
                scene 초상화_눈 with dissolve
                m "뭐지 이 초상화.."
                m "원래 눈을 뜨고 있었나?"
                scene 안방 with dissolve
                play audio "아이 웃는소리.mp3"
                m "..!"
                m "역시 이상해 방금 그 초상화!"
                jump inner_room

            elif photo_count == 2:
                $ photo_count += 1
                scene 초상화 with dissolve
                m "이상해.."
                m "분명 아까 전에는 눈을 뜨고 있었는데"
                play audio "스크림1.mp3"
                scene 초상화_공포 
                m "으악!"
                play audio "쓰러지는 소리.mp3"
                scene black with fade
                "아르망은 정신을 잃었다."
                "............."
                scene mainhall
                show adeline surprise at Transform(xalign=0.5, yalign=0.2) with dissolve
                g "정신이 좀 들어? 너 갑자기 기절했더라고."  ## 대사 수정 필요?
                play audio "거친 숨소리.mp3"
                m "헉..헉.. 방금 그건 뭐였지?"
                g "뭘 봤길래 호들갑이야?"
                m "안방에 걸려있는 초상화말이야!"
                show adeline 의문 at Transform(xalign=0.5, yalign=0.2)
                g "응? 초상화?"
                g "이 저택에 초상화 같은건 없는데?"
                m "뭐..?"
                show adeline idle at Transform(xalign=0.5, yalign=0.2)
                g "잘못본거겠지.. 안좋은 꿈이라도 꾼거야?"
                m "아니야 그럴리가 없어.."
                scene black with dissolve
                jump mainhall
            else:
                m "초상화가 있던 자리에는 아무것도 없다..."
                jump inner_room

        "주변을 살펴본다.":
            if safe_info:
                if safe_password:
                    scene 안방 with fade #안방 이미지
                    "당신은 방 구석에서 잠긴 금고를 발견했다"
                    show 금고 at Transform(xalign=0.5, yalign=0.2)
                    m "아까 얻은 종이에 뭔가 단서가 있을 것 같아..."
                    hide 금고
                    show 단어퍼즐 at Transform(xalign=0.5, yalign=0.2) with dissolve
                    m "단어를 찾아 입력해보자."
                    $ correct_answer = "아델린"       
                    jump input_loop
                else:
                    show 금고 at Transform(xalign=0.5, yalign=0.2)
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
        play audio "책 꺼내는 소리1.mp3"
        "드르륵... 금고가 열리는 소리가 들린다."
        "당신은 안방의 금고에서 네번째 일기장을 찾았다."
        hide 단어퍼즐
        hide 단어퍼즐답
        $ safe_password = False
        $ diary_3 = True
        $ photo_count = 3
        jump diary4
    else:
        m "그건 아닌 것 같아... 다시 생각해보자."
        jump input_loop

label diary4:

    play music "bgm_반전.mp3"

    n "금고 -일기장"
    play audio "책넘김.mp3"
    n "18xx년 4월 6일"

    n "오늘, 저택에 낯선 이가 찾아왔다."

    n "검은 수도복을 입고, 커다란 성경을 들고,"

    n "십자가를 흔들며 중얼거리던 그 사람...."

    n "사람들은 그를 ‘신부님’이라 불렀다."

    n "처음엔, 그가 나를 구하러 온 줄 알았어."

    n "그는 어쩌면… 내 외로움을 이해해줄지도 모른다고 생각했지."

    n "하지만 그는 나를 구원하러 온 게 아니었어."

    n "그의 입은 ‘악령 퇴치’만을 말했고,"

    n "그의 눈엔… 내가 사람이 아니었던거야."

    n "그래서… 나는 결심했어."

    n "그를 멈추기로"

    n "그의 배를 조용히 찔렀고 그는 놀란 눈으로 나를 봤어 ."
    
    n "저항했지만, 이미 늦었어"

    n "그는 조용히, 종잇장처럼 쓰러졌고 피를 흘렸지"
    
    n "피가 흐르던 자리에..."

    n "어느 순간 그는 사라졌어"

    n "아마 그는 죽었을 꺼야"
    nvl clear
    play audio "책넘김.mp3"
    n "18xx년 9월 18일"

    n "신부가 사라진 그날 이후, 사람들은 더 이상 이 집에 오지 않게 되었다."

    n "그 신부가 죽기 전 집에 무슨 짓을 한 게 분명하다."

    n "나는 매일 문 앞을 지켰고, 매일 누구도 오지 않았다."

    n "가끔은 그 신부의 얼굴이 떠오른다."

    n "그때 그냥… 잠시만 참았더라면…"

    n ""
    nvl clear
    play audio "책넘김.mp3"
    n "19xx년 1월 6일"

    n "웃는 연습을 했다."

    n "말하는 연습도 했다."

    n "혹시라도 누군가 오면… 반갑게 맞이하고 싶었으니까."

    n "하지만 오지 않았다."

    n "거울에 비친 내 얼굴이 낯설다."

    n "나는 아직 웃고 있는 걸까?"

    n "아니면 울고 있는 걸까?"

    n ""
    nvl clear
    play audio "책넘김.mp3"
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
    
    stop music
    stop audio
    if bgm_not_playing():
        play music "bgm_main.mp3"
    if garret_first:
        if orgel_try:
            play music "기믹_오르골 원본.mp3"
            "갑자기 안쪽에서 오르골 소리가 들려온다."
            m ".....날 환영하는 소리인가?"
            scene 다락방 with dissolve
            "다락방 안쪽, 달빛이 비스듬히 스며드는 어둠 속."
            
            show 오르골유령 at Transform(xalign=0.5, yalign=0.2) with dissolve 
            "어둠 속에서 실루엣 하나가 천천히 떠오른다."

            "검은색 레이스가 겹겹이 덧대어진 드레스는 낡아 찢긴 자락이 바람에 휘날리듯 흔들리고,"

            "머리 위엔 정갈하게 손질된 고풍스러운 모자가 얹혀 있다."

            "그러나 그 안의 얼굴은 반쯤 흐릿하고,"
            extend " 눈동자 없는 눈이 달빛에 허옇게 반사된다."

            jump orgel_test
        else:
            play music "기믹_오르골 원본.mp3"
            scene 다락방 with dissolve
            show 오르골유령 at Transform(xalign=0.5, yalign=0.2) with dissolve
            s "후후.. 또 왔구나"
            jump orgel_test
    
    menu:        
        "어디로 갈까?"

        "나간다":
            jump two_stair

label orgel_test:
    
        $ orgel_try = False

        s "후후 이 노래 정말 좋지 않아?"
        s "너도 함께 듣지 않을래?"

        menu: 
            s "마음에 들거야"

            "오르골을 함께 듣는다":
                stop music
                play audio "기믹_오르골_단어1.mp3"

                window hide

                $ renpy.pause(10.0, hard=True)
                s "이 오르골 소리가 참 곱지?"
                m "언제까지 들어야 하지?"
                s "더 들어봐"

                # play "기믹_오르골_단어1.mp3"
                play audio "기믹_오르골_단어2.mp3"

                window hide

                $ renpy.pause(10.0, hard=True)
                s "첫째아이가 태어난 날 내가 만든 오르골이야"
                m "하고 싶은 말이 뭐지?"
                s "그 아이가 커서 이 노래를 기억하길 바랬지"

                play audio "기믹_오르골_단어3.mp3"

                # play "기믹_오르골_단어2.mp3"

                window hide

                $ renpy.pause(10.0, hard=True)

                m "이제 끝났나?"

                s "잘 들었지?"

                # play "기믹_오르골_단어3.mp3"
                $ correct_answer = "정화수"

                jump garret_input_loop
            
            "듣지 않는다":
                stop music
                "순간 오르골 노래 소리가 뚝하고 끊어졌다."
                show 오르골유령_정색 at Transform(xalign=0.5, yalign=0.2)
                play audio "우는소리.mp3"
                "너도.."
                "너도 날 버리고 가는거야..?"
                play audio "여자비명2.mp3"
                scene 오르골귀신 
                "당신은 다락방에서 쫓겨났다."
                jump two_stair

label garret_input_loop:
    $ player_input = renpy.input("숨겨진 단어는 무엇일까?").strip().lower()

    if player_input == correct_answer:
        $ garret_first = False
        m "정화수"
        m "단어를 이어붙이니 그렇게 들리는군"
        s "너 정말 열심히 들었구나?"
        $ light = True
        show 등불 at Transform(xalign=0.5, yalign=0.2)
        "자 이건 선물이야."
        play audio "item1.ogg"
        "당신은 등불을 획득 했다."
        scene black with fade
        "그렇게 유령은 사라졌다."
        jump garret
    else:
        show 오르골유령_정색 at Transform(xalign=0.5, yalign=0.2)
        s "뭐..? [player_input]..?"
        play audio "우는소리.mp3"
        hide 오르골유령
        hide 오르골유령_정색 with dissolve
        scene black with fade
        s "흐윽.."
        s "흑.. 흑.."
        play audio "여자비명2.mp3"
        scene 오르골귀신 
        "당신은 다락방에서 쫓겨났다."
        jump two_stair

label hallway:
    play audio "걷는소리 구두.mp3"
    scene black with dissolve
    pause 2
    scene hallway1_base with dissolve
    m "뭐지... 분명 난 2층에서 내려왔을텐데"

    menu:
        "내려간다":
            play audio "걷는소리 구두.mp3"
            scene black with dissolve
            pause 2
            scene hallway1_base with dissolve
    menu:
        "내려간다":
            play audio "걷는소리 구두.mp3"
            scene black with dissolve
            pause 2
            scene hallway1_base with dissolve
            m "역시..계속 같은 곳을 맴돌고 있어.."
    menu:
        "내려간다":
            play audio "걷는소리 구두.mp3"
            scene black with dissolve
            pause 2
            scene hallway1_diff1 with dissolve
            m "음? 저런 시계가 원래 있었나?"
    menu:
        "올라가서 확인해본다":
            play audio "걷는소리 구두.mp3"
            scene black with dissolve
            pause 2
            scene hallway1_base with dissolve
            m "역시.."
            m "원래 저런 시계는 없었는데.."
            m "음? 벽에 무언가 쓰여있군."

            n "과거에 매몰되어 앞만 보고 달리는 우군이여"
            n "시대의 변화를 외면하고 도망가는 패배자여"
            n "그대 행동, 마땅히 비난받아야 할 일이다만."
            n "남겨진 자와의 만남엔 이보다 좋은 지름길은 없으리"
            nvl clear
            ".... 마지막 글씨는 얼룩 때문에 보이지 않는다."

            m "....."
            m "..이건 나를 두고 하는 말인가?"
            m "어찌됐든 지금은 앞으로 나아가는 방법 밖에 없어"
            play audio "item1.ogg"
            " * 복도를 자세히 보세요. 뭔가 이상한 부분이 있다면 돌아가는 것이 좋습니다."
            play audio "걷는소리 구두.mp3"
            scene black with dissolve
            pause 3
    jump hallway_stage

label hallway_stage:
    if progress == 1:
        jump hallway_show_answer_1
    elif progress == 2:
        jump hallway_show_answer_2

label hallway_show_answer_1:
    scene bg hallway1_base with dissolve
    jump hallway_loop

label hallway_show_answer_2:

    scene bg hallway2_base with dissolve
    play music "여자 콧노래.mp3"
    m "..!"
    m "붉은 달이라니..."
    m "그리고 이 노래는..."
    m "......"
    m "어찌됐든 지금은 이 복도를 기억해두는게 좋을 것 같아"
    pause 3
    play audio "걷는소리 구두.mp3"
    scene black with dissolve
    pause 3
    jump hallway_loop

label hallway_entry:
    if clears == 0:
        jump hallway_stage
    else:
        jump hallway_loop

label hallway_loop:
    $ current_data = hallway_data[progress]
    if renpy.random.random() < 0.5:
        $ current_bg = current_data["correct"]
    else:
        $ current_bg = renpy.random.choice(current_data["options"])

    scene expression "bg/" + current_bg with dissolve

    menu:
        "앞으로 나아간다":
            play audio "걷는소리 구두.mp3"
            scene black with dissolve
            if current_bg == current_data["correct"]:
                $ clears += 1
                if clears >= 3:
                    $ progress += 1
                    $ clears = 0
                    if progress > 2:
                        pause 3
                        jump next_room
                    else:
                        pause 3
                        jump hallway_entry
                else:
                    pause 3
                    jump hallway_loop
            else:
                m "이런.. 놓친 부분이 있었나."
                "처음부터 다시 해보자."
                $ clears = 0
                jump hallway_entry

        "뒤로 돌아간다":
            play audio "걷는소리 구두.mp3"
            scene black with dissolve
            if current_bg == current_data["correct"]:
                m "또 처음으로 돌아왔군."
                "다시 해보자."
                $ clears = 0
                jump hallway_entry
            else:
                if clears >= 3:
                    $ progress += 1
                    $ clears = 0
                    if progress > 2:
                        jump next_room
                    else:
                        "뒤로 돌아가자..."
                        "다른 복도가 나왔다."
                        jump hallway_entry
                else:
                    pause 3
                    jump hallway_loop

label next_room:
    stop music
    scene bg dream with dissolve
       
    m "여긴... 대체...?"
    g "어때, 이 꽃? 정말 예쁘지 않아?"
    g "어렸을 땐 부모님이 날 이 꽃밭에 데려다 주셨어. "
    extend "햇살 가득한 날, 엄마가 내 머리에 꽃을 꽂아주며 웃으셨지."
    g "그때는 세상이 다 따뜻하고, "
    extend"모든 게 가능할 것 같았어."
    g "하지만 남동생이 태어난 이후로, "
    g "{size=+10}모든 것이 끝나버렸어.{/size}"
    g "부모님의 관심은 전부 남동생에게로 가버렸고"
    g "그 후로 난..." 
    g "늘 외롭고, 차가운 현실 속에 홀로 남겨졌어."

    m "아델린..."

    g "이 어둠 속, 이 쓸쓸한 곳에 너가 와준 건 마치 한 줄기 빛 같았어."
    g "처음엔 네 시끄럽고 거칠게 들리는 말투, 허세 섞인 태도에 나도 모르게 마음을 닫으려 했어."
    g "그런데, 네가 점차 보여준 항상 당당한 모습, 그리고 눈빛 속에 숨겨진 고독을 알게 된 후, "
    extend "내 심장은 미친 듯이 뛰기 시작했어."
    g "나와 함께 하자. 영원히.....!"

    if holy_water:
        if p_bar[0] > 50:
            jump happy_ending_1
        else:
            jump bad_ending_1
    else:
        if p_bar[0] > 50:
            jump happy_ending_1
        else:
            jump bad_ending_1

# label happy_ending:

#     play music "bgm_감동.mp3"

#     play audio "Equip2.ogg"

#     "아르망은 천천히 투구를 벗으며,"
#     extend "부드럽고 슬픈 표정으로 아델린을 바라보았다."

#     m "아델린, 미안해. 내가 잘못 생각했어."

#     g "아르망...? 어째서...? 너는는 나를 이해하는거 아니였어...?"

#     m "그래, 이해한다고 믿었어. 하지만 나도 너처럼 과거에 얽매여 있었던 것 같아."

#     m "나는 기사였던 시절이 그리워서, 그 시절의 낭만과 명예만을 좇아왔지."

#     m "하지만 지금 세상은 더 이상 나 같은 기사를 필요로 하지 않아."

#     m "시대는 변했고, 나는 그 변화를 외면하며 계속 과거에만 머물렀지."

#     "g는 흔들리며 눈물을 글썽인다."

#     g "그럼... 나는...? 나 역시 이대로 과거에 갇혀 살아야만 하는 거야...?"

#     m "아니야, 아델린. 이제 너도, 나도 더 이상 그렇게 살아선 안 돼."

#     m "너를 만난 시간은 나에게 정말 소중했어."

#     m "마치... 아름답고 낭만적이던 그 옛날로 돌아간 것 같았지."

#     m "하지만, 이 이야기도 이제 끝낼 때가 된 거야. 너와 나 모두 과거로부터 벗어나야만 해."

#     "g는 눈물을 흘리며 떨리는 목소리로 묻는다."

#     g "그럼 난... 어디로 가야 하는 거지...? 나는 언제나 혼자였는데..."

#     m "아니, 넌 혼자가 아니었어. 네 곁을 지키던 사람들이 있었잖아. 집사, 유모, 그리고 주방장... 그들은 너를 사랑했어."

#     "g의 얼굴에 희미한 미소가 떠오른다."

#     g "맞아... 그들은 언제나... 나를 걱정했었지..."

#     "g는 잠시 생각에 잠기더니 조용히 입을 연다."

#     g "지하에서 가져온 성수... 가지고 있지? 그거면... 될 거야."

#     m "정말 괜찮겠어?"

#     g "응. 그저 나를 위해 기도해줘, 기사님... 부탁할게."

#     "아르망은 성수를 들어 조용히 뿌린 뒤, 부드럽고 단호한 눈빛으로 아델린을 바라본다."

#     m "편히 쉬어, 아델린. 나도 이제 앞으로 나아가야겠지."

#     "성수의 빛 속에서 아델린은 환하게 미소 지으며 서서히 사라진다."

#     scene ending1

#     m "안녕, 아델린. 이제는 나도 진정으로 앞으로 나아갈 때가 왔어."

# label bad_ending:
    
#     "아르망은 투구를 벗지 않고 성수를 들며 냉정한 눈빛으로 아델린을 응시한다."

#     "g는 배신감을 느끼며 아프게 웃는다."

#     g "그랬구나... 결국 너도... 결국 날 버리는 거구나!"

#     m "나는 벨포르 가의 아르망, 기사로서 마땅히 해야할 일을 할 뿐이다다!"

#     m "이 성수로 너를 보내고, 이 저택의 저주를 끝내겠다!"

#     "g는 절규하며 비명을 지른다."

#     g "결국 너도 똑같아! 이기적인 인간들! 다 똑같아!!"

#     "g는 괴로운 듯 비명을 지르며 사라진다."

#     "아르망은 차가운 눈빛으로 사라진 아델린의 자리를 바라보며 조용히 중얼거린다."

#     m "나는 명예로운 기사.. 나는 기사로서의 내 의무를 다한 것이다."

#     "칼을 허리에 다시 차고, 아르망은 무거운 발걸음으로 저택의 정문을 나선다."

#     scene bad_ending

#     "그 후 아르망은 마을에 돌아가 자신이 저택의 유령을 정화했다고 외쳤지만, 마을 사람들은 그를 미친 사람 취급하며 외면했다."

#     "결국 아르망은 자신을 이해해주는 사람 하나 없이, 홀로 과거에 집착한 채 쓸쓸히 살아간다."

#     "-END-"

# label bad_ending:
