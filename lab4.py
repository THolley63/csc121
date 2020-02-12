import arcade

SCREEN_WIDTH = 740
SCREEN_HEIGHT = 500


def draw_soccer_field():
    #outline of soccer field (bigger yellow box)

    arcade.draw_lrtb_rectangle_filled(
        15, 725, 485, 15, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        20, 720, 480, 20, arcade.color.FOREST_GREEN
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     20, 720, 445.5, 443.5, arcade.color.WHITE
    # )
    # arcade.draw_lrtb_rectangle_filled(
    #     20, 720, 59.5, 57.5, arcade.color.WHITE
    # )
    arcade.draw_lrtb_rectangle_filled(
        368.5, 372.5, 485, 15, arcade.color.YELLOW
    )

    draw_left_yellow_box()
    draw_left_goal_box()
    draw_right_yellow_box()
    draw_right_goal_box()
    draw_left_center_line()
    draw_middle_circle()

def draw_left_center_line():
    #yellow center-line

    arcade.draw_lrtb_rectangle_filled(
        365, 375, 399, 106, arcade.color.YELLOW
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     368.5, 372.5, 399, 106, arcade.color.WHITE
    # )


def draw_middle_circle():
    # middle circle

    arcade.draw_circle_outline(
        369.5, 252.5, 57.5, arcade.color.YELLOW, 5
    )

def draw_left_yellow_box():
    #left yellow box

    arcade.draw_lrtb_rectangle_filled(
        15, 123, 378.5, 126.5, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        15, 118, 373.5, 131.5, arcade.color.FOREST_GREEN
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     15, 20, 399, 106, arcade.color.WHITE
    # )
    # arcade.draw_lrtb_rectangle_filled(
    #     102.5, 105, 399, 106, arcade.color.WHITE
    # )

def draw_right_yellow_box():
    #right yellow box

    arcade.draw_lrtb_rectangle_filled(
        617, 725, 378.5, 126.5, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        622, 725, 373.5, 131.5, arcade.color.FOREST_GREEN
    )
    # arcade.draw_lrtb_rectangle_filled(
    #     720, 725, 399, 106, arcade.color.WHITE
    # )
    # arcade.draw_lrtb_rectangle_filled(
    #     637.5, 640, 399, 106, arcade.color.WHITE
    # )

def draw_left_goal_box():
    #left goal box (smaller yellow box)

    arcade.draw_lrtb_rectangle_filled(
        20, 61, 317.5, 185, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        20, 56, 312.5, 190, arcade.color.FOREST_GREEN
    )

def draw_right_goal_box():
    #right goal box (smaller yellow box)

    arcade.draw_lrtb_rectangle_filled(
        679, 720, 317.5, 185, arcade.color.YELLOW
    )
    arcade.draw_lrtb_rectangle_filled(
        684, 720, 312.5, 190, arcade.color.FOREST_GREEN
    )

def draw_football_field():
    # sideline and yard markers of football field in 10 yard
    # increments

    arcade.draw_lrtb_rectangle_filled(
        15, 725, 409, 97, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        223, 520, 423, 82, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        222.5, 225, 480, 20, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        517.5, 520, 480, 20, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        20, 720, 399, 106, arcade.color.FOREST_GREEN
    )
    arcade.draw_lrtb_rectangle_filled(
        15, 20, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        102.5, 105, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        130, 135, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        162.5, 165, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        190, 195, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        222.5, 225, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        250, 255, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        282.5, 285, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        310, 315, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        342.5, 345, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        368.5, 372.5, 404, 101, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        400, 402.5, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        425, 430, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        457.5, 460, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        485, 490, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        517.5, 520, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        545, 550, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        577.5, 580, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        605, 610, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        637.5, 640, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        70, 75, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        665, 670, 399, 106, arcade.color.WHITE
    )
    arcade.draw_lrtb_rectangle_filled(
        720, 725, 399, 106, arcade.color.WHITE
    )


def draw_defense(x):
    """Draw the defense"""
    #defense (represented as "x")

    draw_defensive_tackle_x(x)
    draw_defensive_ends_x(x)
    draw_outside_linebacker_1(x,y)
    draw_outside_linebacker_2(x,y)
    draw_inside_linebacker_1(x,y)
    draw_inside_linebacker_2(x,y)
    draw_cornerback_1(x,y)
    draw_cornerback_2(x,y)
    draw_safety_1(x,y)
    draw_safety_2(x,y)

def draw_defensive_tackle_x(x):    
    #defensive line
    arcade.draw_text(
        "x",
        438 + x, 250, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_defensive_ends_x(x):
    arcade.draw_text(
        "x",
        438 + x, 290, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "x",
        438 + x, 210, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_outside_linebacker_1(x,y):
    arcade.draw_text(
        "x",
        420 + x, 320 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
def draw_outside_linebacker_2(x,y):
    arcade.draw_text(
        "x",
        420 + x, 180 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
def draw_inside_linebacker_1(x,y):
    arcade.draw_text(
        "x",
        408 + x, 225 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
def draw_inside_linebacker_2(x,y):
    arcade.draw_text(
        "x",
        408 + x, 275 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    
def draw_cornerback_1(x,y):
    #cornerback
    arcade.draw_text(
        "x",
        428 + x, 140 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_cornerback_2(x,y):
    arcade.draw_text(
        "x",
        428 + x, 370 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_safety_1(x,y):
    #safeties
    arcade.draw_text(
        "x",
        380 + x, 215 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_safety_2(x,y):
    arcade.draw_text(
        "x",
        380 + x, 285 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )


def draw_offense(x):
    """Draw the offense"""
    #offense (represented as "o")

    draw_offensive_linemen(x)
    draw_tight_end(x,y)
    draw_quarterback(x)
    draw_running_back(x,y)
    draw_fullback(x)
    draw_wide_reciever_1(x,y)
    draw_wide_reciever_2(x,y)

def draw_offensive_linemen(x):
    #offensive linemen
    arcade.draw_text(
        "o",
        455 + x, 250, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        458.75 + x, 270, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        462 + x, 290, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        458.75 + x, 230, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    arcade.draw_text(
        "o",
        462 + x, 210, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_tight_end(x,y):
    arcade.draw_text(
        "o",
        462 + x, 190 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

    

def draw_quarterback(x,y):
    #Quarterback
    arcade.draw_text(
        "o",
        490 + x, 250 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )

def draw_running_back(x,y):
    #Running back
    arcade.draw_text(
        "o",
        495 + x, 270 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )
    
def draw_fullback(x,y):
    #Full back
    arcade.draw_text(
        "o",
        495 + x, 230 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )


def draw_wide_reciever_1(x,y):
    #Wide Recievers
    arcade.draw_text(
        "o",
        473 + x, 140 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )


def draw_wide_reciever_2(x,y):    
    arcade.draw_text(
        "o",
        462 + x, 370 + y, arcade.color.RED, 25, width=200, align="center",
        anchor_x="center", anchor_y="center"
    )



def on_draw(delta_time):
    # Modify the defense x



    
    arcade.start_render()

    # draw_soccer_field()
    draw_football_field()

    draw_defensive_tackle_x(on_draw.defensive_tackle_x)
    draw_defensive_ends_x(on_draw.defensive_ends_x)
    draw_outside_linebacker_1(on_draw.olb_1_x,on_draw.olb_1_y)
    draw_outside_linebacker_2(on_draw.olb_2_x,on_draw.olb_2_y)
    draw_inside_linebacker_1(on_draw.ilb_1_x,on_draw.ilb_1_y)
    draw_inside_linebacker_2(on_draw.ilb_2_x,on_draw.ilb_2_y)
    draw_cornerback_1(on_draw.cb_1_x,on_draw.cb_1_y)
    draw_cornerback_2(on_draw.cb_2_x,on_draw.cb_2_y)
    draw_safety_1(on_draw.sf_1_x,on_draw.sf_1_y)
    draw_safety_2(on_draw.sf_2_x,on_draw.sf_2_y)


    on_draw.defensive_tackle_x += .3
    on_draw.defensive_ends_x += .4
    on_draw.olb_1_x += .75
    on_draw.olb_1_y += .75
    on_draw.olb_2_x += 1.5
    on_draw.olb_2_y += .5
    on_draw.ilb_1_x += -.5
    on_draw.ilb_1_y += 1.75
    on_draw.ilb_2_x += -.5
    on_draw.ilb_2_y += 2
    on_draw.cb_1_x += -3.5
    on_draw.cb_1_y += 2
    on_draw.cb_2_x += -4
    on_draw.cb_2_y += .05
    on_draw.sf_1_x += -3
    on_draw.sf_1_y += 1
    on_draw.sf_2_x += -3.5
    on_draw.sf_2_y += 1.5

    draw_offensive_linemen(on_draw.offensive_linemen_x)
    draw_tight_end(on_draw.tight_end_x,on_draw.tight_end_y)
    draw_quarterback(on_draw.quarterback_x,on_draw.quarterback_y)
    draw_running_back(on_draw.running_back_x,on_draw.running_back_y)
    draw_fullback(on_draw.fullback_x,on_draw.fullback_y)
    draw_wide_reciever_1(on_draw.wide_reciever_1_x,on_draw.wide_reciever_1_y)
    draw_wide_reciever_2(on_draw.wide_reciever_2_x,on_draw.wide_reciever_2_y)

    on_draw.offensive_linemen_x += .25
    on_draw.tight_end_x += -2
    on_draw.tight_end_y += 3
    on_draw.quarterback_x += .4
    on_draw.quarterback_y += .4
    on_draw.running_back_x += -.75
    on_draw.running_back_y += 2
    on_draw.fullback_x += .35
    on_draw.fullback_y += -.15
    on_draw.wide_reciever_1_x += -5
    on_draw.wide_reciever_1_y += 2
    on_draw.wide_reciever_2_x += -5
    on_draw.wide_reciever_2_y += .2


on_draw.defensive_tackle_x = 100
on_draw.defensive_ends_x = 100
on_draw.olb_1_x = 100
on_draw.olb_1_y = 0
on_draw.olb_2_x = 100
on_draw.olb_2_y = 0
on_draw.ilb_1_x = 100
on_draw.ilb_1_y = 0
on_draw.ilb_2_x = 100
on_draw.ilb_2_y = 0
on_draw.cb_1_x = 100
on_draw.cb_1_y = 0
on_draw.cb_2_x = 100
on_draw.cb_2_y = 0
on_draw.sf_1_x = 100
on_draw.sf_1_y = 0
on_draw.sf_2_x = 100
on_draw.sf_2_y = 0


on_draw.offensive_linemen_x = 100
on_draw.tight_end_x = 100
on_draw.tight_end_y = 0
on_draw.quarterback_x = 100
on_draw.quarterback_y = 0
on_draw.running_back_x = 100
on_draw.running_back_y = 0
on_draw.fullback_x = 100
on_draw.fullback_y = 0
on_draw.wide_reciever_1_x = 100
on_draw.wide_reciever_1_y = 0
on_draw.wide_reciever_2_x = 100
on_draw.wide_reciever_2_y = 0


def main():
    """Draw the field"""
    arcade.open_window(740, 500, "Drawing Example")

    arcade.set_background_color(arcade.color.GRAY)

    arcade.schedule(on_draw, 1/60)

    arcade.run()
   


if __name__ == '__main__':
    main()