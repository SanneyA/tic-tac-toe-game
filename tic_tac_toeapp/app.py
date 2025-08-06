import streamlit as st

# Initialize session state variables
if "board" not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.game_over = False

def check_winner(board, player):
    # Rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def reset_game():
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.game_over = False

st.title("🎮 Tic Tac Toe Game")

# Show board with buttons
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        if cols[j].button(st.session_state.board[i][j] or " ", key=f"{i}-{j}", use_container_width=True):
            if st.session_state.board[i][j] == "" and not st.session_state.game_over:
                st.session_state.board[i][j] = st.session_state.current_player
                if check_winner(st.session_state.board, st.session_state.current_player):
                    st.session_state.winner = st.session_state.current_player
                    st.session_state.game_over = True
                elif is_full(st.session_state.board):
                    st.session_state.winner = "Draw"
                    st.session_state.game_over = True
                else:
                    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

# Display game status
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.success("🤝 It's a Draw!")
    else:
        st.success(f"🎉 Player {st.session_state.winner} Wins!")
else:
    st.info(f"Player {st.session_state.current_player}'s Turn")

# Reset button
st.button("🔄 Restart Game", on_click=reset_game)
