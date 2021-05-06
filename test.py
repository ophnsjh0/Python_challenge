"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

import os


def add_to_dict(e_dict, key, val=None):
    if str(type(e_dict)) == "<class 'str'>":
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif val == None:
        print("You need to send a word and a definition")
    elif key in list(e_dict):
        print("{1} is already on the dictionary. Won't add.".format(
            e_dict, key, val))
    else:
        e_dict[str(key)] = str(val)
        print("{1} has been added.".format(e_dict, key, val))


def get_from_dict(e_dict, key=None, val=None):
    if str(type(e_dict)) == "<class 'str'>":
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif key == None:
        print("You need to send a word to search for")
    elif key in list(e_dict):
        e_dict = e_dict
        print(e_dict)
    elif str(key) != list(e_dict):
        print("{1} was not found in this dict.".format(e_dict, key))


def update_word(e_dict, key, val=None):
    if str(type(e_dict)) == "<class 'str'>":
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif val == None:
        print("You need to send a word and a definition to update")
    elif key in e_dict:
        e_dict[str(key)] = str(val)
        print("{1} has been updated to: {2}".format(e_dict, key, val))
    elif str(key) != list(e_dict):
        print(
            "{1} is not on the dict. Can't update non-existing word.".format(e_dict, key, val))


def delete_from_dict(e_dict, key=None, val=None):
    if str(type(e_dict)) == "<class 'str'>":
        print("You need to send a dictionary. You sent: <class 'str'>")
    elif key == None and val == None:
        print("You need to specify a word to delete.")
    elif key in e_dict:
        del e_dict[key]
        print("{1} has been deleted.".format(e_dict, key, val))
    else:
        print("{1} is not in the dict. Won't delete".format(e_dict, key, val))


# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\


os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\
