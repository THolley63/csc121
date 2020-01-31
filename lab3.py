import arcade

arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.GRAY)

arcade.start_render

#biggest yellow box (outline of soccer field)
arcade.draw_lrtb_rectangle_filled(
    15, 725, 485, 15, arcade.color.YELLOW
)
arcade.draw_lrtb_rectangle_filled(
    20, 720, 480, 20, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    368.5, 372.5, 485, 15, arcade.color.YELLOW
)

#sideline and yard markers in 
# 10 yard increments of football field
arcade.draw_lrtb_rectangle_filled(
    15, 725, 404, 101, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    20, 720, 399, 106, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    70, 670, 399, 106, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    75, 665, 399, 106, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    130, 610, 399, 106, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    135, 605, 399, 106, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    190, 550, 399, 106, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    195, 545, 399, 106, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    250, 490, 399, 106, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    255, 485, 399, 106, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    310, 430, 399, 106, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    315, 425, 399, 106, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    368.5, 372.5, 399, 106, arcade.color.WHITE
)

# middle circle
arcade.draw_circle_outline(
    370, 252.5, 57.5, arcade.color.YELLOW, 5
)

#left yellow box
arcade.draw_lrtb_rectangle_filled(
    15, 108, 378.5, 126.5, arcade.color.YELLOW
)
arcade.draw_lrtb_rectangle_filled(
    15, 103, 373.5, 131.5, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    70, 75, 399, 106, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    15, 20, 399, 106, arcade.color.WHITE
)

#right yellow box
arcade.draw_lrtb_rectangle_filled(
    637, 725, 378.5, 126.5, arcade.color.YELLOW
)
arcade.draw_lrtb_rectangle_filled(
    642, 725, 373.5, 131.5, arcade.color.FOREST_GREEN
)
arcade.draw_lrtb_rectangle_filled(
    665, 670, 399, 106, arcade.color.WHITE
)
arcade.draw_lrtb_rectangle_filled(
    720, 725, 399, 106, arcade.color.WHITE
)

#left goal box (smaller yellow box)
arcade.draw_lrtb_rectangle_filled(
    20, 61, 317.5, 185, arcade.color.YELLOW
)
arcade.draw_lrtb_rectangle_filled(
    20, 56, 312.5, 190, arcade.color.FOREST_GREEN
)

#right goal box (smaller yellow box)
arcade.draw_lrtb_rectangle_filled(
    679, 720, 317.5, 185, arcade.color.YELLOW
)
arcade.draw_lrtb_rectangle_filled(
    684, 720, 312.5, 190, arcade.color.FOREST_GREEN
)

#yellow center-line
arcade.draw_lrtb_rectangle_filled(
    365, 375, 399, 106, arcade.color.YELLOW
)
arcade.draw_lrtb_rectangle_filled(
    368.5, 372.5, 399, 106, arcade.color.WHITE
)



arcade.finish_render()

arcade.run()