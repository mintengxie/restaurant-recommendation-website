from website.models.models import *
import pandas
from pandas import DataFrame
def get_similar_user(user1):
    # find the top restaurant this user like
    review=Review.objects.filter(user_id=user1)
    like_r=[]
    for r in review:
        if float(r.star)>=4:
            like_r.append(r.business_id)
    # find the top similar user who like those restaurant
    x=[]
    for r in like_r:
        user=Review.objects.filter(business_id=r)
        for u in user:
            if u.user_id==user1:
                continue
            if float(u.star)>3:
                x.append(u.user_id)
    if len(x)==0:
        return []
    like_u = DataFrame(x)
    like_u.columns = ['id']
    like_u['Similar_Level'] = 1
    similar_users = like_u.groupby('id')
    similar_users = similar_users.count().reset_index()
    similar_users = similar_users.sort(columns='Similar_Level', ascending=False).reset_index()
    del similar_users['index']
    return similar_users


def get_name_of_restaurant(id):
    try:
        return Business.objects.get(business_id=id).name
    except:
        return "Cannot find"
def get_name_of_user(id1):
    try:
        return User_yelp.objects.get(user_id=id1).name
    except :
        return 'Cannot find'

def adjust1(df):
    x=[]
    rate = 10.0 / df['Recommend_Level'][0]
    for i in range(len(df)):
        level=int(df['Recommend_Level'][i]*rate)
        if level<1:
            level=1
        x.append([df['id'][i],get_name_of_restaurant(df['id'][i]),level])
    df1=DataFrame(x)
    df1.columns=['id','name','Recommend_Level']
    return df1
def adjust(df):
    x=[]
    rate = 10.0 / df['Similar_Level'][0]
    for i in range(len(df)):
        level = int(df['Similar_Level'][i] * rate)
        if level<1:
            level=1
        x.append([df['id'][i],get_name_of_user(df['id'][i]), level])
        #df['Similar_Level'][i]=level
    df1=DataFrame(x)
    df1.columns=['id','name','Similar_Level']
    return df1
#find the top restaurant you may like
def get_restaurant(similar_users):
    top_similar_user=similar_users.head(int(len(similar_users)*0.7))
    x=[]
    for u in top_similar_user['id'].tolist():
        rr=Review.objects.filter(user_id=u)
        for r in rr:
            if int(r.star)>3:
                x.append(r.business_id)
    if len(x)==0:
        return []
    restaurant = DataFrame(x)
    restaurant.columns = ['id']
    restaurant['Recommend_Level'] = 1
    R_you_may_like = restaurant.groupby('id')
    R_you_may_like = R_you_may_like.count().reset_index()
    R_you_may_like = R_you_may_like.sort(columns='Recommend_Level', ascending=False).reset_index()
    del R_you_may_like['index']
    return R_you_may_like

