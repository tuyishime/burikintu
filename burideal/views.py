# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from burideal.models import *
import urllib
import urllib2 

MSG1 = 'Urakoze kumenyekanisha ibintu byawe kuri Burikintu! Turakomesha tubashakire abakiliya'
MSG2 = 'Mushobora kuba mwanditse nabi!' 


def home(request):
    output = u'''
      <html> 
        <head><title>%s</title></head> 
        <body> 
         <h1>%s</h1><p>%s</p> 
        </body> 
       </html>
     ''' % (
         u'Burikintu', 
         u'Urakaza neza kuri Burikintu', 
         u'Ushobora gushyira cg gushaka ikintu cyose ushaka hano'
     )
    return HttpResponse(output) 

@csrf_exempt
def postDeal(request): 
    text = request.GET['text'].lower() 
    number = request.GET['number'] 
    endpoint = request.GET['endpoint'].lower()
    
    # Parse the message
    requestParts = text.split(' ')
    

    objectType = requestParts[1]
    if objectType == 'inzu':
        house = House(number=number, 
                      location=requestParts[2],  
                      price=requestParts[3], 
                      size=requestParts[4],
                      action=endpoint
        )
        if len(requestParts) > 5: 
            house.description = requestParts[5]
        #house.save()
        return HttpResponse(sendResponse(endpoint, number, MSG1))
    elif objectType == 'imodoka': 
        car = Car(number=number, 
                  ctype=requestParts[2], 
                  price=requestParts[3], 
                  action=endpoint
            )
           # car.save()
        if len(requestParts) > 4: 
            car.description = requestParts[4]
        return HttpResponse(sendResponse(endpoint, number,MSG1))
    else: 
        if objectType != '':
            deal = Deal(number=number, 
                        name=requestParts[1], 
                        price=requestParts[2], 
                        action=endpoint) 
            if len(requestParts) > 3: 
                deal.description = requestParts[3]
            #deal.save()
            return HttpResponse(sendResponse(endpoint, number, MSG1))
        else: 
            return HttpResponse('Oups, something went wrong')


def sendResponse(endpoint, number, msg):
    password = '221152355'
    url = 'https://www.sawanet.com/rsms/send?'
    query = {} 
    query['endpoint'] = endpoint 
    query['number'] = number 
    query['text'] = msg 
    query['password'] = password
    data = urllib.urlencode(query)
    #url = url + 'endpoint=' + endpoint 
    #url = url + '&number=' + number 
    #url = url + '&text=' + msg 
    #url = url + '&password=' + password
    #urltest = 'http://www.sawanet.com/rsms/send?endpoint=gukodesha&number=250788123123&text=test+message&password=221152355'
    url = url + data
    try: 
        req = urllib2.Request(url) 
        res = urllib2.urlopen(req) 
    except urllib2.HTTPError, e:
        return 'Error'
    return res.code
    
        

    
