from FeedbackPrinter import FeedbackPrinter
from LCSTestCase import LCSTestCase

test_feedback = FeedbackPrinter()
test_cases = [
    LCSTestCase(
        "ALASKAN",
        "BANANAS",
        { "AAA", "AAS", "AAN" },
        [
            # B  A  N  A  N  A  S
            [ 0, 1, 1, 1, 1, 1, 1 ], # A
            [ 0, 1, 1, 1, 1, 1, 1 ], # L
            [ 0, 1, 1, 2, 2, 2, 2 ], # A
            [ 0, 1, 1, 2, 2, 2, 3 ], # S
            [ 0, 1, 1, 2, 2, 2, 3 ], # K
            [ 0, 1, 1, 2, 2, 3, 3 ], # A
            [ 0, 1, 2, 2, 3, 3, 3 ]  # N
        ]
    ),
    LCSTestCase(
        "BAAB",
        "ABBA",
        { "AA", "BB", "AB", "BA" },
        [
            # A  B  B  A
            [ 0, 1, 1, 1 ], # B
            [ 1, 1, 1, 2 ], # A
            [ 1, 1, 1, 2 ], # A
            [ 1, 2, 2, 2 ]  # B
        ]
    ),
    LCSTestCase(
        "ABBA",
        "BAAB",
        { "AA", "BB", "AB", "BA" },
        [
            # B  A  A  B
            [ 0, 1, 1, 1 ], # A
            [ 1, 1, 1, 2 ], # B
            [ 1, 1, 1, 2 ], # B
            [ 1, 2, 2, 2 ]  # A
        ],
    ),
    LCSTestCase(
        "lower case",
        "UPPER CASE",
        { " " },
        [
            # U  P  P  E  R     C  A  S  E
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # l
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # o
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # w
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # e
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], # r
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], #
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], # c
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], # a
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ], # s
            [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1 ]  # e
        ],
    ),
    LCSTestCase(
        "PROGRAMMING",
        "PROBLEM",
        { "PROM" },
        [
            # P  R  O  B  L  E  M
            [ 1, 1, 1, 1, 1, 1, 1 ], # P
            [ 1, 2, 2, 2, 2, 2, 2 ], # R
            [ 1, 2, 3, 3, 3, 3, 3 ], # O
            [ 1, 2, 3, 3, 3, 3, 3 ], # G
            [ 1, 2, 3, 3, 3, 3, 3 ], # R
            [ 1, 2, 3, 3, 3, 3, 3 ], # A
            [ 1, 2, 3, 3, 3, 3, 4 ], # M
            [ 1, 2, 3, 3, 3, 3, 4 ], # M
            [ 1, 2, 3, 3, 3, 3, 4 ], # I
            [ 1, 2, 3, 3, 3, 3, 4 ], # N
            [ 1, 2, 3, 3, 3, 3, 4 ]  # G
        ],
    ),
    LCSTestCase(
        "LOOK",
        "ZYBOOKS",
        { "OOK" },
        [
            # Z  Y  B  O  O  K  S
            [ 0, 0, 0, 0, 0, 0, 0 ], # L
            [ 0, 0, 0, 1, 1, 1, 1 ], # O
            [ 0, 0, 0, 1, 2, 2, 2 ], # O
            [ 0, 0, 0, 1, 2, 3, 3 ]  # K
        ],
        True
    ),
    LCSTestCase(
        "ZYBOOKS",
        "LOOK",
        { "OOK" }
    ),
    LCSTestCase(
        "A_B_C",
        "X_Y_Z",
        { "__" }
    ),
    LCSTestCase(
        "ABCEDEFGHIJKL",
        "MNOPQRSTUVWXYZ",
        set()
    ),
    LCSTestCase(
        "DATA STRUCTURES",
        "ALGORITHMS",
        { "ARTS" }
    ),
    LCSTestCase(
        "",
        "",
        set()
    ),
    LCSTestCase(
        "RELATIVELY",
        "ACTIVE",
        { "ATIVE" }
    ),
    LCSTestCase(
        "ACTIVE",
        "RELATIVELY",
        { "ATIVE" }
    ),
    LCSTestCase(
        "very very very very very very very very very long string",
        "short string",
        { "o string", "r string" }
    ),
    LCSTestCase(
        "five food groups",
        "dairy, vegetables, fruits, grains, and protein",
        { "ive f grp", "ive fd ro", "ive f gro", "ive f grs" }
    ),
    LCSTestCase(
        "A MAN A PLAN A CANAL PANAMA",
        "THE RAIN IN SPAIN STAYS MAINLY IN THE PLAIN",
        { " AN  PAN A ANL PAN" }
    )
]
# Execute each test case and count the number that pass
pass_count = 0;
for test_case in test_cases:
    if test_case.execute(test_feedback):
        pass_count += 1

# Print the summary
print(f"{pass_count} of {len(test_cases)} test cases passed")
