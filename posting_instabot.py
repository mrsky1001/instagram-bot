import secrets
from os import listdir
from os.path import join, isfile

from story_posted import get_story_posted, clear_story, add_story


def post_medias(bot, folder, count, caption):
    list_posted = get_story_posted()
    files = [f for f in listdir(folder) if isfile(join(folder, f))]

    files_to_post = []

    if len(list_posted) >= len(files):
        clear_story()

    for num in range(count):
        while True:
            file = secrets.choice(files)

            if file in list_posted:
                continue
            else:
                break

        files_to_post.append(file)

    for file in files_to_post:
        add_story(file)
        post(bot, path_to_image=folder + '/' + file, caption=caption)

    print('posted images: ')
    print(list_posted)
    print('selected images: ')
    print(files_to_post)


#
# def post_random(bot, folder):
#     list_posted = get_story_posted()
#     files = [f for f in listdir(folder) if isfile(join(folder, f))]
#
#     file = ''
#
#     if file in list_posted:
#         while file in list_posted and len(list_posted) < len(files):
#             file = secrets.choice(files)
#     else:
#         file = secrets.choice(files)
#
#     if len(list_posted) >= len(files):
#         clear_story()
#
#     add_story(file)
#     post(bot, path_to_image=folder + '/' + file)
#     print('posted images: ' + list_posted)
#     print('selected image: ' + join(folder + file))


def post(bot, path_to_image, caption):
    bot.upload_photo(photo=path_to_image, caption=caption)
