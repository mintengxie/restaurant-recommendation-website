import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

if django.VERSION >= (1, 7):
    django.setup()

def main():
    from website.models.models import Review

    f = open('/Users/apple/PycharmProjects/mysite/website/Database/review.txt')

    List = []
    for line in f:
        parts = line.split('___')
        List.append(Review(user_id=parts[0], business_id=parts[1],
                           star=parts[2], date=parts[3]))
    f.close()

    Review.objects.bulk_create(List)


if __name__ == "__main__":
    main()
    print('Done!')