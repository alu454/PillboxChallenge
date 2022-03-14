from pyfirmata import Arduino, util, STRING_DATA
import requests, time
board = Arduino('COM6')

def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )
    else:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( ' ' ) )

def load():
    msg('Atualizando...')
    rio = requests.get('http://api.hgbrasil.com/weather/?format=json&cid=BRXX0201')
    rio_json = rio.json()['results']
    msg('Carregou')
    screens = [
    [ rio_json['city_name'], rio_json['date'] + ' ' + rio_json['temp'] + 'C' ],
    [ rio_json['city_name'], rio_json['description'] ],
    [ rio_json['city_name'], 'Min:'+rio_json['forecast'][0]['min']+'C Max:' + rio_json['forecast'][0]['max'] + 'C' ],
    [ rio_json['city_name'], 'Vento:'+rio_json['wind_speedy'] ],
    [ rio_json['city_name'], 'Humidade:' + rio_json['humidity'] + '%' ],
    [ rio_json['forecast'][1]['weekday'] + ' ' +  rio_json['forecast'][1]['date'], rio_json['forecast'][1]['description'] ],
    [ rio_json['forecast'][1]['weekday'] + ' ' +  rio_json['forecast'][1]['date'], 'Min:'+rio_json['forecast'][1]['min']+'C Max:' + rio_json['forecast'][1]['max'] + 'C' ],
    [ rio_json['forecast'][2]['weekday'] + ' ' +  rio_json['forecast'][2]['date'], rio_json['forecast'][2]['description'] ],
    [ rio_json['forecast'][2]['weekday'] + ' ' +  rio_json['forecast'][2]['date'], 'Min:'+rio_json['forecast'][2]['min']+'C Max:' + rio_json['forecast'][2]['max'] + 'C'  ],
    [ rio_json['forecast'][3]['weekday'] + ' ' +  rio_json['forecast'][3]['date'], rio_json['forecast'][3]['description'] ],
    [ rio_json['forecast'][3]['weekday'] + ' ' +  rio_json['forecast'][3]['date'], 'Min:'+rio_json['forecast'][3]['min']+'C Max:' + rio_json['forecast'][3]['max'] + 'C'  ],
    [ 'Atualizado em', time.asctime()[:16] ]
    ]
    return screens

screens = load()
start_time = time.time()
while (True):
    time_now = time.time()
    if (time_now - start_time) > 1800.0:
        screens = load()
        start_time = time.time()
    for screen in screens:
        msg(screen[0])
        time.sleep(0.01)
        msg(screen[1])
        time.sleep(2)
