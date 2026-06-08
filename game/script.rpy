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
