#!/usr/bin/env python

import random

import stem
import sys
from curlstem.struct_data.curlstem_tor_instance import TorInstance


# Imports Custom Logger & Logging Modules
from curlstem.logger.custom_logger import CustomLogger
from logging import INFO, DEBUG, WARNING
import logging
from random import randint

DEFAULT_ID = 0
DEFAULT_PROXY_PORT = 9050
DEFAULT_CNTRL_PORT = 9051
DEFAULT_INSTANCE_NICK_NAMES = ['Moctezuma', 'Catherine', 'Ghandi', 'Ragnar', 'Tokugawa', 'Sitting Bull',
                               'Joao II', 'Gengis Khan', 'Saladino']

DEFAULT_CONNECTION_USE_LIMIT = 1000
DEFAULT_PROXY_MODE = 'random'


class ProxyEngine():
    def __init__(self, logging_lvl=DEBUG):
        #  threading.Thread.__init__(self)
        self.tor_instance_list = []
        self.tor_last_connected = -1

        # Read from configuration file in the future
        self.tor_connection_limit = DEFAULT_CONNECTION_USE_LIMIT
        self.tor_instance_list.append(TorInstance(DEFAULT_ID, DEFAULT_INSTANCE_NICK_NAMES[0],
                                                  DEFAULT_PROXY_PORT, DEFAULT_CNTRL_PORT, None, None))

        self.tor_instance_counter = len(self.tor_instance_list) - 1
        self.proxy_connection_mode = DEFAULT_PROXY_MODE

        self.logger = CustomLogger(name=__name__, level=logging_lvl)

        # CustomLogger Format Definition
        formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)s]: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # Custom Logger File Configuration: File Init Configuration
        file_handler = logging.FileHandler('./curlstem/log/ProxyEngine.log', 'w')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level=logging_lvl)

        # Custom Logger Console Configuration; Console Init Configuration
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging_lvl)

        # Custom Logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        # self._propperties = {}

    def get_proxy_address(self):
        return {'tor_instance': str(self.get_tor_instance().get_proxy())}

    def __str__(self):
        # INSTANCE_HEADER = '\nPROXY_ROTATOR ( Instance )\n Number Of Instances: [ {0} ]\n Connection Mode: [ {1} ]\n'.format(self.tor_instance_counter + 1, self.proxy_connection_mode)
        result = '\nProxyRotator Instance\n Number of Instances: %s, Connection Mode: %s\n' %\
                 (self.tor_instance_counter +1, self.proxy_connection_mode)

        for item in self.tor_instance_list:
            result = result + '\n' + str(item) + '\n'
        return(result)

    def run(self):
        return

    def add_tor_instance(self, nickname, socks_port, cntrl_port, exit_policy, circuit_hops):
        """

        :param nickname: nickname of the Tor instance you have created, just an easter egg for now
        :param socks_port: socks5 connection port
        :param cntrl_port: cntrl connection port to manage tor over stem library
        :param exit_policy: allow, deny policy
        :param circuit_hops: number of hops in the tor circuit (future!!)
        :return:
        """
        if nickname is None:
            nickname = DEFAULT_INSTANCE_NICK_NAMES[self.tor_instance_counter + 1]
            self.tor_instance_list.append(TorInstance(self._new_tor_instance_id(), nickname, socks_port, cntrl_port,
                                                      exit_policy, circuit_hops))

        # eval if the instance it's actually running, and change the state acordingly if needed
        try:
            control_port = stem.socket.ControlPort(port=cntrl_port)
        except stem.SocketError as exc:
            print('Unable To Connect To Port {0} ( {1} )'.format(cntrl_port, exc))
            sys.exit(1)
        return

    def _new_tor_instance_id(self):
        """
        :return:
        """
        self.tor_instance_counter += 1
        return self.tor_instance_counter

    def get_tor_instance(self):
        """

        :return:
        """
        try:
            if self.proxy_connection_mode == 'sequential':
                tor_instance = self._sequential_tor_mode()
                self.eval_tor_instance(tor_instance)
                return tor_instance

            if self.proxy_connection_mode == 'random':
                tor_instance = self._random_tor_mode()
                self.eval_tor_instance(tor_instance)
                return tor_instance

        except:
            return

    def set_proxy_connection_mode(self, mode):
        """

        :param mode:
        :return:
        """
        self.proxy_connection_mode = mode

    def _random_tor_mode(self):
        """

        :return:
        """
        return random.choice(self.tor_instance_list)

    def add_last_connected_count(self):
        """

        :return:
        """
        self.tor_last_connected += 1

    def _sequential_tor_mode(self):
        """

        :return:
        """
        self.add_last_connected_count()
        result = self.tor_instance_list[self.tor_last_connected % (self.tor_instance_counter + 1)]
        return result

    def eval_tor_instance(self, tor_instance):
        """

        :param tor_instance:
        :return:
        """
        # if tor_instance.connection_count >= tor_instance.connection_reset_threshold:
        #     print('[ {0} ]: {1} - {2} TOR Circuit Should Reset Shortly ...'.format(tor_instance.nickname, tor_instance.socks_port, tor_instance.cntrl_port))
        #     tor_instance.reset()
        #     return False
        return True

    # def increment_connection_count(self, tor_instance_id):
    #     """
    #
    #     :param tor_instance_id:
    #     :return:
    #     """
    #     tor_instance = self.tor_instance_list[tor_instance_id]
    #     tor_instance.increment_connection_count()
    #     return