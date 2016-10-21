import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django

if django.VERSION >= (1, 7):
    django.setup()

def main():
    from website.models.models import Checkin_analysis

    f = open('/Users/apple/PycharmProjects/mysite/website/Database/checkin.txt')

    List = []
    for line in f:
        parts = line.split('___')
        t1=list(parts[1].replace(',','').replace('[','').replace(']','').split())
        t2=list(parts[3].replace(',','').replace('[','').replace(']','').split())
        List.append(Checkin_analysis(business_id=parts[0], customer_flow=t1,
                                avg_rating=parts[2], avg_ratings=t2))
    f.close()

    Checkin_analysis.objects.bulk_create(List)


if __name__ == "__main__":
    main()
    print('Done!')