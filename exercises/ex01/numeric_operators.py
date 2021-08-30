"""This program shows the computations of two integers and gives the printed strings of the computations."""

__author__ = "730481030"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

exponent_answer: int = left_hand_side ** right_hand_side
division_answer: float = left_hand_side / right_hand_side
integer_division_answer: int = left_hand_side // right_hand_side
remainder_answer: float = left_hand_side % right_hand_side

print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(exponent_answer))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(division_answer))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(integer_division_answer))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(remainder_answer))