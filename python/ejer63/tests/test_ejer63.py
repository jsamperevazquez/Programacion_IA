from ejer63 import UserDlib

user = UserDlib("../imaxes/bruce.jpeg", "Bruce Dickinson")


def test_create_user_dlib():
    assert "../imaxes/bruce.jpeg" == user.img_uri
    assert "Bruce Dickinson" == user.user_name


def test_create_new_register():
    user.create_table_image_name(user.img_uri, user.user_name)
