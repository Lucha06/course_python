# Hurdle 1
# move()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()
# turn_left()
# turn_left()
# turn_left()
# move()

# Hurdle 2
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def perform_moves():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# perform_moves()

# Hurdle 3
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def pass_wall():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while at_goal() == False:
#     if wall_in_front():
#         pass_wall()
#     elif not wall_in_front():
#         move()

# Hurdle 4
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def pass_wall():
#     turn_left()
#     count_wall = 0
#     while wall_on_right():
#         count_wall += 1
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while count_wall > 0:
#         move()
#         count_wall -= 1
#     turn_left()
#
#
# while at_goal() == False:
#     if wall_in_front():
#         pass_wall()
#     else:
#         move()

# Maze
# def left_3():
#     counter = 3
#     while counter > 0:
#         turn_left()
#         counter -= 1
#
#
# while not at_goal():
#     while is_facing_north() and not at_goal():
#         if not wall_in_front():
#             move()
#         elif wall_in_front() and wall_on_right():
#             turn_left()
#             if wall_in_front() and wall_on_right():
#                 turn_left()
#             else:
#                 move()
#         elif wall_in_front() and not wall_on_right():
#             left_3()
#
#     while not is_facing_north() and not at_goal():
#         if not wall_in_front() and not wall_on_right():
#             move()
#         elif not wall_on_right() and wall_in_front():
#             left_3()
#         elif wall_on_right() and not wall_in_front():
#             turn_left()
#             if wall_in_front():
#                 left_3()
#                 move()
#             else:
#                 move()
#         elif wall_in_front() and not wall_on_right():
#             turn_left()
#         elif wall_on_right and wall_in_front():
#             turn_left()
#             if not wall_in_front():
#                 move()