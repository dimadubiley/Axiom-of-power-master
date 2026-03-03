# GABRIELA
define gab_text = Character("Габриэла", image="к", color="#c2c2c2")
define gab_text_nvl = Character("Габриэла", kind=nvl, image="edgy")
image gabriela_without_smile   = "heroes/Gabriela/Gwithoutsmile.webp"
image gabriela_happy    = "heroes/Gabriela/Normal/Ghappy.webp"
image gabriela_angry    = "heroes/Gabriela/Normal/Gangry.webp"
image gabriela_shy      = "heroes/Gabriela/Normal/shy.webp"
image gabriela_surprise = "heroes/Gabriela/Normal/surprise.webp"
image gabriela_sad      = "heroes/Gabriela/Normal/Gsad.webp" 
image gabriela_normal   = "heroes/Gabriela/Normal/Gnorm.webp"

image gabriela_white_normal = "heroes/Gabriela/White/GWnorm.webp"
image gabriela_white_smile  = "heroes/Gabriela/White/GWsmile.webp"
image gabriela_white_flirt  = "heroes/Gabriela/White/GWflirt.webp"
image gabriela_white_sad    = "heroes/Gabriela/White/GWsad.webp"
image gabriela_white_shok   = "heroes/Gabriela/White/GWshok.webp"
image gabriela_white_angry  = "heroes/Gabriela/White/GWangry.webp"
image gabriela_white_cry    = "heroes/Gabriela/White/GWcry.webp"

image gabriela_black_normal = "heroes/Gabriela/Black/GBnorm.webp"
image gabriela_black_smile  = "heroes/Gabriela/Black/GBsmile.webp"
image gabriela_black_flirt  = "heroes/Gabriela/Black/GBflirt.webp"
image gabriela_black_sad    = "heroes/Gabriela/Black/GBsad.webp"
image gabriela_black_shok   = "heroes/Gabriela/Black/GBshok.webp"
image gabriela_black_angry  = "heroes/Gabriela/Black/GBangry.webp"
image gabriela_black_cry    = "heroes/Gabriela/Black/GBcry.webp"

image gabriela_nacked_flirt = "heroes/Gabriela/Nacked/NackedGflirt.webp"
image gabriela_nacked_sexy  = "heroes/Gabriela/Nacked/NackedGsexy.webp"
image gabriela_nacked_eyes  = "heroes/Gabriela/Nacked/NackedGeyes.webp"
image gabriela_nacked_sad   = "heroes/Gabriela/Nacked/NackedGsad.webp"

# MASON
define mas_text = Character("Мейсон", image="к", color="#c2c2c2")
define mas_text_nvl = Character("Мейсон", kind=nvl, image="edgy")
image mason normal   = "heroes/Mason/Maynorm.webp"
image mason flirt    = "heroes/Mason/Mayflirt.webp"
image mason sad      = "heroes/Mason/Maysad.webp"
image mason smile      = "heroes/Mason/Maysmile.webp"
image mason shok = "heroes/Mason/Mayshok.webp"
image mason angry    = "heroes/Mason/Mangry.webp"

# BOWIE
define bow_text = Character("    Боуи", image="к", color="#c2c2c2")
define bow_text_nvl = Character("Боуи", kind=nvl, image="edgy")
image bowie shok   = "heroes/Bowie/Bshok.webp"
image bowie flirt    = "heroes/Bowie/Bflirt.webp"
image bowie sad      = "heroes/Bowie/Bsad.webp"
image bowie vampire  = "heroes/Bowie/Bvamp.webp"
image bowie angry  = "heroes/Bowie/Bangry.webp"

# DICTORE
define dictore = Character("        . . .", image="к", color="#c2c2c2")
define dictore_nvl = Character("...", kind=nvl, image="edgy")

# STACEY
define sta_text = Character("Стейси", image="к", color="#c2c2c2")
define sta_text_nvl = Character("Стейси", kind=nvl, image="edgy")
image stacey normal = "heroes/Stecey/Snorm.webp"
image stacey flirt = "heroes/Stecey/Sflirt.webp"
image stacey angry = "heroes/Stecey/Sangry.webp"
image stacey cry = "heroes/Stecey/Scry.webp"
image stacey sad = "heroes/Stecey/Ssad.webp"
image stacey shok = "heroes/Stecey/Sshok.webp"
image stacey vampire = "heroes/Stecey/Svamp.webp"

# OLIVIA
define sta_text = Character("Оливия", image="к", color="#c2c2c2")
define sta_text_nvl = Character("Оливия", kind=nvl, image="edgy")
image olivia normal = "heroes/Olivia/Onorm.webp"
image olivia smile = "heroes/Olivia/Osmile.webp"
image olivia angry = "heroes/Olivia/Oangry.webp"
image olivia sad = "heroes/Olivia/Osad.webp"
image olivia flirt = "heroes/Olivia/Oflirt.webp"

# MARGO
define mar_text = Character("Маргошка Бэйби", image="к", color="#c2c2c2")
define mar_text_nvl = Character("Маргошка Бэйби", kind=nvl, image="edgy")
image margo angry = "heroes/Margo/Mangry.webp"
image margo flirt = "heroes/Margo/Mflirt.webp"
image margo normal = "heroes/Margo/Mnormal.webp"
image margo sad = "heroes/Margo/Msad.webp"
image margo shok = "heroes/Margo/Mshok.webp"
image margo strange = "heroes/Margo/Mstrange.webp"

# ТАКСИСТ
define taxi_driver = Character("  Таксист", image="к", color="#c2c2c2")
define taxi_driver_nvl = Character("Таксист", kind=nvl, image="edgy")
image taksist = "heroes/Other/taksist.webp"

# ОФИЦИАНТКА
define oficiant = Character("  Официантка", image="к", color="#c2c2c2")
define oficiant_nvl = Character("Официантка", kind=nvl, image="edgy")
image oficiant = "heroes/Other/Oficiant.webp"

default bg_side = "center"

init python:
    
    gabriela_normal1 = [
        "gabriela_normal",   #0
        "gabriela_happy",    #1
        "gabriela_angry",    #2
        "gabriela_shy",      #3
        "gabriela_surprise", #4
        "gabriela_sad",      #5
    ]

    gabriela_white = [
        "gabriela_white_normal", #0
        "gabriela_white_smile",  #1
        "gabriela_white_flirt",  #2
        "gabriela_white_sad",    #3
        "gabriela_white_shok",   #4
        "gabriela_white_angry",  #5
        "gabriela_white_cry",    #6
    ]

    gabriela_black = [
        "gabriela_black_normal", #0
        "gabriela_black_smile",  #1
        "gabriela_black_flirt",  #2
        "gabriela_black_sad",    #3
        "gabriela_black_shok",   #4
        "gabriela_black_angry",  #5
        "gabriela_black_cry",    #6
    ]
    gabriela_nacked = [
        "gabriela_nacked_flirt", #0
        "gabriela_nacked_sexy",  #1
        "gabriela_nacked_eyes",  #2
        "gabriela_nacked_sad",   #3
    ]

    mason = [
        "mason normal", #0
        "mason flirt",  #1
        "mason sad",    #2
        "mason smile",  #3
        "mason shok",   #4
        "mason angry",  #5
    ]

    bowie = [
        "bowie flirt",   #0
        "bowie shok",    #1
        "bowie sad",     #2
        "bowie vampire", #3
        "bowie angry",   #4
    ]

    stacey = [
        "stacey normal",  #0
        "stacey happy",   #1
        "stacey angry",   #2
        "stacey cry",     #3
        "stacey sad",     #4
        "stacey shok",    #5
        "stacey vampire", #6
    ]

    olivia = [
        "olivia normal", #0
        "olivia smile",  #1
        "olivia angry",  #2
        "olivia sad",    #3
        "olivia flirt",  #4
    ]

    margo = [
        "margo normal",  #0
        "margo sad",     #1
        "margo angry",   #2
        "margo shok",    #3
        "margo strange", #4
        "margo flirt",   #5
    ]

    taksist = [
        "taksist",  #0
    ]

    oficiant = [
        "oficiant",  #0
    ]


    small_char = Transform(
        zoom=0.9,
        yalign=1.0
    )

    def textbox(n):
        store.tb_id = n

    def swap_char(char_array, index, *transforms):

        image_name = char_array[index]

        # Если имя через пробел (mason normal)
        if " " in image_name:
            tag_name = image_name.split()[0]
        # Если имя через подчёркивание (gabriela_black_normal)
        else:
            tag_name = image_name.split("_")[0]

        # Удаляем старого персонажа
        renpy.hide(tag_name)

        # Показываем нового
        renpy.show(
            image_name,
            tag=tag_name,
            at_list=list(transforms)
        )


transform slide_in_left:
    xalign 20.0
    yalign 1.0
    alpha 0.0
    linear 0.5 xalign 12.0 alpha 1.0

transform slide_in_right:
    xalign -20.0
    yalign 1.0
    alpha 0.0
    linear 0.5 xalign -12.0 alpha 1.0

image airport = "gui/BGs/BgAirplaneInside.webp"
image taxi_air = "gui/BGs/BgAirplaneStreet.webp"
image in_taxi = "gui/BGs/BgCar.webp"

image r1_d = "gui/BGs/BgRoom1Day.webp"
image r1_n = "gui/BGs/BgRoom1Night.webp"

image r2_d = "gui/BGs/BgRoom2Day.webp"
image r2_n = "gui/BGs/BgRoom2Night.webp"

image r3_d = "gui/BGs/BgRoom3Day.webp"
image r3_n = "gui/BGs/BgRoom3Night.webp"

image cl = "gui/BGs/BgClass.webp"
image dv = "gui/BGs/BgDvor.webp"

image kor_c = "gui/BGs/BgKoridorCampus.webp"
image kor_u = "gui/BGs/BgKoridorUniv.webp"
image oks = "gui/BGs/BgOksford.webp"

label start:

    scene airport: #Двигать фон
        xalign 0.0
        yalign 0.4
        zoom 1.5
        linear 0.5 xalign 0 alpha 1.0

    # show gabriela normal
    
    $ swap_char("gabriela", gabriela_black, 0, small_char, slide_in_right)
    gab_text "Test1"

    $ swap_char("gabriela", gabriela_normal, 0, small_char, slide_in_left)
    gab_text "Test2"

    $ swap_char("mason", mason, 0, small_char, slide_in_right)
    mas_text "Test3"

    hide main_char
    dictore "Хитроу встретил меня типичным британским гостеприимством:"
    dictore "серым небом и очередями. Перелет из Штатов прошел терпимо,"
    dictore "если не считать легкой турбулентности над Атлантикой. Но это мелочи."
    dictore "Главное испытание впереди: два семестра в Оксфорде по обмену."
    dictore "Из Гарварда — в самую древнюю дыру Англии."

    $ swap_char(gabriela, 2, small_char, slide_in_left)
    gab_text "{i}Боже, этот акцент... Он уже сверлит мне мозг.{/i}"
    gab_text "{i}Надеюсь, местные профессора хотя бы знают, что такое дезодорант, в отличие от людей в этой толпе.{/i}"

    scene taxi_air
    dictore "Я вытащила два тяжелых чемодана на тротуар, высматривая кэб."
    dictore "Рядом притормозил черный «Nissan Leaf», стекло медленно опустилось."
    dictore "За рулем сидел мужчина лет сорока с сальной улыбкой."

    $ swap_char(taksist, 0, small_char, slide_in_right)
    taxi_driver "Эй, красавица! Давай сюда свои баулы. Подброшу с ветерком."

    $ swap_char(gabriela, 0, small_char, slide_in_left)
    gab_text "{i}Прекрасно. Поездка не обойдется без дешевого флирта{/i}"

    scene in_taxi
    dictore "Я молча позволила загрузить багаж и нырнула на заднее сиденье,"
    dictore "демонстративно натягивая большие наушники."
    dictore "Всем своим видом она кричала: «Не влезай — убьет». Машина тронулась."
    dictore "Через пару минут экран телефона вспыхнул."
    dictore "Входящий видеовызов: «Маргошка Бейби»."



    # $ swap_char(mason, 1, small_char)
    # mas_text "Я знаю"

    # $ swap_char(bowie, 3, small_char)
    # bow_text "А я вампир"

    # $ swap_char(bowie, 0, small_char)
    # bow_text "Ну тут прям очень огромный текст что не могу. Он создан чисто для проверки как себя поведет прям очень огромный текст. Проверка длинного слова танаталогия"

    #Выбор
    menu:
        e "Do you wish to view the poem?"

        "Yes":
            if persistent.allow_vibration:
                $ renpy.vibrate(0.2)
            jump mode
        "No":
            if persistent.allow_vibration:
                $ renpy.vibrate(0.2)
            e "That concludes the quick GUI demonstration."
            return

label mode:

    menu:
        e "Do you want to view the poem in NVL mode or ADV mode?"

        "NVL":
            if persistent.allow_vibration:
                $ renpy.vibrate(0.2)
            jump nvl_the_raven
        "ADV":
            if persistent.allow_vibration:
                $ renpy.vibrate(0.2)
            pass

label the_raven:

    $ renpy.notify("ADV mode")

    menu:
        "You selected ADV mode"

        "Continue":
            pass

        "Go back":
            jump mode

    e "Once upon a midnight dreary, while I pondered, weak and weary,\n"
    extend "Over many a quaint and curious volume of forgotten lore."
    e "While I nodded, nearly napping,\n"
    extend "suddenly there came a tapping,\n"
    extend "As of some one gently rapping, rapping at my chamber door."
    e "\"\'Tis some visitor,\" I muttered, \"tapping at my chamber door\n"
    extend "Only this and nothing more.\""

    e "Ah, distinctly I remember it was in the bleak December;\n"
    extend "And each separate dying ember wrought its ghost upon the floor."
    e "Eagerly I wished the morrow; "
    extend "vainly I had sought to borrow,\n"
    extend "From my books surcease of sorrow,{w} sorrow for the lost Lenore."
    e "For the rare and radiant maiden whom the angels name Lenore."
    e "Nameless here for evermore."

    e "And the silken, sad, uncertain rustling of each purple curtain\n"
    extend "Thrilled me, filled me with fantastic terrors never felt before;\n"
    e "So that now, to still the beating of my heart, I stood repeating"
    e "\"\'Tis some visiter entreating entrance at my chamber door.\n"
    extend "Some late visiter entreating entrance at my chamber door;\n"
    extend "This it is and nothing more.\""

    e "Presently my soul grew stronger;\n"
    extend "hesitating then no longer,"
    e "\"Sir,\" said I, \"or Madam, truly your forgiveness I implore;"
    e "But the fact is I was napping, and so gently you came rapping,\n"
    extend "And so faintly you came tapping, tapping at my chamber door,"
    e "That I scarce was sure I heard you\"\nhere I opened wide the door;"
    e "Darkness there and nothing more."

    e "Deep into that darkness peering, long I stood there wondering, fearing,"
    e "Doubting, dreaming dreams no mortal ever dared to dream before;"
    e "But the silence was unbroken, and the stillness gave no token,"
    e "And the only word there spoken was the whispered word, \"Lenore?\""
    e "This I whispered, and an echo murmured back the word, \"Lenore!\""
    e "Merely this and nothing more."

    e "Back into the chamber turning, all my soul within me burning,"
    e "Soon again I heard a tapping somewhat louder than before."
    e "\"Surely,\" said I, \"surely that is something at my window lattice;"
    e "Let me see, then, what thereat is, and this mystery explore\n"
    extend "Let my heart be still a moment and this mystery explore;\n"
    extend "\'Tis the wind and nothing more!\""

    e "Open here I flung the shutter, when, with many a flirt and flutter,\n"
    extend "In there stepped a stately Raven of the saintly days of yore;"
    e "Not the least obeisance made he; not a minute stopped or stayed he;"
    e "But, with mien of lord or lady, perched above my chamber door\n"
    extend "Perched upon a bust of Pallas just above my chamber door\n"
    extend "Perched, and sat, and nothing more."

    e "Then this ebony bird beguiling my sad fancy into smiling,"
    e "By the grave and stern decorum of the countenance it wore,"
    e "\"Though thy crest be shorn and shaven, thou,\" I said, \"art sure no craven,"
    e "Ghastly grim and ancient Raven wandering from the Nightly shore\n"
    extend "Tell me what thy lordly name is on the Night\'s Plutonian shore!\""
    e "Quoth the Raven \"Nevermore.\""

    e "Much I marvelled this ungainly fowl to hear discourse so plainly,"
    e "Though its answer little meaning, little relevancy bore;"
    e "For we cannot help agreeing that no living human being"
    e "Ever yet was blessed with seeing bird above his chamber door\n"
    extend "Bird or beast upon the sculptured bust above his chamber door,\n"
    extend "With such name as \"Nevermore.\""

    e "But the Raven, sitting lonely on the placid bust, spoke only\n"
    extend "That one word, as if his soul in that one word he did outpour."
    e "Nothing farther then he uttered, not a feather then he fluttered,"
    e "Till I scarcely more than muttered \"Other friends have flown before\n"
    extend "On the morrow he will leave me, as my Hopes have flown before.\""
    e "Then the bird said \"Nevermore.\""

    e "Startled at the stillness broken by reply so aptly spoken,"
    e "\"Doubtless,\" said I, \"what it utters is its only stock and store"
    e "Caught from some unhappy master whom unmerciful Disaster"
    e "Followed fast and followed faster till his songs one burden bore\n"
    extend "Till the dirges of his Hope that melancholy burden bore\n"
    extend "Of \'Never, nevermore\'.\""

    e "But the Raven still beguiling my sad fancy into smiling,"
    e "Straight I wheeled a cushioned seat in front of bird, and bust and door;"
    e "Then, upon the velvet sinking, I betook myself to linking"
    e "Fancy unto fancy, thinking what this ominous bird of yore\n"
    extend "What this grim, ungainly, ghastly, gaunt, and ominous bird of yore\n"
    extend "Meant in croaking \"Nevermore.\""

    e "This I sat engaged in guessing, but no syllable expressing"
    e "To the fowl whose fiery eyes now burned into my bosom\'s core;"
    e "This and more I sat divining, with my head at ease reclining"
    e "On the cushion\'s velvet lining that the lamp-light gloated o\'er,"
    e "But whose velvet-violet lining with the lamp-light gloating o\'er,"
    e "She shall press, ah, nevermore!"

    e "Then, methought, the air grew denser, perfumed from an unseen censer"
    e "Swung by seraphim whose foot-falls tinkled on the tufted floor."
    e "\"Wretch,\" I cried, \"thy God hath lent thee, by these angels he hath sent thee"
    e "Respite, respite and nepenthe, from thy memories of Lenore;"
    e "Quaff, oh quaff this kind nepenthe and forget this lost Lenore!\""
    e "Quoth the Raven \"Nevermore.\""

    e "\"Prophet!\" said I, \"thing of evil!, prophet still, if bird or devil!\n"
    extend "Whether Tempter sent, or whether tempest tossed thee here ashore,"
    e "Desolate yet all undaunted, on this desert land enchanted\n"
    extend "On this home by Horror haunted, tell me truly, I implore"
    e "Is there, is there balm in Gilead? Tell me, tell me, I implore!\""
    e "Quoth the Raven \"Nevermore.\""

    e "\"Prophet!\" said I, \"thing of evil!, prophet still, if bird or devil!"
    e "By that Heaven that bends above us, by that God we both adore"
    e "Tell this soul with sorrow laden if, within the distant Aidenn,"
    e "It shall clasp a sainted maiden whom the angels name Lenore\n"
    extend "Clasp a rare and radiant maiden whom the angels name Lenore.\""
    e "Quoth the Raven \"Nevermore.\""

    e "\"Be that word our sign of parting, bird or fiend!\" I shrieked, upstarting"
    e "\"Get thee back into the tempest and the Night\'s Plutonian shore!"
    e "Leave no black plume as a token of that lie thy soul hath spoken!\n"
    extend "Leave my loneliness unbroken!, quit the bust above my door!"
    e "Take thy beak from out my heart, and take thy form from off my door!\""
    e "Quoth the Raven \"Nevermore.\""

    e "And the Raven, never flitting, still is sitting, still is sitting\n"
    extend "On the pallid bust of Pallas just above my chamber door;"
    e "And his eyes have all the seeming of a demon\'s that is dreaming,"
    e "And the lamp-light o\'er him streaming throws his shadow on the floor;"
    e "And my soul from out that shadow that lies floating on the floor\n"
    extend "Shall be lifted, nevermore!"

    return

label nvl_the_raven:
    $ renpy.notify("NVL mode")

    $ in_nvl = True
    $ persistent.quick_menu_align = True

    show screen quick_menu

    e_nvl "You selected NVL mode"

    menu (nvl=True):
        "You selected NVL mode"

        "Continue":
            pass

        "Go back":
            jump mode

    e_nvl "Once upon a midnight dreary, while I pondered, weak and weary,"
    e_nvl "Over many a quaint and curious volume of forgotten lore—"
    e_nvl "While I nodded, nearly napping, suddenly there came a tapping,"
    e_nvl "As of some one gently rapping, rapping at my chamber door."
    e_nvl "\"\'Tis some visitor,\" I muttered, \"tapping at my chamber door—"
    e_nvl "Only this and nothing more.\""

    nvl clear

    e_nvl "Ah, distinctly I remember it was in the bleak December;"
    e_nvl "And each separate dying ember wrought its ghost upon the floor."
    e_nvl "Eagerly I wished the morrow;—vainly I had sought to borrow"
    e_nvl "From my books surcease of sorrow—sorrow for the lost Lenore—"
    e_nvl "For the rare and radiant maiden whom the angels name Lenore—"
    e_nvl "Nameless here for evermore."

    nvl clear

    e_nvl "And the silken, sad, uncertain rustling of each purple curtain"
    e_nvl "Thrilled me—filled me with fantastic terrors never felt before;"
    e_nvl "So that now, to still the beating of my heart, I stood repeating"
    e_nvl "\"\'Tis some visiter entreating entrance at my chamber door—"
    e_nvl "Some late visiter entreating entrance at my chamber door;—"
    e_nvl "This it is and nothing more.\""

    nvl clear

    e_nvl "Presently my soul grew stronger; hesitating then no longer,"
    e_nvl "\"Sir,\" said I, \"or Madam, truly your forgiveness I implore;"
    e_nvl "But the fact is I was napping, and so gently you came rapping,"
    e_nvl "And so faintly you came tapping, tapping at my chamber door,"
    e_nvl "That I scarce was sure I heard you\"—here I opened wide the door;—"
    e_nvl "Darkness there and nothing more."

    nvl clear

    e_nvl "Deep into that darkness peering, long I stood there wondering, fearing,"
    e_nvl "Doubting, dreaming dreams no mortal ever dared to dream before;"
    e_nvl "But the silence was unbroken, and the stillness gave no token,"
    e_nvl "And the only word there spoken was the whispered word, \"Lenore?\""
    e_nvl "This I whispered, and an echo murmured back the word, \"Lenore!\"—"
    e_nvl "Merely this and nothing more."

    nvl clear

    e_nvl "Back into the chamber turning, all my soul within me burning,"
    e_nvl "Soon again I heard a tapping somewhat louder than before."
    e_nvl "\"Surely,\" said I, \"surely that is something at my window lattice;"
    e_nvl "Let me see, then, what thereat is, and this mystery explore—"
    e_nvl "Let my heart be still a moment and this mystery explore;—"
    e_nvl "\'Tis the wind and nothing more!\""

    nvl clear

    e_nvl "Open here I flung the shutter, when, with many a flirt and flutter,"
    e_nvl "In there stepped a stately Raven of the saintly days of yore;"
    e_nvl "Not the least obeisance made he; not a minute stopped or stayed he;"
    e_nvl "But, with mien of lord or lady, perched above my chamber door—"
    e_nvl "Perched upon a bust of Pallas just above my chamber door—"
    e_nvl "Perched, and sat, and nothing more."

    nvl clear

    e_nvl "Then this ebony bird beguiling my sad fancy into smiling,"
    e_nvl "By the grave and stern decorum of the countenance it wore,"
    e_nvl "\"Though thy crest be shorn and shaven, thou,\" I said, \"art sure no craven,"
    e_nvl "Ghastly grim and ancient Raven wandering from the Nightly shore—"
    e_nvl "Tell me what thy lordly name is on the Night\'s Plutonian shore!\""
    e_nvl "Quoth the Raven \"Nevermore.\""

    nvl clear

    e_nvl "Much I marvelled this ungainly fowl to hear discourse so plainly,"
    e_nvl "Though its answer little meaning—little relevancy bore;"
    e_nvl "For we cannot help agreeing that no living human being"
    e_nvl "Ever yet was blessed with seeing bird above his chamber door—"
    e_nvl "Bird or beast upon the sculptured bust above his chamber door,"
    e_nvl "With such name as \"Nevermore.\""

    nvl clear

    e_nvl "But the Raven, sitting lonely on the placid bust, spoke only"
    e_nvl "That one word, as if his soul in that one word he did outpour."
    e_nvl "Nothing farther then he uttered—not a feather then he fluttered—"
    e_nvl "Till I scarcely more than muttered \"Other friends have flown before—"
    e_nvl "On the morrow he will leave me, as my Hopes have flown before.\""
    e_nvl "Then the bird said \"Nevermore.\""

    nvl clear

    e_nvl "Startled at the stillness broken by reply so aptly spoken,"
    e_nvl "\"Doubtless,\" said I, \"what it utters is its only stock and store"
    e_nvl "Caught from some unhappy master whom unmerciful Disaster"
    e_nvl "Followed fast and followed faster till his songs one burden bore—"
    e_nvl "Till the dirges of his Hope that melancholy burden bore"
    e_nvl "Of \'Never—nevermore\'.\""

    nvl clear

    e_nvl "But the Raven still beguiling my sad fancy into smiling,"
    e_nvl "Straight I wheeled a cushioned seat in front of bird, and bust and door;"
    e_nvl "Then, upon the velvet sinking, I betook myself to linking"
    e_nvl "Fancy unto fancy, thinking what this ominous bird of yore—"
    e_nvl "What this grim, ungainly, ghastly, gaunt, and ominous bird of yore"
    e_nvl "Meant in croaking \"Nevermore.\""

    nvl clear

    e_nvl "This I sat engaged in guessing, but no syllable expressing"
    e_nvl "To the fowl whose fiery eyes now burned into my bosom\'s core;"
    e_nvl "This and more I sat divining, with my head at ease reclining"
    e_nvl "On the cushion\'s velvet lining that the lamp-light gloated o\'er,"
    e_nvl "But whose velvet-violet lining with the lamp-light gloating o\'er,"
    e_nvl "She shall press, ah, nevermore!"

    nvl clear

    e_nvl "Then, methought, the air grew denser, perfumed from an unseen censer"
    e_nvl "Swung by seraphim whose foot-falls tinkled on the tufted floor."
    e_nvl "\"Wretch,\" I cried, \"thy God hath lent thee—by these angels he hath sent thee"
    e_nvl "Respite—respite and nepenthe, from thy memories of Lenore;"
    e_nvl "Quaff, oh quaff this kind nepenthe and forget this lost Lenore!\""
    e_nvl "Quoth the Raven \"Nevermore.\""

    nvl clear

    e_nvl "\"Prophet!\" said I, \"thing of evil!—prophet still, if bird or devil!—"
    e_nvl "Whether Tempter sent, or whether tempest tossed thee here ashore,"
    e_nvl "Desolate yet all undaunted, on this desert land enchanted—"
    e_nvl "On this home by Horror haunted—tell me truly, I implore—"
    e_nvl "Is there—is there balm in Gilead?—tell me—tell me, I implore!\""
    e_nvl "Quoth the Raven \"Nevermore.\""

    nvl clear

    e_nvl "\"Prophet!\" said I, \"thing of evil!—prophet still, if bird or devil!"
    e_nvl "By that Heaven that bends above us—by that God we both adore—"
    e_nvl "Tell this soul with sorrow laden if, within the distant Aidenn,"
    e_nvl "It shall clasp a sainted maiden whom the angels name Lenore—"
    e_nvl "Clasp a rare and radiant maiden whom the angels name Lenore.\""
    e_nvl "Quoth the Raven \"Nevermore.\""

    nvl clear

    e_nvl "\"Be that word our sign of parting, bird or fiend!\" I shrieked, upstarting—"
    e_nvl "\"Get thee back into the tempest and the Night\'s Plutonian shore!"
    e_nvl "Leave no black plume as a token of that lie thy soul hath spoken!"
    e_nvl "Leave my loneliness unbroken!—quit the bust above my door!"
    e_nvl "Take thy beak from out my heart, and take thy form from off my door!\""
    e_nvl "Quoth the Raven \"Nevermore.\""

    nvl clear

    e_nvl "And the Raven, never flitting, still is sitting, still is sitting"
    e_nvl "On the pallid bust of Pallas just above my chamber door;"
    e_nvl "And his eyes have all the seeming of a demon\'s that is dreaming,"
    e_nvl "And the lamp-light o\'er him streaming throws his shadow on the floor;"
    e_nvl "And my soul from out that shadow that lies floating on the floor"
    e_nvl "Shall be lifted—nevermore!"

    return
