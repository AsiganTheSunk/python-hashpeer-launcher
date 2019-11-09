#!/usr/bin/env python

import sys
import getpass
import stem.connection
import stem.socket


from stem.control import Controller, Signal
import time
# from colorama import Fore, Style

DEFAULT_PROXY_PORT = 9050
DEFAULT_CNTRL_PORT = 9051
DEFAULT_TIME_OUT_RESET_THRESHOLD = 180
DEFAULT_RESET_THRESHOLD = 30
DEFAULT_CIRCUIT_HOPS = 'X'
LOCAL_HOST = '127.0.0.1'

# controller.set_conf("ExitNodes", "{" + country + "}")
# force circuit extension to provide n jumps if needed when the tor instance it's created.
# force exit policy to the socket to provide some security
# force country exit node policy to provide additional control over where you are hopping.
# Threaded in the future...

class TorInstance():
    def __init__(self, tor_instance_id, nickname, socks_port, cntrl_port, exit_policy, circuit_hops):
        self.tor_instance_id = tor_instance_id
        self.nickname = nickname
        self.cntrl_port = cntrl_port
        self.socks_port = socks_port
        self.proxy_ip = LOCAL_HOST

        # Advanced Parameters
        self.exit_policy = exit_policy
        self.country_list = 'ALL'
        self.circuit_hops = circuit_hops
        if circuit_hops is None:
            self.circuit_hops = DEFAULT_CIRCUIT_HOPS

        # Stem Cntrl
        try:
            control_socket = stem.socket.ControlPort(port=9051)
        except stem.SocketError as exc:
            print('Unable to connect to port 9051 (%s)' % exc)
            sys.exit(1)

        try:
            stem.connection.authenticate(control_socket)
        except stem.connection.IncorrectSocketType:
            print('Please check in your torrc that 9051 is the ControlPort.')
            print('Maybe you configured it to be the ORPort or SocksPort instead?')
            sys.exit(1)
        except stem.connection.MissingPassword:
            controller_password ='dummypass' #getpass.getpass('Controller password: ')

        try:
            stem.connection.authenticate_password(control_socket, password=controller_password)
        except stem.connection.PasswordAuthFailed:
            print('Unable to authenticate, password is incorrect')
            sys.exit(1)
        except stem.connection.AuthenticationFailure as exc:
            print('Unable to authenticate: %s' % exc)
            sys.exit(1)

        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password='dummypass')
            bytes_read = controller.get_info("traffic/read")
            bytes_written = controller.get_info("traffic/written")

            print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))

        # self.ctrl = Controller.from_port(port=
        # self.ctrl.authenticate(password=)

        # Circuit dirtyness 10min by default
        self.circuit_dirtyness = time.time()

        # Aditional Configuration. Even tho the circuits resets every 10min, we are gonna force a higher refresh if it's
        # needed or upon reaching the max number of connections per circuit that it's stablished by the attr connection_
        # reset_threshold

        self.time_out_reset_threshold = DEFAULT_TIME_OUT_RESET_THRESHOLD
        self.connection_reset_threshold = DEFAULT_RESET_THRESHOLD
        self.connection_count = 0



    def __str__(self):
        timer = time.time()
        return('TorInstance ID: %s\n Nickname: %s\n ProxyPort: %s, CntrlPort: %s\n Circuit Dirt: %s, Circuit Hops: %s\n ExitPolicy: {%s}\n'
               ' Country List: %s' % (
                   self.tor_instance_id, self.nickname, self.socks_port, self.cntrl_port, timer - self.circuit_dirtyness, self.circuit_hops, self.exit_policy,
                   self.country_list
        ))

    def get_proxy(self):
        return str(self.proxy_ip)+':'+str(self.socks_port)

    def add_connection_use_count(self):
        """Function

            Attributes:
            """
        self.connection_count = self.connection_count + 1
        return

    def build_circuit(self):
        """Function

            Attributes:
            """
        #add the needed hops
        return

    def reset(self):
        """Function

        Attributes:
        """
        try:
            print('TorPyCurl Status: Connection Reset ExitRelay')
            self.ctrl.signal(Signal.NEWNYM)
        except:
            print('An error occurred: ')

