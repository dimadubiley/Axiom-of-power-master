init python:

    active_characters = []

    small_char = Transform(
        zoom=1,
        yalign=1.0
    )

    def textbox(n):
        store.tb_id = n

    def swap_char(tag_name, char_array, index, *transforms):

        global active_characters

        # Скрываем предыдущих
        for tag in active_characters:
            if tag != tag_name:
                renpy.hide(tag)

        active_characters = [tag_name]

        # Показываем нового
        renpy.show(
            char_array[index],
            tag=tag_name,
            at_list=list(transforms)
        )

    def show_two_heroes(tag_name, char_array, index, *transforms):

        renpy.show(
            char_array[index],
            tag=tag_name,
            at_list=list(transforms)
        )