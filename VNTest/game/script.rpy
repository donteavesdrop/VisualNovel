init python:
    import pygame
    import os
    import random

# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# define narrator = Character('Thoughts', color="#808080") # рассказчик для описания или мейби мысли гг
define mc = Character('ГГ', color="#c8ffc8") # сам гг
define elizabeth = Character('Элизабет', color="#FF69B4") # элизабет
define vlada = Character("Влада", color="#40E0D0") # влада
define stas = Character("Стас", color="#FFFF00") # Стас
define sasha = Character("Саша", color="#B0E0E6") # Саша
define policeman = Character("Полицейский", color="#00008B") # полция

#Музыка
define audio.musbar1 = "music/bar1.mp3"
define audio.musintro = "music/intro.mp3"
define audio.muslove = "music/love.mp3"
define audio.muspolice = "music/police.mp3"
define audio.mustolpa = "musci/tolpa.mp3"

#Звуки
define audio.zvsms = "sounds/ayfonsms.mp3"
define audio.zvzvon = "sounds/ayfonzvon.mp3"
define audio.zvpolice = "sounds/polits2.mp3"
define audio.zvposuda = "sounds/posuda3.mp3"
define audio.zvticktack = "sounds/ticktack.mp3"

# Локации
image street_intro = "bg/street_intro.png" # заменить на черный фон для начала истории
image bar = "bg/bar.png" # бар
image room_el = "bg/roomel.png" # комната девушки 1
image room_vlada = "bg/roomvlada.png" # комната девушки 2
image police = "bg/police1.png" # полиц уч
image doors = "bg/doors.jpg" # двери в квартиры
image street = "bg/street2.png" # улица

# Спрайты
image mc = "chs/mc.png" # главный герой
image sasha = "chs/sasha.png" # саша
image elizabeth = "chs/el.png" # элизабет
image vlada = "chs/vl.png" # влада
image cop = "chs/cop.png" # коп
image drunk = "chs/drunk.png" # пьяница
image stas = "chs/stas.png" # стас
image tv = "bg/TV.png" # телевизор

transform walk(start, end, tall):
    xpos start ypos tall xanchor 0.5 yanchor 0
    linear 0.5 xpos end

# Загатовки
#    show mc: для передвижения по экрану
#        xpos 450 ypos 100
#        linear.3 xpos 50 ypos 100
#        linear.3 xpos 25 ypos 100

init: # константы
    $ left2 = Position(xalign=0.2, yalign=1.1)  # позиция
    $ right2 = Position(xalign=0.8, yalign=1.1)  # позиция
    $ zlost = 0 # степень агрессивности друзей???
    $ constEl = 0 # флирта с элизабет
    $ changebar = 0 #  для ухода
    $ keys = 0 # для ухода
    $ lovesoundel = 0 # для музыки эл
    $ introsoundStreet = 0 # для музыки в сцене с владой

# Игра начинается здесь:
label start: # начало игры
    play music musintro fadein (0.5)  # фоновая музыка в интро
    #play music = "" fadein(0.5) # музыка для начала, нарастает 0.5
    "" "Меня зовут ГГ – обычный выпускник обычного технического вуза, как и все остальные привыкаю к новой жизни работяги. Оглядываясь назад жизнь студента была не такой уж и плохой по сравнению с нынешней."
    "" "Свободного времени стало еще меньше, хватает лишь дэйлики выполнить по вечерам. Но сегодняшний вечер исключение. Сегодня в первые за долгое время мы решили собраться со старыми друзьями и выпить."
    scene street_intro
    show mc at center with dissolve:
        zoom 1.15
        ypos 1200
    "" "Пока я иду в бар, на улице уже темнеет. Днём Москва нагнетает своей серостью и однообразностью, но в ночных огнях фонарей она приобретает совершенно другой вид."
    "" "Город, который казался уставшим, ночью оживает и преобажается. Вокруг мерцает многочисленная реклама, люди уже не так угрюмы, ведь большинство из них здесь с целью отдохнуть, собственно как и я."
    "" "Надеюсь, сегодня получится воссоздать атмосферу студенческих лет, когда у нас было много свободного времени и мы могли себе позволить ходить на вечеринки каждый вечер."
    "" "Теперь же все по-другому. Работа, обязательства, ответственность..."
    hide mc at center with dissolve
    stop music fadeout (0.5)
    jump bar

label bar: # сцена в баре
    scene bar
    play music musbar1 fadein (0.5)
    "" "Я люблю атмосферу в барах. Не знаю, как это лучше описать. Уютно тут. Создается ощущение свободы и возможности забыться на время. Хотя иногда такое заканчивается не очень весело, но это опустим."
    stas "Йоу!!!"
    show mc at left with easeinleft:
        zoom 1.15
        ypos 1200
    show stas at right with easeinright:
        zoom 1.15
        ypos 1200
        xpos 1550
    # show sasha at right with easeinright:
    #     zoom 1.15
    #     ypos 1150
    "" "А вот и мои братки"
    stas "Здарова ГГ, долго же ты!"
    "" "Этот пижон - мой друган Стас. Мы знакомы с ним еще со школы. На первый вгляд может показаться сомнительной личностью, но он хороший человек"
    mc "Да в соседнюю квартиру заехала девушка и попросила помочь ей там с коробками. О! Привет Саня."
    show sasha at right with easeinright:
        zoom 1.15
        ypos 1150
    sasha "Привет..."
    "" "А этот угрюмый тип – Санёк, трудоголик, с которым мы познакомились в университете. Еще недавно выпускник, а сейчас уже семьянин. Бедняга."
    mc "Вы уже начали пить?"
    stas "Так а чего мы тут собрались? Тебя ждать сидя в мобилах?"
    stas "Ты знаешь что это означает. Штрафную."
    menu:
        "Летс гоу, я только за. Девушка! Будьте добры бокальчик...":
            stas "Мужик!"
            "" "И я выпил..."
            stas "Хах, хорошее начало вечера, готов поспорить, что живым уйду отсюда только я"
            sasha "Мда, и это говорит наш главный тусовщик, ты тут единственный границ не видишь"
            stas "В смысле?? Всё я вижу, они у меня просто шире"
            "" "Приятно знать что время не сильно нас изменило"
            # мейби добавить переменну на бухло??
        "Мужики, успеется. Не давите, дайте выбрать сначала":
            stas "Ссыкло!"
            mc "Да не парни, я еще хочу домой спокойно добраться, не против выпить, но давайте все вместе. Я уже не настолько молод"
            stas "Эх понятно, прошло две минуты, а уже душнишь"
            sasha "Да ладно тебе, Стас, давайте уже вместе выпьем"
    mc "Ну что ж. Как жизнь нелегкая?"
    stas "Кто сказал, что нелегкая. На рынке акций в последнее время всё хорошо, и у меня соответственно тоже. Из последнего купил робот пылесос. Невероятная вещь, полюбил его больше чем свою кошку"
    sasha "Весело. А мне помимо работы сегодня еще пришлось идти с малым в поликлинику. Жуткое место и жуткие очереди. А у тебя что как нынче?"
    "" "КАК ДЕЛА??"
    "" "Хм, а и правда, как у меня дела? Даже не знаю, что рассказать, жизнь ужасно скучная."
    menu:
        "Да собственно ничего, всё как обычно...":
            stas "Чтожжжж, из тебя как обычно отличный собеседник"
            sasha "Да отстань от него, реально нечего рассказать бывает, одна рутина."
        "У меня всё шикарно!!! Вот выбил сигнатурное оружие на Райден недавно!!":
            stas "АХАХАХАХ дай угадаю, девушку так и не нашел??) Знаешь, я тоже не против поиграть, но и real life stuff люблю."
            sasha "Эх, везёт же, у меня времени на игрушки вообще нет"
    "" "Дальше мы просто наслаждались вечером и компанией друг друга." #(затемнение и таймскип) (звук часиков?? или звук толпы погромче)
    hide sasha with dissolve
    hide stas with dissolve
    hide mc with dissolve
    stop music fadeout (1.0)
    scene black
    play sound zvticktack
    $ renpy.pause(1.0)
    "" "..." # тайм скип, хз нужно ли??
    # звук тиакющих часов
    play music musbar1 fadein (0.5)
    scene bar
    show mc at left with dissolve:
        zoom 1.15
        ypos 1200
    show stas at right with dissolve:
        zoom 1.15
        ypos 1200
        xpos 1550
    show sasha at right with dissolve:
        zoom 1.15
        ypos 1150
    sasha "Как же я устал, не женитесь, парни."
    mc "Опять с женой проблемы?"
    sasha "Даже не хочу об этом. Программистам не нужны женщины."
    sasha "Завидую тебе, гг, проблем никаких"
    stas "Ну не скажи, ты просто не умеешь жить в кайф. ГГ, неужели никто не запал в сердце?"
    mc "Да я как то даже не думал об этом"
    stas "Мда, с таким подходом  отношения у тебя будут только в дейтсимах."
    mc "Не гони"
    stas "Слабо сейчас подойти познакомиться?"
    mc "Да вообще изи, предложи любую"
    "" "И тут мы начали осматриваться вокруг"
    "" "Моё внимание привлекла девушка у барной стойки. Первая мысль *Она слишком хороша для меня*"
    "" "Я увидел ехидную ухмылку Стаса и сразу понял, что к чему."
    mc "НЕТ"
    "Cтас и Саня" "ДА!"
    mc "Я вас ненавижу."
    "" "Что же я ей скажу...."
    hide mc with dissolve
    hide stas with dissolve
    hide sasha with dissolve
    "" "Если честно, еще ни разу не подходил познакомиться с девушкой. Я набрался смелости и пошёл не думая"
    show elizabeth at right with dissolve:
        zoom 1.15
        ypos 1200
        xpos 1700
    show mc at left with easeinleft:
        zoom 1.15
        ypos 1200
        xpos 600
    menu:
        "Привет, ты мне понравилась, не хочешь пообщаться???": # не уверен нужно ли
            "" "Она оценочно посмотрела на меня и сказал"
            "???" "Прости, мне сейчас это не интересно..."
            "" "И я ушёл в слезах."
        "Эм, слышала, что сегодня новый патч в финалке?? Пойдешь на новый рейд??": # спросить у кости
            "???" "Ээээм, что???"
            "" "Б** какой же бред я сказал, пора сваливать, это точно провал..."
            $ constEl = constEl + 1
        "Йоу королева, почему одна?? Сейчас будет два!":
            "???" "Мечтай....(резко отворачиваясь)"
            "" "И я ушёл в слезах"
    show mc at walk(600, 50, 90)
    $ renpy.pause(0.3)
    hide mc with dissolve
    hide elizabeth with dissolve
    "" "..."
    show sasha at right with dissolve:
        zoom 1.15
        ypos 1150
    show stas at right with dissolve:
        zoom 1.15
        ypos 1200
        xpos 1550
    "Стас и Саня" "Ахаха, ну что, ботяра???"
    show mc at left with easeinleft:
        zoom 1.15
        ypos 1200
    mc "Заткнитесь и наливайте..."
    # мини игра с выпивкой или тайм скип
    hide mc with dissolve
    hide stas  with dissolve
    hide sasha with dissolve
    stop music fadeout (2.0)
    scene black
    play sound zvticktack
    $ renpy.pause(1.0)
    "" "..."
    play sound zvposuda
    $ renpy.pause(1.0)
    # тайм скип и звук ломающейся посуды
    scene bar
    play music muspolice fadein (0.5)
    show drunk at center with dissolve:
        zoom 1.15
        ypos 1200
    "" "Что?? Мы заметили, как за соседним столиком ссорилась одна пара и казалось, что мужик много себе позволяет, будто он сейчас ударит девушку."
    "" "ДА ЧТО ОН СЕБЕ ПОЗВОЛЯЕТ???"
    menu:
        "(Пойти въ***ть ему)":
            mc "ЭЙ МУЖИК!! НЕ ТРОГАЙ ДЕВУШКУ!!!"
            scene black
            play sound zvpolice
            $ renpy.pause(1.0)
            "" "Больше ничего не помню кроме звука полицейских сирен."
            jump police
        "(Ничего не делать, день и так уже кринж)":
            "" "Лучше тихо отсижусь, сами разберутся, у меня достаточно своих проблем."
            hide drunk with dissolve
            stop music fadeout (1.0)
            $ introsoundStreet = introsoundStreet + 1
            jump doors


label police: # сцена с полиц
    scene street_intro
    # play music muspolice fadein (0.5)
    "" "Приехала полиция и мы стояли на улице, возле входа в бар."
    show cop at right with dissolve:
        zoom 1.15
        ypos 1200
    show mc at left with dissolve:
        zoom 1.15
        ypos 1200
    policeman "Так, молодой человек, рассказывайте. Зачем вы его напали на того гражданина?"
    mc "Что значит напал? Я защищал женщину, которую он кстати намеревался ударить!"
    policeman "Эта женщина как раз и вызвала нас, сообщив что на её мужа набросились."
    mc "Чего?! Что это значит? Но ведь..."
    policeman "Ясно, дебош в общественном месте, дра..."
    if constEl == 1:
        "???" "Постойте! Подождите пожалуйста. Я могу рассказать о произошедшем."
        show elizabeth at left with easeinleft:
            zoom 1.15
            ypos 1200
            xpos 500
        "" "Посмотрев кто подошел, я немного опешил. Эта была та самая девушка, с которой я пытался познакомиться."
        "" "Краем глаза я заметил своих друзей, которые тоже собирались подойти, но остались наблюдать."
        "" "Она поведала, о том что я нормальный парень, а та парочка - пьяницы, устроившие сцену."
        policeman "Так значит это те двое начали нарушать спокойствие. Хорошо. Можете быть свободны, сейчас мы поговорим с ними."
        policeman "Но постарайтесь больше не прибегать к кулакам. Вам может повезти меньше."
        hide cop with dissolve
        "" "Пронесло..."
        mc "Спасибо, не стоило. Прости за неудобства."
        "???" "Что ты. Меня саму напрягал шум тех двоих. А ты вроде неплохой парень."
        "" "Господи, она святая!"
        mc "Еще раз спасибо, что выручила. Как я могу тебя отблагодарить? Я кстати ГГ, а тебя как звать"
        "???" "Элизабет. Дай как подумать... Можешь угостить меня, я бы хотела кое-что спросить у тебя."
        mc "... КОНЕЧНО! Ой... Да, конечно, пошли!"
        "" "Я посмотрел на парней, и мы поняли друг друга. Они подмигнули, а я направился с Элизабет обратно в бар."
        hide elizabeth with dissolve
        hide mc with dissolve
        stop music fadeout (1.0)
        scene black
        play sound zvticktack
        $ renpy.pause(1.0)
        "" "..."
        scene bar
        play music muslove fadein (0.5)
        show mc at left with dissolve:
            zoom 1.15
            ypos 1200
        show elizabeth at right with dissolve:
            zoom 1.15
            ypos 1200
        elizabeth "Так вот. Я хотела спросить о том, что ты спрашивал меня ранее вечером. Кажется ты что-то говорил про Final Fantasy..."
        "" "Что-что? Мне не послышалось??"
        mc "Дааа... Я немного занервничал и случайно спросил про финалку. А как ты...?"
        elizabeth "Сказать по секрету я тоже в неё играю. Недавно даже на фест ходила, где был стенд игры"
        mc "Не может быть, я там тоже был. Чокобо брелок купил..."
        # stop music fadeout (1.0)
        scene black
        play sound zvticktack
        $ renpy.pause(1.0)
        "" "..."
        $ lovesoundel = lovesoundel + 1
        jump elizabethHome

    "Стас и Саня" "Подождите!"
    show sasha at left with easeinleft:
        zoom 1.15
        ypos 1150
        xpos 450
    show stas at left with easeinleft:
        zoom 1.15
        ypos 1200
        xpos 800
    sasha "Позвольте я вам расскажу о произошедшем..."
    "" "Парни поговорили с товарищем полицейским, и с их помощью я смог объясниться."
    policeman "Так значит это та парочка начала нарушать спокойствие. Хорошо. Можете быть свободны, сейчас мы поговорим с ними."
    policeman "Но постарайтесь больше не прибегать к кулакам. Вам может повезти меньше."
    hide cop with dissolve
    "" "Пронесло..."
    mc "Спасибо, мужики. Выручили."
    sasha "Не за что. Но не делай так больше"
    stas "Это уж точно, ахахах. Герой нашелся..."
    hide stas with dissolve
    hide sasha with dissolve
    hide mc with dissolve
    stop music fadeout (1.0)
    scene black
    play music musintro fadein (0.5)
    "" "Мы пошли обратно в бар, посидели еще немного, смеясь с ситуации в которой только что были. Запоминающаяся встреча вышла" # изменил на пошли обратно в бар а не в новый бар
    $ changebar = changebar + 1
    jump doors
    # мини игры выпивка??


label elizabethHome:
    if keys == 1:
        scene black
        "" "В этот раз я быстро добрался до бара."
        scene bar
        show mc at left with dissolve:
            zoom 1.15
            ypos 1200
        "" "Зайдя внутрь я стал искать глазами Стаса. Но его нигде не было. Я пошел к стойке спросить у бармена о ключах."
        "???" "Постой"
        show elizabeth at right with easeinright:
            zoom 1.15
            ypos 1200
        "" "Кто-то окликнул меня. Посмотрев кто, я немного опешил. Эта была та самая девушка, с которой я пытался познакомиться."
        mc "Ты... мне?"
        "???" "Да-да"
        mc "Сл..ушаю, ахах"
        "???" "Твои ведь ключи?"
        mc "Оу! Да, но почему они у тебя?"
        "???" "Я их нашла на полу возле себя. Наверное они выпали, когда ты подходил познакомиться. (сказав это, она улыбнулась)"
        "???" "Я хотела отдать их твоему другу, но он сказал, раз я все равно еще не собираюсь уходить, оставить у себя, а если и пойду, то оставить бармену. А сам ушёл."
        "" "Вот же придурок"
        mc "Ох, спасибо тебе большое. И прости за неудобства. Я тогда побегу"
        "???" "Да погоди же. Это случаем не брелок чокобо у тебя на ключах? Кажется ты фанат Final Fantasy..." # упростил диалог а то не стакается с прошлым
        mc "... ДА! Ой. Да, этот брелок я купил не так давно на фесте на стенде финалки."
        "???" "Правда? Я тоже там была. Меня кстати зовут Элизабет."
        mc "ГГ, очень приятно познакомиться."
        scene black
        stop music fadeout (1.0)
        play sound zvticktack
        $ renpy.pause(1.0)
        "" "..."
    scene bar
    if lovesoundel == 0:
        play music muslove fadein (0.5)
    show mc at left with dissolve:
        zoom 1.15
        ypos 1200
    show elizabeth at right with dissolve:
        zoom 1.15
        ypos 1200
    "" "Совершенно неожиданно оказалось, что Элизабет не такая пугающая, как на могло показаться на первый взгляд. К тому же мы фанаты одной и той же ммо!"
    "" "Мы просидели, вот так болтая, еще какое-то время. В баре осталось уже совсем мало народу. И судя по всему они скоро закрывались. Мы расплатились за напитки."
    elizabeth "Раз такое дело, как насчет зайти ко мне? Я живу буквально в соседнем доме. А метро уже закрыто."
    "" "Джекпот! подумал я"
    mc "Да что ты, я не хочу доставлять трудностей, нооо, если ты конечно настаиваешь."
    elizabeth "Отлично. Тогда пошли"
    scene black
    "" "Она схватила меня, и мы вышли. А уже через пару мгновений я уже очутился в её квартире. Я и подумать не мог, что жилище такой статной леди будет таким. А где дворецкий и прочее?"
    scene room_el
    show mc at left with dissolve:
        zoom 1.15
        ypos 1200
    show elizabeth at right with dissolve:
        zoom 1.15
        ypos 1200
    elizabeth "Винца будешь?"
    play sound zvsms
    $ renpy.pause(1.0)
    "" "Внезапно нам обоим пришло уведомление на телефон о начале рейда. Мы посмотрели друг на друга"
    elizabeth "У меня еще есть ноут..."
    mc "Ни слова больше, всё ясно. Запускай!"
    "" "С каждой освоенной механикой, мы становились всё ближе и ближе..."
    stop music fadeout (1.0)
    # мини игра рпг
    jump elGame
    # return


label doors: # сцена перед квартирой гг и влады
    scene black
    if introsoundStreet == 1:
        play music musintro fadein (0.5)
    if changebar == 0:
        "" "Мы еще какое-то время провели в баре. Та буйная парочка вроде успокоилась и позже ушла."
    "" "Саньку позвонила жена, после чего он сказал, что ему пора."
    "" "Мы со Стасом посидели еще какое-то время, и я тоже решил пойти домой. Он же остался, сказав что дома делать нечего."
    scene street
    show mc at left with dissolve:
        zoom 1.15
        ypos 1200
    "" "Я шёл, пошатываясь, по ночным улицам. Постепенно прохладный воздух привёл меня в чувства, и я стал как огурчик. Хорошо быть молодым."
    "" "Подойдя к подъезду, я не обнаружил ключей ни в одном из своих карманов. Ну... ничего не поделаешь."
    "" "Постояв некоторое время у закрытой двери, я решил пойти в ближайший круглосуточный за сушняком."
    "" "Приближаясь к месту назначения, я встретил знакомое лицо"
    show vlada at right with easeinright:
        zoom 1.15
        ypos 1200
    vlada "О! Да это же мой соседушка, ГГ! Неожиданная встреча. Передо мной стояла юная девушка с пакетами в руках, которая не так давно заехала в соседнюю квартиру."
    "" "Её зовут Влада. Красивое имя. Хоть мы и не так часто контактировали, но она мне показалась хорошей и жизнерадостной. И, что самое главное, миленькой! Особенно в домашней одежде, как сейчас на ней."
    mc "Привет. Чего это ты в такое позднее время решила сходить за покупками?"
    vlada "Хаха... Немного неловко это говорить, но я проснулась совсем недавно, а в холодильнике пусто... пчих! Сам то чего тут?"
    mc "Будь. Я с друзьями встречался, а как вернулся понял, что ключи посеял и не смог попасть в дом. Выручишь? У меня в тамбуре запасной ключ от квартиры вроде есть."
    vlada "В таком случае это судьба, хихи. Пошли?"
    mc "Давай с сумками помогу тогда."
    vlada "Оу, да у нас тут джентельмен. Ну давай."
    "" "По дороге мы болтали о том, о сём по мелочи. Это первый раз когда мы так много говорили."
    "" "Оказалось, что у нас, на удивление, много общих интересов. Каким-то образом мы начали обсуждать вчерашнюю презентацию PlayСтанции."
    play sound zvzvon
    $ renpy.pause(3.0)
    "" "Эту довольно приятную беседу прервал звонок. Это был Стас."
    $ renpy.pause(1.5)
    stas "Хай! Ты случаем ничего не терял?"
    mc "Ключи. Ты их нашел? Слава Богу!"
    stas "Ну не совсем я их нашел, но они действительно нашлись. Если хочешь получить их плюс приятный сюрприз, то дуй обратно в бар."
    stas "А нет, так заберешь их у бармена в другой день. Ой... Ладно, давай, покеда!"
    "" "Он сбросил. Что за сюрприз? Ну да ладно. Я убрал телефон в карман."
    vlada "Таак продолжая разговор о новом Теккене..."
    "" "Она почему-то заговорила неуверенно."
    vlada "Не хотел бы ты...  зайти сейчас ко мне? Могли бы сыграть вместе."
    vlada "Угощу еще баночкой холодненького, хихи"
    "" "Сказала она уже более уверенно, встав в позу, расставив ноги и указывая на пакет, что я нёс. Там действительно было по мимо всего прочего несколько банок жигулей."
    "" "Что же делать?! Милая соседка завет зарубиться в файтинг! Я не сплю? Но Стас только что говорил про ключи, да еще и какой-то загадочный сюрприз."
    menu:
        "Пойти с Владой":
            stop music fadeout (1.0)
            play music muslove fadein (0.5)
            "" "Я решил, что упускать такой шанс нельзя! Ключи заберу завтра."
            vlada "Ну так что?"
            mc "Звучит действительно заманчиво! Но только попробуй взять Эдди!"
            vlada "Хаха, не переживай, я Йошимитсу мэйн."
            mc "Ох, от этого не легче..."
            jump vladaHome
        "Пойти обратно в бар":
            "" "Всё хочется попасть домой, да и сюрприз интригует. С Владой мы еще увидимся."
            vlada "Ну так что?"
            mc "Прости, давай в другой раз. Мне только что позвонили, сказали, что ключи нашли. Так что я побегу. Спасибо за компанию."
            vlada "Конечно. Давай, удачи..."
            "" "Влада выглядела расстроенной."
            $ keys = keys + 1
            jump elizabethHome


label vladaHome: # сцена в квартире влады
    scene black
    "" "Мы дошли до дома. Ехать в лифте по какой-то причине было немного неловко. Но вот мы и зашли в квартиру."
    scene room_vlada
    show mc at left with dissolve:
        zoom 1.15
        ypos 1200
    show vlada at right with dissolve:
        zoom 1.15
        ypos 1200
    vlada "Прости за бардак. Минутку."
    hide vlada with dissolve
    "" "Это у кого еще бардак, подумал я, вспоминая свою хату. Она быстренько раскидала пару интересных вещей по шкафам и заправила кровать."
    vlada "Садись-садись. Сейчас принесу похрумкать, подрубай пока плоечку, если хочешь."
    "" "Я и не знал, что такие гики-геймеры существуют. Включив консоль, я увидел количество наигранных часов в некоторых играх и понял... Джекпот."
    show vlada at right with dissolve:
        zoom 1.15
        ypos 1200
    vlada "Так, держи. Ну что погнали?"
    mc "Летс гоооу!"
    "" "По ходу игры, накал страстей становился всё сильнее, а мы становились всё ближе и ближе..."
    stop music fadeout (1.0)
    # мини игра с файтингом
    # jump vlGame
    return

label elGame:
    $ from game.miniGames.RPGGame.main import run_RPG
    return

label vlGame:
    $ from game.miniGames.StreetFighter.StreetFighter1.StreetFighterGame import RunFight
    return






label minigameEllie:
    # $ renpy.call_in_new_context("from game/miniGames/test/main.py import run_game")
    $ from game.miniGames.test.main import run_game
    # $ run_game()
    # jump vladaHome
    return

# label check:
#     if game_finished == True:
#         jump vladaHome


return