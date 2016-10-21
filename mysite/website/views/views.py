from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from website.models.models import *

def homepage(request):
    return render(request,'homepage.html')
def hello(request):
    # t=get_template('hello.html')
    # html=t.render()
    # return HttpResponse(html)
    return render(request, 'hello.html')
def project(request):
    return render(request, 'project.html')

def find(request):
    if 'name' in request.GET and (request.GET['name']):
        name=request.GET['name']
        ids=User_yelp.objects.filter(name__contains=name)
        if len(ids)==0:
            return render(request, 'project.html', {'not_find': True})
        return render(request, 'project.html', {'get_id':ids})
    elif 'name' in request.GET:
        return render(request, 'project.html', {'error1': True})
    else:
        return render(request, 'project.html')
def search(request):
    if 'q' in request.GET and (request.GET['q']):
        q=request.GET['q']
        Restaurant = Business.objects.filter(city=q)
        citys = Business.objects.filter(city__icontains=q.lower())
        temp=[]
        res=[]
        for c in citys:
            if c.city not in temp:
                temp.append(c.city)
                res.append(c)
        if len(Restaurant)==0:
            return render(request, 'search.html', {'Restaurant': Restaurant, 'query': q, 'City': res,'error2': True})
        temp1=[]
        for r in Restaurant:
            if float(r.star)>=4 and int(r.review_count)>100:
                temp1.append(r)
        if len(temp1)<10:
            temp1=Restaurant
        return render(request, 'search.html', {'Restaurant': Restaurant,'popular':temp1, 'query': q})
    else:
        return render(request, 'project.html', {'error2': True})

def recommend(request):
    if 'p' in request.GET and (request.GET['p']):
        p = request.GET['p']
        user = User_yelp.objects.filter(name=p)
        user1 = User_yelp.objects.filter(user_id=p)
        res = user or user1
        if len(res) == 0:
            return render(request, 'recommend.html', {'user': res, 'query': p, 'error3': True})
        ################
        if len(user1)==0:
            for i in user:
                temp=i.user_id
        else:
            temp=p
        restaurant=[]
        if len(get_similar_user(temp))==0:
            similar_user=[]
        else:
            temp1=get_similar_user(temp)
            similar_user=temp1.head()
            similar_user=adjust(similar_user)
            temp2=get_restaurant(temp1)
            restaurant=temp2.head()
            restaurant=adjust1(restaurant)

        x=[]
        for i in range(len(similar_user)):
            t=[]
            t.append(similar_user['id'][i])
            t.append(similar_user['name'][i])
            t.append(str(similar_user['Similar_Level'][i]))
            x.append(t)
        x1=[]
        for i in range(len(restaurant)):
            t=[]
            t.append(restaurant['id'][i])
            t.append(restaurant['name'][i])
            t.append(str(restaurant['Recommend_Level'][i]))
            x1.append(t)

        #################
        for i in res:
            res=i
        return render(request,'recommend.html',{'user': res,'query': p,'similar_user':x,'r':x1})
    else:
        return render(request, 'project.html', {'error3': True})


########################
#implement the recommendation algorithm
from .algorithm import *
########################