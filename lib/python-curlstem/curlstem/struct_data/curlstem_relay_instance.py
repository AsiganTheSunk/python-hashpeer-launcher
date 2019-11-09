#!/usr/bin/env python

class RelayInstance:
    def __init__(self, nickname, fingerprint, address, or_port, exit_policy, protocols, observed_bandwidth='0 B',
                 exit_relay=False, country_instance=None, handshake_time='', handshake_validation=False):

        self.name = self.__class__.__name__

        # Relay Information
        self.nickname = nickname
        self.fingerprint = fingerprint
        self.address = address
        self.or_port = or_port
        self.country_instance = country_instance
        self.exit_relay = exit_relay
        self.handshake_time = handshake_time
        self.handshake_validation = handshake_validation

        # Exit Policies
        self.exit_policy = exit_policy

        # Protocol Information
        self.protocols = protocols

        # Average Bandwidth
        self.observed_bandwidth = observed_bandwidth

    def __str__(self):
        _str = '{0}:\n ## {1} ##\n' \
               '[ Fingerprint: {2} ] | [ Address:{3}:{4} ] | [  AverageBandwidth: {5}/s ] | [ ExitRelay: {6} ]\n' \
               ' - ExitPolicy: {7}\n, ' \
               ' - Protocols: {8}\n' \
               ' - Handshake_Time: {9}'.format(
                    self.name, self.nickname, self.fingerprint, self.address, self.or_port, self.observed_bandwidth,
                    self.exit_relay, self.exit_policy, self.protocols, self.handshake_time)
        return _str

