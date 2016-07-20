import json
import base64

from getpass import getpass

from bot import Bot
from schedulers import RandomizedTaskScheduler
from utils.auth import PtcAuth
from utils.rpc_client import RpcClient
from utils.structures import Player
from utils.pgoexceptions import AuthenticationException, RpcException
import geopy
from geopy.geocoders import GoogleV3


def writeSettings(settings):
    with open('settings.json', 'w') as outfile:
        json.dump(settings, outfile)

if __name__ == '__main__':
    try:
        with open('settings.json') as file:
            settings = json.load(file)
    except IOError as error:
        provider = raw_input('Which login provider do you want to '
                'use (google/ptc)? [ptc]: ') or 'ptc'

        username = raw_input('Username: ')
        password = getpass()
        location = raw_input('Where do you want to spawn? '
                             '[New York, NY, USA]: ') or 'New York, NY, USA'
        settings["username"] = username;
        settings["password"] = password;
        settings["location"] = location;
        settings["provider"] = provider;

    writeSettings(settings);

    login_type = {
        'google': None,
        'ptc': PtcAuth
    }[settings["provider"]]

    try:
        if "latitude" in settings:
            position = geopy.point.Point(latitude = settings["latitude"], longitude = settings["longitude"], altitude = settings["altitude"])
        else:
            geolocator = GoogleV3()
            position = geolocator.geocode(settings["location"])
            settings["latitude"] = position.latitude;
            settings["longitude"] = position.longitude;
            settings["altitude"] = position.altitude;
            writeSettings(settings);
        player = Player(position.latitude, position.longitude, position.altitude)
        rpc = RpcClient(player)

        if "ticket" in settings:
            from POGOProtos.Networking.Envelopes.AuthTicket_pb2 import AuthTicket
            ticket = AuthTicket();
            ticket.ParseFromString(base64.b64decode(settings["ticket"]))
            rpc.setTicket(ticket);
        else:
            login_session = login_type()
            if login_session.login(settings["username"], settings["password"]):
                if rpc.authenticate(login_session):
                    print "[RPC] Authenticated"
                    settings["ticket"] = base64.b64encode(rpc.getTicket().SerializeToString());
                    writeSettings(settings);
                else:
                    print "[RPC] Failed to authenticate"
            else:
                print "[LOGIN] Login failed, check your username and password"

        if rpc.isauthenticated:
            scheduler = RandomizedTaskScheduler()
            bot = Bot(rpc, scheduler)

    except AuthenticationException as error:
        print(error)
    except RpcException as error:
        print(error)
    except ValueError as error:
        print(error)
        exit(1)
