import hashlib

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import xml.etree.ElementTree as ET

from vicky.models import Alert

NS = {
    'cap': 'urn:oasis:names:tc:emergency:cap:1.2'
}


def index():
    return render_to_response('vicky/index.html')


@csrf_exempt
def alerts(req):
    if not req.method in ['POST', 'PUT']:
        return HttpResponse(status=405)

    # Check if we have seen this once before
    summer = hashlib.sha1()
    summer.update(req.body)
    message_sha1sum = summer.hexdigest()
    print('message_sha1sum: ' + message_sha1sum)

    try:
        existing_alert = Alert.objects.get(message_sha1sum=message_sha1sum)
        if existing_alert:
            print('alert with identifier %s already presented and saved' % existing_alert.alert_id)
            existing_alert.save()
            return HttpResponse(status=202)
    except ObjectDoesNotExist:
        print('alert does not exists in database')

    message_xml = req.body.decode('utf-8')
    print('message_xml: ' + message_xml)


    root = ET.fromstring(message_xml)
    alert_id = root.find('cap:identifier', NS).text
    print('alert_id: ' + alert_id)

    alert = Alert()
    alert.alert_id = alert_id
    alert.message_sha1sum = message_sha1sum
    alert.message_xml = message_xml
    alert.save()

    return HttpResponse(status=201)
