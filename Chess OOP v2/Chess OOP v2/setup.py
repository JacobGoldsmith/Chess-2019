import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]
list = ["black_king.png", "black_bishop.png", "black_queen.png", "black_rook.png", "black_knight.png", "black_pawn.png", "white_king.png", "white_queen.png", "white_rook.png", "white_bishop.png", "white_knight.png", "white_pawn.png"]
cx_Freeze.setup(
    name="YaakovsChess",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":list}},
    executables = executables

    )