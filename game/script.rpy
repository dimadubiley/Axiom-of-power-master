label start:
    default relation_stacey = 0
    default reputation = 0
    
    scene airport: #Двигать фон
        xalign 0.0
        yalign 0.4
        zoom 1.5
        linear 0.5 xalign 0 alpha 1.0
    
    hide main_char
    dictore "Хитроу встретил меня типичным британским гостеприимством:"
    dictore "серым небом и очередями. Перелет из Штатов прошел терпимо,"
    dictore "если не считать легкой турбулентности над Атлантикой."
    dictore "Но это мелочи. Главное испытание впереди: два семестра в Оксфорде по обмену."
    dictore "Из Гарварда — в самую древнюю дыру Англии."

    $ swap_char("gabriela", gabriela_normal_hero, 2, small_char, slide_in_left)
    gab_text "{i}Боже, этот акцент... Он уже сверлит мне мозг."
    gab_text "{i}Надеюсь, местные профессора хотя бы знают, что такое дезодорант,"
    gab_text "{i}в отличие от людей в этой толпе."


    scene taxi_air:
        xalign 0.0
        yalign 0.4
        zoom 1.5
        linear 0.5 xalign 0 alpha 1.0


    dictore "{i}Я вытащила два тяжелых чемодана на тротуар, высматривая кэб."
    dictore "{i}Рядом притормозил черный «Nissan Leaf», стекло медленно опустилось."
    dictore "{i}За рулем сидел мужчина лет сорока с сальной улыбкой."

    $ swap_char("taksist", taksist, 0, small_char, slide_in_right)
    taxi_driver "Эй, красавица! Давай сюда свои баулы. Подброшу с ветерком."

    $ swap_char("gabriela", gabriela_normal_hero, 2, small_char, slide_in_left)
    gab_text "{i}Прекрасно. Поездка не обойдется без дешевого флиртаю."

    scene in_taxi at gentle_sway:
        xalign 0.0
        yalign 0.4
        zoom 1.85
        linear 0.5 xalign 0 alpha 1.0
    
    dictore "Я молча позволила загрузить багаж и нырнула на заднее сиденье,"
    dictore "демонстративно натягивая большие наушники. Всем своим видом она кричала: «Не влезай — убьет»"
    dictore "Машина тронулась. Через пару минут экран телефона вспыхнул."
    dictore "Входящий видеовызов: «Маргошка (Кембридж) 🐍»."

    $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
    gab_text "Ну привет, предательница."
    $ swap_char("margo", margo, 0, small_char, slide_in_right)
    mar_text "И тебе не хворать! Ну, как там на туманном Альбионе?"
    mar_text "Небось, серо, мокро и хочется удавиться?"
    mar_text "А у нас в Кембридже солнце шпарит, завидуй!"
    $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
    gab_text "{i}Марго всегда выражала любовь через подколы. Это был их особый код."
    gab_text "Туманно, но терпимо. Знаешь, есть в этом какой-то вайб... «Сумерек»."
    gab_text "Только без блестящих вампиров."
    
    $ swap_char("margo", margo, 0, small_char, slide_in_right)
    mar_text "О-о-о! А Эдвард с Джейкобом будут?"
    mar_text "Если увидишь бледного красавчика, который смотрит на тебя как на еду"
    mar_text "свистни, я примчусь первым поездом! Ха-ха-ха!"
    
    hide margo
    dictore "(Обе громко смеются)"

    $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
    gab_text "Я еще в дороге. Минут через двадцать буду на месте."
    gab_text "Честно говоря... не знаю, как меня встретят эти британские снобы. "
    gab_text "Гарвард для них — «слишком новомодно»."
    
    $ swap_char("margo", margo, 0, small_char, slide_in_right)
    mar_text "Плевать на снобов. Твоя цель — главный красавчик универа."
    mar_text "Охмури его и разбей сердце во славу американского флага!"

    $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
    gab_text "Больно надо. Эти парни проглатывают половину алфавита,"
    gab_text "когда говорят. Меня этот акцент с ума сведет раньше, чем учеба."

    hide gabriela
    taxi_driver "Таксист бросил на нее презрительный взгляд через зеркало заднего вида."
    $ swap_char("taksist", taksist, 0, small_char, slide_in_right)
    taxi_driver "..."
    taxi_driver "Габи это заметила и лишь закатила глаза."
    
    $ swap_char("margo", margo, 0, small_char, slide_in_right)
    mar_text "Ладно, зануда. Меня Джейдан зовет. Набери, как заселишься в свою келью!"

    hide margo
    dictore "{i}(Звонок завершен)"

    dictore "Я уставилась в окно. "
    dictore "Пейзажи за стеклом сменялись с унылых пригородов на величественные шпили."
    dictore "Оксфорд. Город, где каждый камень дышит историей... и высокомерием. "
    dictore "Примет ли он меня? Или я стану одной из тех, кому выливают суп на голову в столовой,"
    dictore "как в дрянных подростковых сериалах?"
    dictore "{i}Ну уж нет. Я не для того пахала в Гарварде, чтобы здесь быть жертвой"


    scene oks:
        xalign 0.7
        yalign 0.41
        zoom 1.5
        linear 0.5 alpha 1.0

    dictore "Машина остановилась. Я вышла, чувствуя на себе десятки взглядов."
    dictore "Они смотрели на неё не как на человека, а как на экзотического зверька в зоопарке. Или как на грязь."
    
    $ swap_char("taksist", taksist, 0, small_char, slide_in_right)
    taxi_driver "Твои чемоданы, детка. Чаевые оставишь?"
    $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
    gab_text ". . ."

    dictore "Я молча взяла ручки чемоданов и, не удостоив его взглядом, направилась к кампусу."
    dictore "{i}Это место мне уже не нравится. Я чувствую этот запах... Запах старых денег и лицемерия"
    dictore "Внезапно путь мне преградила девушка. Высокая, с модельной фигурой и ногами от ушей. "
    dictore "Её взгляд сканировал Меня, оценивая стоимость каждой вещи на ней."

    $ swap_char("stacey", stacey, 0, small_char, slide_in_right)
    woman_text "Новенькая посреди семестра? Интересно. Кому нужно было отсосать в ректорате, чтобы тебя воткнули на курс?"

    $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)

    menu:
        gab_text "{i}Обычная стерва. Классика жанра."

        "Я смотрю, нахальство — твоя главная черта?":
            jump mode

        "А ты, видимо, эксперт в этом вопросе?":
            jump after_choice

    label mode:
        gab_text "Я смотрю, нахальство — твоя доминирующая черта. С воспитанием в Англии, видимо, совсем беда."
        $ swap_char("stacey", stacey, 0, small_char, slide_in_right)
        woman_text "Зубы мне не заговаривай, серая мышь. Иначе с тобой будут разбираться уже другие."
        $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
        gab_text "«Другие» — это твоя свита из парней, которых ты держишь на поводке про запас?"
        $ swap_char("stacey", stacey, 0, small_char, slide_in_right)
        woman_text "Милочка, тебе такую коллекцию мужчин не собрать даже за две жизни."
        $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
        gab_text "О, поверь, я не горю желанием, чтобы меня имели в три ствола."
        gab_text "Предпочитаю качество, а не количество."
        $ swap_char("stacey", stacey, 0, small_char, slide_in_right)
        woman_text "Я прощу тебе дерзость сегодня. Первый и последний раз."
        woman_text "Спишем на то, что ты просто не знаешь местных правил... пока."
    jump next_scene
    label after_choice:
        $ swap_char("gabriela", gabriela_normal_hero, 1, small_char, slide_in_left)
        gab_text "А ты, видимо, эксперт? Тоже пришлось пройти через этот «ритуал»?"
        $ swap_char("stacey", stacey, 0, small_char, slide_in_right)
        woman_text "Сосать здесь скоро будешь ты, дорогая. И умолять о добавке."
        $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
        gab_text "Прости, я не любительница брать в рот всё, что плохо лежит. Но, судя по твоим губам, у тебя большой опыт."
        $ swap_char("stacey", stacey, 0, small_char, slide_in_right)
        woman_text "Судьба тебя заставит. От неё не убежишь... хи-хи."
        dictore "Стейси грациозно развернулась, взмахнув идеальными волосами,"
        dictore "и, виляя бедрами, направилась к группе своих клонов-подружек."
        $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
        gab_text "Господи... Не успела ступить на порог, а уже вляпалась в местную драму."

    label next_scene:
        pass
    menu:
        dictore "{i}Перед вами выбор комнаты. Это повлияет на атмосферу и ваши характеристики"
        
        "Уютная мансарда (Светлая, с запахом лаванды и мягким пледом)":
            jump peace
        "Готическая спальня (Темное дерево, тяжелые портьеры, свечи)":
            jump bedroom
        "Стильный модерн (Минимализм, дорогие материалы, идеальный порядок)":
            jump modern


    label peace:
        pass
    label bedroom:
        pass
    label modern:
        pass


    dictore ("{i}Резкий скачек во времени")

    $ swap_char("mason", "mason normal", 0, small_char, slide_in_right)
    mas_text "Эй. Кажется, я кое-что нашел."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Я аккуратно прикрыла свою книгу и подалась вперед, скользнув взглядом по раскрытому фолианту."

    dictore "На пожелтевшей странице красовалась гравюра: мужская фигура в балахоне, вокруг которой были расставлены свечи строго по кругу. В центре — какой-то символ, похожий на вытянутую букву «V», пронзенную вертикальной линией."

    dictore "Под гравюрой шел текст на старолатинском. И всего одна строчка на английском, судя по шрифту — уже позднейшая приписка другой рукой:"

    dictore "«Ordo Veri Oculi — Орден Истинного Ока. Оксфорд, 1743 год.»"

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Мурашки поднялись по рукам, хотя в библиотеке было душно."
    gab_text "Истинное Око... Белые закатившиеся зрачки Стейси. Слепота короля из его легенды. Совпадение?

    $ swap_char("mason", "mason normal", 0, small_char, slide_in_right)
    mas_text "Орден основали студенты одного из первых колледжей. Занимались, цитирую: «ритуалами очищения разума и постижением сокрытой истины». Потом официально распустили в 1891-м после какого-то скандала. Подробностей нет."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "«Распустили» — и ты в это веришь?"

    $ swap_char("mason", "mason flirt", 0, small_char, slide_in_right)
    mas_text "Нет. Но на бумаге именно так."

    gab_text "{i}Мы переглянулись."

    menu:
        gab_text "{i}(Спросить про символ или промолчать?)"

        "Ты знаешь этот символ?":
            jump lib_ask_symbol

        "Сделать вид, что не заинтересована.":
            jump lib_stay_cold

    label lib_ask_symbol:
        $ mason_rel += 1

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "Слушай, вот этот знак... — я ткнула пальцем в гравюру. — Ты его где-нибудь видел? Здесь, в Оксфорде?"

        $ swap_char("mason", "mason shok", 0, small_char, slide_in_right)
        mas_text "Почему ты спрашиваешь?"

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Слишком быстро ответил вопросом на вопрос. Интересно."
        gab_text "Статистика. Хочу понять, насколько этот культ актуален сейчас, или это чисто архивная пыль."

        $ swap_char("mason", "mason normal", 0, small_char, slide_in_right)
        mas_text "...Однажды видел. На стене в подсобке нашего студенческого клуба. Решил, что это чья-то художественная самодеятельность."
        mas_text "Теперь уже не уверен."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Сердце пропустило удар. Студенческий клуб. Нужно запомнить."
        gab_text "Какой клуб?"

        $ swap_char("mason", "mason normal", 0, small_char, slide_in_right)
        mas_text "«Meridian». Закрытый дискуссионный клуб. Туда берут только по приглашению."
        mas_text "Стейси там состоит, если тебе интересно.

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Конечно состоит. А кто еще?"

        $ swap_char("mason", "mason sad", 0, small_char, slide_in_right)
        mas_text "Я не знаю всех. Но Боуи... — он осекся. — Неважно. Забудь."

        $ swap_char("gabriela", "gabriela_angry", 0, small_char, slide_in_left)
        gab_text "{i}Вот так вот. Имя — и сразу осекся. Либо боится, либо сам оттуда."
        gab_text "{i}Спрашивать дальше смысла нет. Он закрылся. Пусть пока думает, что я ничего не заметила."

        jump lib_end

    label lib_stay_cold:

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "Понятно. Запишу в таблицу как «нет данных». Бесполезно."

        $ swap_char("mason", "mason normal", 0, small_char, slide_in_right)
        mas_text "Ну и ладно. Может, в соседнем разделе что-то найдешь — там про тайные общества целая полка."

        gab_text "{i}Он встал и молча указал рукой куда-то в глубину зала. Я проследила взглядом. Дальняя секция. Почти без света."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "Там что, специально лампочки не меняют?"

        $ swap_char("mason", "mason flirt", 0, small_char, slide_in_right)
        mas_text "Библиотекари говорят, что там постоянно перегорают. Четыре раза за семестр меняли. Потом просто... перестали."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Чудесно. Типичный Оксфорд."

        jump lib_end

    label lib_end:

    scene kor_u:
        xalign 0.5
        yalign 0.5
        zoom 1.3
        linear 0.4 alpha 1.0

    # [Сцена: Коридор университета — вечер]

    dictore "Мы вышли из библиотеки, когда за узкими стрельчатыми окнами уже стемнело. В коридорах почти никого — только эхо далеких шагов и гул старой вентиляции."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Руки ещё хранили ощущение шершавой бумаги. Ordo Veri Oculi. Это имя теперь не выветрится."

    $ swap_char("mason", "mason normal", 0, small_char, slide_in_right)
    mas_text "Слушай, мне в ту сторону. — Он кивнул в сторону лестничного пролета. — Завтра в кампусе есть?"

    menu:
        gab_text "{i}(Как ответить?)"

        "Буду. — (нейтрально)":
            jump corridor_neutral

        "Зависит от того, зачем. — (интрига)":
            jump corridor_intrigue

    label corridor_neutral:

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "Буду. А что?"

        $ swap_char("mason", "mason normal", 0, small_char, slide_in_right)
        mas_text "Ничего. Просто уточнял."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Непонятный тип. Непонятный — и при этом единственный нормальный человек за весь день. Это либо очень хороший знак, либо очень плохой."

        jump corridor_end

    label corridor_intrigue:
        $ mason_rel += 1

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "Зависит от того, зачем ты спрашиваешь."

        $ swap_char("mason", "mason flirt", 0, small_char, slide_in_right)
        mas_text "Может, хочу убедиться, что тебя не утащили в подвал местные друиды раньше времени."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Усмешка получилась сама собой. Против воли."
        gab_text "Тронута. Буду."

        $ swap_char("mason", "mason smile", 0, small_char, slide_in_right)
        mas_text "Отлично."

        jump corridor_end

    label corridor_end:

    hide mason

    dictore "Он ушел. Я осталась стоять в гулком коридоре одна."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Ordo Veri Oculi. «Meridian». Стейси с белыми глазами и кровью из носа. Боуи — имя, которое Мейсон не решился произнести до конца."
    gab_text "{i}Это уже не паранойя. Это — система. Кто-то тщательно сложил эти кусочки задолго до того, как я сюда приехала."
    gab_text "{i}Вопрос только один: я случайная фигура на этой доске — или меня сюда поставили намеренно?"

    # [Сцена: Комната — ночь]

    scene r1_n:
        xalign 0.5
        yalign 0.5
        zoom 1.3
        linear 0.5 alpha 1.0

    dictore "Комната встретила темнотой и запахом чужого тепла — батарея под окном жарила без остановки. Я бросила сумку на кровать и рухнула рядом, уставившись в потолок."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Телефон молчал. Даже Марго не писала — значит, закопалась в свои кембриджские дела."
    gab_text "{i}Мне бы так. Закопаться. Не думать."

    dictore "Но стоило закрыть глаза — снова этот символ. Вытянутая «V», пронзённая вертикалью. Простой. Почти декоративный. И при этом — старше, чем сам университет."

    $ swap_char("gabriela", "gabriela_sad", 0, small_char, slide_in_left)
    gab_text "{i}Я перевернулась на бок. На тумбочке лежал блокнот — я всегда возила его с собой, ещё с Гарварда. Привычка записывать. Систематизировать. Контролировать хаос."

    dictore "Я открыла чистую страницу и написала три слова:"
    dictore "«Ordo Veri Oculi»"
    dictore "Под ними — стрелки. Имена. Вопросы без ответов."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Кто-то в этом здании знает правду. И рано или поздно я её найду."
    gab_text "{i}А пока — спать. Завтра будет другой день."
    gab_text "{i}Надеюсь."

    dictore "Она выключила свет."

    # [Системное сообщение]

    dictore "📖 Конец главы 1."
    dictore "Ваши показатели:"
    dictore "— Отношения со Стейси: [stacey_rel]"
    dictore "— Отношения с Мейсоном: [mason_rel]"
    dictore "— Репутация Габриэлы: [gabriela_reputation]"

    # ====================================================
    # ГЛАВА 2 — «MERIDIAN»
    # ====================================================

    scene oks:
        xalign 0.5
        yalign 0.4
        zoom 1.4
        linear 0.5 alpha 1.0

    dictore "Утро пришло с дождём. Мелким, упрямым, типично британским."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Я стояла у окна с кружкой холодного кофе и смотрела, как капли расчерчивают стекло косыми линиями."
    gab_text "{i}Ночью почти не спала. Зато блокнот теперь выглядит как доска следователя."

    dictore "Телефон завибрировал. Незнакомый номер."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "— ...Да?"

    dictore "Голос в трубке был тихим. Женским. С намеренно размытой интонацией — ни вопроса, ни утверждения."

    # Неизвестная
    dictore "Голос: — Габриэла Торрес. Добро пожаловать в Оксфорд. Вас ждут сегодня в 20:00. Meridian. Восточное крыло, третий этаж, аудитория без номера. Придите одна."

    $ swap_char("gabriela", "gabriela_surprise", 0, small_char, slide_in_left)
    gab_text "Подождите — кто это?"

    dictore "Гудки."

    $ swap_char("gabriela", "gabriela_angry", 0, small_char, slide_in_left)
    gab_text "{i}Я опустила телефон и медленно выдохнула."
    gab_text "{i}Они вышли на меня первыми. Это либо ловушка, либо приглашение."
    gab_text "{i}Разницы, в общем-то, никакой."

    menu:
        gab_text "{i}(Что делать с этим приглашением?)"

        "Пойти. Это шанс.":
            jump ch2_go
            $ gabriela_reputation += 1

        "Сначала рассказать Мейсону.":
            jump ch2_tell_mason

        "Проигнорировать. Слишком подозрительно.":
            jump ch2_ignore

    label ch2_go:

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Хорошо. Значит, в 20:00."
        gab_text "{i}Мне нужно только одно: не показать страха. Они должны думать, что я иду на их условиях. На самом деле — на своих."

        jump ch2_evening

    label ch2_tell_mason:
        $ mason_rel += 1

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}...Нет. Не буду его втягивать. Ещё не время."
        gab_text "{i}Но знать, что он рядом, было бы неплохо."

        dictore "Я написала ему одно сообщение:"
        dictore "«Вечером буду в восточном крыле. Если не отвечу до 21:00 — ищи меня.»"

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Страховка. Небольшая, но хоть что-то."

        jump ch2_evening

    label ch2_ignore:

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Нет. Слишком топорно. Анонимный звонок, точный адрес, «придите одна» — это либо проверка, либо примитивная провокация."
        gab_text "{i}Я не пойду. Пускай сами найдут способ поговорить по-человечески."

        dictore "Телефон замолчал. День прошёл тихо."
        dictore "Почти слишком тихо."
        dictore "(Сцена ночного визита в Meridian пропущена. Вы получите другую точку входа позже.)"

        jump ch2_next_day

    label ch2_evening:

    scene kor_u:
        xalign 0.5
        yalign 0.5
        zoom 1.3
        linear 0.5 alpha 1.0

    dictore "19:58. Восточное крыло."

    dictore "Коридор здесь был другим — старше, что ли. Стены из тёмного камня, без плакатов и расписаний. Даже воздух другой: плотнее, холоднее."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Третий этаж. Аудитория без номера. Вот она — в конце коридора, за поворотом. Дверь приоткрыта. Из щели — тонкая полоска тёплого света."

    gab_text "{i}Я толкнула дверь."

    scene Kabinet2:
        xalign 0.5
        yalign 0.5
        zoom 1.3
        linear 0.4 alpha 1.0

    dictore "Небольшая аудитория. Старые деревянные кресла, сдвинутые в круг. Несколько свечей на подоконнике — не как декор, а как единственный источник света. Пахло воском и чем-то травяным, едким."

    dictore "В центре круга стояла Стейси."

    dictore "Не та Стейси из коридора с её острым языком и безупречными волосами. Эта выглядела спокойной. Почти безразличной. Руки сложены перед собой, взгляд — прямой, без привычного яда."

    $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
    woman_text "Ты пришла. Это хорошо."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "Была масса причин не приходить."

    $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
    woman_text "Но ты здесь. Значит, правильных причин оказалось больше."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "{i}Она указала на одно из кресел. Я не села."

    $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
    woman_text "Как хочешь. — Пауза. — Ты искала нас в библиотеке. Мы знаем."

    $ swap_char("gabriela", "gabriela_angry", 0, small_char, slide_in_left)
    gab_text "{i}Кровь похолодела. Значит, следили. Или — Мейсон?"
    gab_text "Вы много знаете о том, что меня не касается."

    $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
    woman_text "Касается. Иначе зачем ты листала книгу про Ordo Veri Oculi?"

    dictore "Тишина растянулась на несколько секунд."

    $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
    gab_text "Чего вы хотите?"

    $ swap_char("stacey", "stacey flirt", 0, small_char, slide_in_right)
    woman_text "Предложить тебе ответы. — Она чуть склонила голову. — И кое-что большее."

    menu:
        gab_text "{i}(Как ответить на предложение?)"

        "Какую цену?":
            $ gabriela_reputation += 1
            jump meridian_ask_price

        "Я не продаюсь.":
            jump meridian_refuse

        "Я слушаю. — (осторожно)":
            jump meridian_listen

    label meridian_ask_price:

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "Ответы — это хорошо. Но всё имеет цену. Какую хочешь ты?"

        $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
        woman_text "Умница. Сразу к сути. — Лёгкая улыбка. — Лояльность. Информацию. И одну маленькую услугу, о которой мы поговорим позже."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Размыто. Нарочито. Она не скажет конкретики сейчас — хочет, чтобы я согласилась на туман."
        gab_text "«Позже» — это не условие. Это ловушка."

        $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
        woman_text "Назови это как хочешь. Но ты умная девочка. Ты понимаешь, что в одиночку ты ничего не докажешь. А с нами — возможно всё."

        jump meridian_end

    label meridian_refuse:
        $ stacey_rel -= 1

        $ swap_char("gabriela", "gabriela_angry", 0, small_char, slide_in_left)
        gab_text "Я не продаюсь. И не покупаюсь на красивые слова в комнате со свечами."

        $ swap_char("stacey", "stacey angry", 0, small_char, slide_in_right)
        woman_text "Это не покупка. Это — выбор."

        $ swap_char("gabriela", "gabriela_angry", 0, small_char, slide_in_left)
        gab_text "Отличный. Я выбираю дверь."

        $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
        woman_text "Дверь никуда не денется. — Голос остался ровным. — Но подумай вот о чём: всё, что ты уже видела, — это только верхушка. И без нас ты утонешь, не добравшись до дна."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Я не ответила. Развернулась и вышла."
        gab_text "{i}Шаги звучали слишком громко в пустом коридоре."
        gab_text "{i}Она права насчёт одного: я ничего ещё не видела. Но это не значит, что им можно доверять."

        jump ch2_night

    label meridian_listen:
        $ stacey_rel += 1

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "Я слушаю."

        $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
        woman_text "Ordo Veri Oculi не распался в 1891 году. Он трансформировался. Meridian — это его современная оболочка."
        woman_text "Мы не секта. Мы — структура. У нас есть информация, связи и кое-что ещё. То, чего ни в одной библиотеке не найдёшь."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "А то, что случилось со Стейси — с тобой в коридоре в первый день? Белые глаза, кровь?"

        dictore "Первый раз за весь разговор она моргнула. Быстро. Почти незаметно."

        $ swap_char("stacey", "stacey sad", 0, small_char, slide_in_right)
        woman_text "...Это издержки. Всё под контролем."

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Ложь. Но не грубая. Скорее — тема, в которую она не хочет углубляться."
        gab_text "{i}Запомним."

        jump meridian_end

    label meridian_end:

        $ swap_char("stacey", "stacey normal", 0, small_char, slide_in_right)
        woman_text "Не нужно отвечать сейчас. У тебя есть время до конца недели."
        woman_text "Подумай, Габриэла. Оксфорд — это не просто университет. Это — механизм. И лучше понимать, как он работает, чем однажды попасть под шестерёнки."

        hide stacey

        $ swap_char("gabriela", "gabriela_normal", 0, small_char, slide_in_left)
        gab_text "{i}Она погасила одну из свечей — будто точку поставила."
        gab_text "{i}Я вышла в коридор. Дверь за спиной закрылась беззвучно."

        jump ch2_night

    label ch2_night:

    scene r1_n:
        xalign 0.5
        yalign 0.5
        zoom 1.3
        linear 0.5 alpha 1.0

    # [Сцена: Комната — глубокая ночь]

    dictore "Я открыла блокнот и написала под вчерашними стрелками новое слово:"
    dictore "«Meridian = Ordo Veri Oculi»"
    dictore "И ниже — вопрос, который не давал покоя:"
    dictore "«Почему они вышли на меня сами?»"

    $ swap_char("gabriela", "gabriela_sad", 0, small_char, slide_in_left)
    gab_text "{i}Случайных совпадений больше нет. Значит, я здесь не случайно."
    gab_text "{i}Кто-то привёл меня в Оксфорд. И мне нужно понять — кто и зачем — раньше, чем они решат, что я уже слишком много знаю."

    dictore "За окном дождь наконец прекратился."
    dictore "Город молчал."


    $ swap_char("margo", margo, 0, small_char, slide_in_right)
    mar_text ""
    mar_text ""
    mar_text ""
    $ swap_char("gabriela", gabriela_normal_hero, 0, small_char, slide_in_left)
    gab_text ""
    gab_text ""
    gab_text ""


    $ swap_char("gabriela", gabriela_black, 0, small_char, slide_in_left)
    gab_text "Left"
    $ swap_char("gabriela", gabriela_black, 0, small_char, slide_in_right)
    gab_text "Right"

    $ swap_char("gabriela", gabriela_white, 0, small_char, slide_in_left)
    gab_text "Left"
    $ swap_char("gabriela", gabriela_white, 0, small_char, slide_in_right)
    gab_text "Right"

    $ swap_char("gabriela", gabriela_nacked, 0, small_char, slide_in_left)
    gab_text "Left"
    $ swap_char("gabriela", gabriela_nacked, 0, small_char, slide_in_right)
    gab_text "Right"

    $ swap_char("mason", mason, 0, small_char, slide_in_left)
    mas_text "Left"
    $ swap_char("mason", mason, 0, small_char, slide_in_right)
    mas_text "Right"

    $ swap_char("mason", mason_nacked, 0, small_char, slide_in_left)
    mas_text "Left"
    $ swap_char("mason", mason_nacked, 0, small_char, slide_in_right)
    mas_text "Right"

    $ swap_char("bowie", bowie, 0, small_char, slide_in_left)
    bow_text "Left"
    $ swap_char("bowie", bowie, 0, small_char, slide_in_right)
    bow_text "Right"

    $ swap_char("bowie", bowie_nacked, 0, small_char, slide_in_left)
    bow_text "Left"
    $ swap_char("bowie", bowie_nacked, 0, small_char, slide_in_right)
    bow_text "Right"

    
    $ swap_char("stacey", stacey, 0, small_char, slide_in_left)
    sta_text "Left"
    $ swap_char("stacey", stacey, 0, small_char, slide_in_right)
    sta_text "Right"

    $ swap_char("olivia", olivia, 0, small_char, slide_in_left)
    oli_text "Left"
    $ swap_char("olivia", olivia, 0, small_char, slide_in_right)
    oli_text "Right"

    $ swap_char("margo", margo, 0, small_char, slide_in_left)
    mar_text "Left"
    $ swap_char("margo", margo, 0, small_char, slide_in_right)
    mar_text "Right"

    $ swap_char("taksist", taksist, 0, small_char, slide_in_left)
    taxi_driver "Left"
    $ swap_char("taksist", taksist, 0, small_char, slide_in_right)
    taxi_driver "Right"

    $ swap_char("oficiant", oficiant, 0, small_char, slide_in_left)
    oficiant_text "Left"
    $ swap_char("oficiant", oficiant, 0, small_char, slide_in_right)
    oficiant_text "Right"

    #Выбор
    # menu:
    #     e "Do you wish to view the poem?"

    #     "Yes":
    #         if persistent.allow_vibration:
    #             $ renpy.vibrate(0.2)
    #         jump mode
    #     "No":
    #         if persistent.allow_vibration:
    #             $ renpy.vibrate(0.2)
    #         e "That concludes the quick GUI demonstration."
    #         return

# label mode:

#     menu:
#         e "Do you want to view the poem in NVL mode or ADV mode?"

#         "NVL":
#             if persistent.allow_vibration:
#                 $ renpy.vibrate(0.2)
#             jump nvl_the_raven
#         "ADV":
#             if persistent.allow_vibration:
#                 $ renpy.vibrate(0.2)
#             pass

# label the_raven:

#     $ renpy.notify("ADV mode")

#     menu:
#         "You selected ADV mode"

#         "Continue":
#             pass

#         "Go back":
#             jump mode

#     e "Once upon a midnight dreary, while I pondered, weak and weary,\n"
#     extend "Over many a quaint and curious volume of forgotten lore."
#     e "While I nodded, nearly napping,\n"
#     extend "suddenly there came a tapping,\n"
#     extend "As of some one gently rapping, rapping at my chamber door."
#     e "\"\'Tis some visitor,\" I muttered, \"tapping at my chamber door\n"
#     extend "Only this and nothing more.\""

#     e "Ah, distinctly I remember it was in the bleak December;\n"
#     extend "And each separate dying ember wrought its ghost upon the floor."
#     e "Eagerly I wished the morrow; "
#     extend "vainly I had sought to borrow,\n"
#     extend "From my books surcease of sorrow,{w} sorrow for the lost Lenore."
#     e "For the rare and radiant maiden whom the angels name Lenore."
#     e "Nameless here for evermore."

#     e "And the silken, sad, uncertain rustling of each purple curtain\n"
#     extend "Thrilled me, filled me with fantastic terrors never felt before;\n"
#     e "So that now, to still the beating of my heart, I stood repeating"
#     e "\"\'Tis some visiter entreating entrance at my chamber door.\n"
#     extend "Some late visiter entreating entrance at my chamber door;\n"
#     extend "This it is and nothing more.\""

#     e "Presently my soul grew stronger;\n"
#     extend "hesitating then no longer,"
#     e "\"Sir,\" said I, \"or Madam, truly your forgiveness I implore;"
#     e "But the fact is I was napping, and so gently you came rapping,\n"
#     extend "And so faintly you came tapping, tapping at my chamber door,"
#     e "That I scarce was sure I heard you\"\nhere I opened wide the door;"
#     e "Darkness there and nothing more."

#     e "Deep into that darkness peering, long I stood there wondering, fearing,"
#     e "Doubting, dreaming dreams no mortal ever dared to dream before;"
#     e "But the silence was unbroken, and the stillness gave no token,"
#     e "And the only word there spoken was the whispered word, \"Lenore?\""
#     e "This I whispered, and an echo murmured back the word, \"Lenore!\""
#     e "Merely this and nothing more."

#     e "Back into the chamber turning, all my soul within me burning,"
#     e "Soon again I heard a tapping somewhat louder than before."
#     e "\"Surely,\" said I, \"surely that is something at my window lattice;"
#     e "Let me see, then, what thereat is, and this mystery explore\n"
#     extend "Let my heart be still a moment and this mystery explore;\n"
#     extend "\'Tis the wind and nothing more!\""

#     e "Open here I flung the shutter, when, with many a flirt and flutter,\n"
#     extend "In there stepped a stately Raven of the saintly days of yore;"
#     e "Not the least obeisance made he; not a minute stopped or stayed he;"
#     e "But, with mien of lord or lady, perched above my chamber door\n"
#     extend "Perched upon a bust of Pallas just above my chamber door\n"
#     extend "Perched, and sat, and nothing more."

#     e "Then this ebony bird beguiling my sad fancy into smiling,"
#     e "By the grave and stern decorum of the countenance it wore,"
#     e "\"Though thy crest be shorn and shaven, thou,\" I said, \"art sure no craven,"
#     e "Ghastly grim and ancient Raven wandering from the Nightly shore\n"
#     extend "Tell me what thy lordly name is on the Night\'s Plutonian shore!\""
#     e "Quoth the Raven \"Nevermore.\""

#     e "Much I marvelled this ungainly fowl to hear discourse so plainly,"
#     e "Though its answer little meaning, little relevancy bore;"
#     e "For we cannot help agreeing that no living human being"
#     e "Ever yet was blessed with seeing bird above his chamber door\n"
#     extend "Bird or beast upon the sculptured bust above his chamber door,\n"
#     extend "With such name as \"Nevermore.\""

#     e "But the Raven, sitting lonely on the placid bust, spoke only\n"
#     extend "That one word, as if his soul in that one word he did outpour."
#     e "Nothing farther then he uttered, not a feather then he fluttered,"
#     e "Till I scarcely more than muttered \"Other friends have flown before\n"
#     extend "On the morrow he will leave me, as my Hopes have flown before.\""
#     e "Then the bird said \"Nevermore.\""

#     e "Startled at the stillness broken by reply so aptly spoken,"
#     e "\"Doubtless,\" said I, \"what it utters is its only stock and store"
#     e "Caught from some unhappy master whom unmerciful Disaster"
#     e "Followed fast and followed faster till his songs one burden bore\n"
#     extend "Till the dirges of his Hope that melancholy burden bore\n"
#     extend "Of \'Never, nevermore\'.\""

#     e "But the Raven still beguiling my sad fancy into smiling,"
#     e "Straight I wheeled a cushioned seat in front of bird, and bust and door;"
#     e "Then, upon the velvet sinking, I betook myself to linking"
#     e "Fancy unto fancy, thinking what this ominous bird of yore\n"
#     extend "What this grim, ungainly, ghastly, gaunt, and ominous bird of yore\n"
#     extend "Meant in croaking \"Nevermore.\""

#     e "This I sat engaged in guessing, but no syllable expressing"
#     e "To the fowl whose fiery eyes now burned into my bosom\'s core;"
#     e "This and more I sat divining, with my head at ease reclining"
#     e "On the cushion\'s velvet lining that the lamp-light gloated o\'er,"
#     e "But whose velvet-violet lining with the lamp-light gloating o\'er,"
#     e "She shall press, ah, nevermore!"

#     e "Then, methought, the air grew denser, perfumed from an unseen censer"
#     e "Swung by seraphim whose foot-falls tinkled on the tufted floor."
#     e "\"Wretch,\" I cried, \"thy God hath lent thee, by these angels he hath sent thee"
#     e "Respite, respite and nepenthe, from thy memories of Lenore;"
#     e "Quaff, oh quaff this kind nepenthe and forget this lost Lenore!\""
#     e "Quoth the Raven \"Nevermore.\""

#     e "\"Prophet!\" said I, \"thing of evil!, prophet still, if bird or devil!\n"
#     extend "Whether Tempter sent, or whether tempest tossed thee here ashore,"
#     e "Desolate yet all undaunted, on this desert land enchanted\n"
#     extend "On this home by Horror haunted, tell me truly, I implore"
#     e "Is there, is there balm in Gilead? Tell me, tell me, I implore!\""
#     e "Quoth the Raven \"Nevermore.\""

#     e "\"Prophet!\" said I, \"thing of evil!, prophet still, if bird or devil!"
#     e "By that Heaven that bends above us, by that God we both adore"
#     e "Tell this soul with sorrow laden if, within the distant Aidenn,"
#     e "It shall clasp a sainted maiden whom the angels name Lenore\n"
#     extend "Clasp a rare and radiant maiden whom the angels name Lenore.\""
#     e "Quoth the Raven \"Nevermore.\""

#     e "\"Be that word our sign of parting, bird or fiend!\" I shrieked, upstarting"
#     e "\"Get thee back into the tempest and the Night\'s Plutonian shore!"
#     e "Leave no black plume as a token of that lie thy soul hath spoken!\n"
#     extend "Leave my loneliness unbroken!, quit the bust above my door!"
#     e "Take thy beak from out my heart, and take thy form from off my door!\""
#     e "Quoth the Raven \"Nevermore.\""

#     e "And the Raven, never flitting, still is sitting, still is sitting\n"
#     extend "On the pallid bust of Pallas just above my chamber door;"
#     e "And his eyes have all the seeming of a demon\'s that is dreaming,"
#     e "And the lamp-light o\'er him streaming throws his shadow on the floor;"
#     e "And my soul from out that shadow that lies floating on the floor\n"
#     extend "Shall be lifted, nevermore!"

#     return

# label nvl_the_raven:
#     $ renpy.notify("NVL mode")

#     $ in_nvl = True
#     $ persistent.quick_menu_align = True

#     show screen quick_menu

#     e_nvl "You selected NVL mode"

#     menu (nvl=True):
#         "You selected NVL mode"

#         "Continue":
#             pass

#         "Go back":
#             jump mode

#     e_nvl "Once upon a midnight dreary, while I pondered, weak and weary,"
#     e_nvl "Over many a quaint and curious volume of forgotten lore—"
#     e_nvl "While I nodded, nearly napping, suddenly there came a tapping,"
#     e_nvl "As of some one gently rapping, rapping at my chamber door."
#     e_nvl "\"\'Tis some visitor,\" I muttered, \"tapping at my chamber door—"
#     e_nvl "Only this and nothing more.\""

#     nvl clear

#     e_nvl "Ah, distinctly I remember it was in the bleak December;"
#     e_nvl "And each separate dying ember wrought its ghost upon the floor."
#     e_nvl "Eagerly I wished the morrow;—vainly I had sought to borrow"
#     e_nvl "From my books surcease of sorrow—sorrow for the lost Lenore—"
#     e_nvl "For the rare and radiant maiden whom the angels name Lenore—"
#     e_nvl "Nameless here for evermore."

#     nvl clear

#     e_nvl "And the silken, sad, uncertain rustling of each purple curtain"
#     e_nvl "Thrilled me—filled me with fantastic terrors never felt before;"
#     e_nvl "So that now, to still the beating of my heart, I stood repeating"
#     e_nvl "\"\'Tis some visiter entreating entrance at my chamber door—"
#     e_nvl "Some late visiter entreating entrance at my chamber door;—"
#     e_nvl "This it is and nothing more.\""

#     nvl clear

#     e_nvl "Presently my soul grew stronger; hesitating then no longer,"
#     e_nvl "\"Sir,\" said I, \"or Madam, truly your forgiveness I implore;"
#     e_nvl "But the fact is I was napping, and so gently you came rapping,"
#     e_nvl "And so faintly you came tapping, tapping at my chamber door,"
#     e_nvl "That I scarce was sure I heard you\"—here I opened wide the door;—"
#     e_nvl "Darkness there and nothing more."

#     nvl clear

#     e_nvl "Deep into that darkness peering, long I stood there wondering, fearing,"
#     e_nvl "Doubting, dreaming dreams no mortal ever dared to dream before;"
#     e_nvl "But the silence was unbroken, and the stillness gave no token,"
#     e_nvl "And the only word there spoken was the whispered word, \"Lenore?\""
#     e_nvl "This I whispered, and an echo murmured back the word, \"Lenore!\"—"
#     e_nvl "Merely this and nothing more."

#     nvl clear

#     e_nvl "Back into the chamber turning, all my soul within me burning,"
#     e_nvl "Soon again I heard a tapping somewhat louder than before."
#     e_nvl "\"Surely,\" said I, \"surely that is something at my window lattice;"
#     e_nvl "Let me see, then, what thereat is, and this mystery explore—"
#     e_nvl "Let my heart be still a moment and this mystery explore;—"
#     e_nvl "\'Tis the wind and nothing more!\""

#     nvl clear

#     e_nvl "Open here I flung the shutter, when, with many a flirt and flutter,"
#     e_nvl "In there stepped a stately Raven of the saintly days of yore;"
#     e_nvl "Not the least obeisance made he; not a minute stopped or stayed he;"
#     e_nvl "But, with mien of lord or lady, perched above my chamber door—"
#     e_nvl "Perched upon a bust of Pallas just above my chamber door—"
#     e_nvl "Perched, and sat, and nothing more."

#     nvl clear

#     e_nvl "Then this ebony bird beguiling my sad fancy into smiling,"
#     e_nvl "By the grave and stern decorum of the countenance it wore,"
#     e_nvl "\"Though thy crest be shorn and shaven, thou,\" I said, \"art sure no craven,"
#     e_nvl "Ghastly grim and ancient Raven wandering from the Nightly shore—"
#     e_nvl "Tell me what thy lordly name is on the Night\'s Plutonian shore!\""
#     e_nvl "Quoth the Raven \"Nevermore.\""

#     nvl clear

#     e_nvl "Much I marvelled this ungainly fowl to hear discourse so plainly,"
#     e_nvl "Though its answer little meaning—little relevancy bore;"
#     e_nvl "For we cannot help agreeing that no living human being"
#     e_nvl "Ever yet was blessed with seeing bird above his chamber door—"
#     e_nvl "Bird or beast upon the sculptured bust above his chamber door,"
#     e_nvl "With such name as \"Nevermore.\""

#     nvl clear

#     e_nvl "But the Raven, sitting lonely on the placid bust, spoke only"
#     e_nvl "That one word, as if his soul in that one word he did outpour."
#     e_nvl "Nothing farther then he uttered—not a feather then he fluttered—"
#     e_nvl "Till I scarcely more than muttered \"Other friends have flown before—"
#     e_nvl "On the morrow he will leave me, as my Hopes have flown before.\""
#     e_nvl "Then the bird said \"Nevermore.\""

#     nvl clear

#     e_nvl "Startled at the stillness broken by reply so aptly spoken,"
#     e_nvl "\"Doubtless,\" said I, \"what it utters is its only stock and store"
#     e_nvl "Caught from some unhappy master whom unmerciful Disaster"
#     e_nvl "Followed fast and followed faster till his songs one burden bore—"
#     e_nvl "Till the dirges of his Hope that melancholy burden bore"
#     e_nvl "Of \'Never—nevermore\'.\""

#     nvl clear

#     e_nvl "But the Raven still beguiling my sad fancy into smiling,"
#     e_nvl "Straight I wheeled a cushioned seat in front of bird, and bust and door;"
#     e_nvl "Then, upon the velvet sinking, I betook myself to linking"
#     e_nvl "Fancy unto fancy, thinking what this ominous bird of yore—"
#     e_nvl "What this grim, ungainly, ghastly, gaunt, and ominous bird of yore"
#     e_nvl "Meant in croaking \"Nevermore.\""

#     nvl clear

#     e_nvl "This I sat engaged in guessing, but no syllable expressing"
#     e_nvl "To the fowl whose fiery eyes now burned into my bosom\'s core;"
#     e_nvl "This and more I sat divining, with my head at ease reclining"
#     e_nvl "On the cushion\'s velvet lining that the lamp-light gloated o\'er,"
#     e_nvl "But whose velvet-violet lining with the lamp-light gloating o\'er,"
#     e_nvl "She shall press, ah, nevermore!"

#     nvl clear

#     e_nvl "Then, methought, the air grew denser, perfumed from an unseen censer"
#     e_nvl "Swung by seraphim whose foot-falls tinkled on the tufted floor."
#     e_nvl "\"Wretch,\" I cried, \"thy God hath lent thee—by these angels he hath sent thee"
#     e_nvl "Respite—respite and nepenthe, from thy memories of Lenore;"
#     e_nvl "Quaff, oh quaff this kind nepenthe and forget this lost Lenore!\""
#     e_nvl "Quoth the Raven \"Nevermore.\""

#     nvl clear

#     e_nvl "\"Prophet!\" said I, \"thing of evil!—prophet still, if bird or devil!—"
#     e_nvl "Whether Tempter sent, or whether tempest tossed thee here ashore,"
#     e_nvl "Desolate yet all undaunted, on this desert land enchanted—"
#     e_nvl "On this home by Horror haunted—tell me truly, I implore—"
#     e_nvl "Is there—is there balm in Gilead?—tell me—tell me, I implore!\""
#     e_nvl "Quoth the Raven \"Nevermore.\""

#     nvl clear

#     e_nvl "\"Prophet!\" said I, \"thing of evil!—prophet still, if bird or devil!"
#     e_nvl "By that Heaven that bends above us—by that God we both adore—"
#     e_nvl "Tell this soul with sorrow laden if, within the distant Aidenn,"
#     e_nvl "It shall clasp a sainted maiden whom the angels name Lenore—"
#     e_nvl "Clasp a rare and radiant maiden whom the angels name Lenore.\""
#     e_nvl "Quoth the Raven \"Nevermore.\""

#     nvl clear

#     e_nvl "\"Be that word our sign of parting, bird or fiend!\" I shrieked, upstarting—"
#     e_nvl "\"Get thee back into the tempest and the Night\'s Plutonian shore!"
#     e_nvl "Leave no black plume as a token of that lie thy soul hath spoken!"
#     e_nvl "Leave my loneliness unbroken!—quit the bust above my door!"
#     e_nvl "Take thy beak from out my heart, and take thy form from off my door!\""
#     e_nvl "Quoth the Raven \"Nevermore.\""

#     nvl clear

#     e_nvl "And the Raven, never flitting, still is sitting, still is sitting"
#     e_nvl "On the pallid bust of Pallas just above my chamber door;"
#     e_nvl "And his eyes have all the seeming of a demon\'s that is dreaming,"
#     e_nvl "And the lamp-light o\'er him streaming throws his shadow on the floor;"
#     e_nvl "And my soul from out that shadow that lies floating on the floor"
#     e_nvl "Shall be lifted—nevermore!"

#     return
