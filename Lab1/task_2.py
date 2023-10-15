# TODO Найдите количество книг, которое можно разместить на дискете

INFORMATION_VOLUME = 1.44 * 1024 * 1024  # объем дискеты
NUMBER_OF_PAGES = 100
NUMBER_OF_STRINGS = 50
NUMBER_OF_SYMBOLS = 25
VOLUME_OF_SYMBOL = 4

volume_of_book = NUMBER_OF_SYMBOLS * NUMBER_OF_STRINGS * NUMBER_OF_PAGES * VOLUME_OF_SYMBOL
number_of_books = round(INFORMATION_VOLUME / volume_of_book)

print("Количество книг, помещающихся на дискету:", number_of_books)
