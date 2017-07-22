from pprint import pprint

from django.shortcuts import render, render_to_response

from vicky import cap_api


def _parse_point(p):
    return list(map(float, p.split(',')))


def _parse_polygon(ps):
    points = ps.split()
    return list(map(_parse_point, points))


def index(req):
    from vicky.models import Alert
    vicky_alerts = Alert.objects.order_by('-message_received')[:100]
    alerts = []
    for vicky_alert in vicky_alerts:
        cap_alert = cap_api.parseString(vicky_alert.message_xml.encode('utf-8'), silence=True)
        for info in cap_alert.get_info():
            if info.get_language().startswith('sv'):
                headline = info.get_headline()
                senderName = info.get_senderName()
                description = info.get_description()
                polygons = list(map(_parse_polygon, info.get_area()[0].get_polygon()))
                print(polygons)
                alert = {
                    'id': vicky_alert.id,
                    'headline': headline,
                    'senderName': senderName,
                    'description': description,
                    'polygons': polygons,
                }
                pprint(alert)
                alerts.append(alert)

    context = {'alerts': alerts}
    return render_to_response('front/index.html', context)
