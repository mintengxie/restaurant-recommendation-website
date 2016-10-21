import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

if django.VERSION >= (1, 7):
    django.setup()

def main():
    from website.models.models import User_yelp

    f = open('/Users/apple/PycharmProjects/mysite/website/Database/user.txt')

    List = []
    for line in f:
        parts = line.split('___')
        List.append(User_yelp(user_id=parts[0], name=parts[1],
                              review_count=parts[2]))
    f.close()

    User_yelp.objects.bulk_create(List)


if __name__ == "__main__":
    main()
    print('Done!')