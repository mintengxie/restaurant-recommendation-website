import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

if django.VERSION >= (1, 7):
    django.setup()

def main():
    from website.models.models import Business

    f = open('/Users/apple/PycharmProjects/mysite/website/Database/business.txt')

    List = []
    for line in f:
        parts = line.split('___')
        List.append(Business(business_id=parts[0], name=parts[1],
                             city=parts[2], review_count=parts[3],star=parts[4]))
    f.close()

    Business.objects.bulk_create(List)


if __name__ == "__main__":
    main()
    print('Done!')