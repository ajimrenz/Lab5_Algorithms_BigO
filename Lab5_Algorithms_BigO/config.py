LAST_NAME = "Agawa"
STUDENT_ID = "TUPM-26-1082"
FAVORITE_ARTIST = "Juan Karlos"

_digits = [int(c) for c in STUDENT_ID if c.isdigit()]
_letters = [c for c in FAVORITE_ARTIST.upper() if c.isalpha()]

SEED_DIGIT = _digits[-1]
ID_SUM = sum(_digits)
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(c) - 64 for c in _letters)


def show_inputs():
    print("=== STUDENT INPUTS ===")
    print(f"LAST_NAME={LAST_NAME}  STUDENT_ID={STUDENT_ID}  FAVORITE_ARTIST={FAVORITE_ARTIST}")
    print(f"SEED_DIGIT={SEED_DIGIT}  ID_SUM={ID_SUM}  NAME_LENGTH={NAME_LENGTH}  "
          f"ARTIST_LENGTH={ARTIST_LENGTH}  ARTIST_SUM={ARTIST_SUM}\n")