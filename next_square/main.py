def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return (int(sq ** 0.5)+ 1)**2 if sq ** 0.5 % 1 == 0 else -1