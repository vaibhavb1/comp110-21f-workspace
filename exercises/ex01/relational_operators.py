"""This program uses relational operators and gives the boolian value of the relations between the integers entered."""

__author__ = "730481030"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

less_than_answer: bool = left_hand_side < right_hand_side
at_least_answer: bool = left_hand_side >= right_hand_side
equal_answer: bool = left_hand_side == right_hand_side
not_equal_answer: bool = left_hand_side != right_hand_side

print(str(left_hand_side) + " < " + str(right_hand_side) + " is " + str(less_than_answer))
print(str(left_hand_side) + " >= " + str(right_hand_side) + " is " + str(at_least_answer))
print(str(left_hand_side) + " == " + str(right_hand_side) + " is " + str(equal_answer))
print(str(left_hand_side) + " != " + str(right_hand_side) + " is " + str(not_equal_answer))
