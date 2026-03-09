def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200
    # if its not matching, just use normal range so app dont crash
    return 1, 100
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # if nothing typed, ask again
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()
    if raw == "":
        return False, None, "Enter a guess."
   
    # i blocked decimals so game is more simple and fair
    if "." in raw:
        return False, None, "Please enter a whole number."

    try:
        value = int(raw)
    except ValueError:
        return False, None, "That is not a number."

    return True, value, None
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # if guess bigger then secret, player needs to go lower
    if guess == secret:
        return "Win", "Correct!"
    # otherwise guess is lower, so player go higher
    if guess > secret:
        return "Too High", "Go LOWER!"
    return "Too Low", "Go HIGHER!"
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # less points if took too many attemps
        points = 100 - (10 * attempt_number)
        return current_score + max(points, 10)
    
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    
    # if weird outcome, just keep score same
    return current_score
    # raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
