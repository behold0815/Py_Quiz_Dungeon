import numpy as npy
import json

Quiz = [
    {"Question":"1+1=","Answer":2},
    {"Question":"5+1=","Answer":6},
    {"Question":"3+1=","Answer":4},
    {"Question":"11+1=","Answer":12}
]

# a Directions Heads Up
aDirectionsHeadsUp = [
    {"Left":"Your left is "},
    {"Right":"Your right is "},
    {"Front":"Your front is "},
    {"Back":"You have back to the original path "},
]

# a Environment Heads Up
aEnvironmentHeadsUp = [
    {"0":"wall that you cannot pass. "},
    {"1":"a path that you can pass. "},
    {"2":"the exit that means you passed the Quiz journey. "},
    {"Q":"a question you need to solve. "}
]

Q1 = json.dumps(Quiz[0])
Q2 = json.dumps(Quiz[1])
Q3 = json.dumps(Quiz[2])
Q4 = json.dumps(Quiz[3])

# dungeon layout
dungeon = npy.array(
    [Q1, 1, Q2, 1, Q3, 1, 1, Q4, 2,]
 )
# dungeon = npy.array(
#     [[Q1, 1, 1, 0, 0, 1, 0, 0, 0,],
#     [1, 0, 1, 0, 0, 1, 0, 1, 0,],
#     [1, 1, 1, 0, 0, 1, 0, 1, 0,],
#     [0, 1, Q2, 1, 1, 1, 1, 1, 2,],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0,],
#     [0, 1, 0, 1, Q4, 1, 1, 1, 0,],
#     [0, 1, 0, 1, 0, 1, 0, 0, 0,],
#     [0, 1, 0, 1, 0, 1, 0, 2, 0,],
#     [0, 1, Q3, 1, 0, 1, 1, 1, 0]]
#  )
