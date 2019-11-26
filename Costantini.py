from Book import Book

la_canzone_dei_soldi = Book("La canzone da sei soldi ","A. J. Cronin","Bompiani",1965 , 373, "IT\\ICCU\\LIA\\0032849")
la_camera_cinese = Book("La camera cinese", "Vivian Connell", "Garzanti", 1965, 303, "IT\\ICCU\\SBL\\0553196")

books = [la_canzone_dei_soldi, la_camera_cinese]
def get_books_list():
    return books
