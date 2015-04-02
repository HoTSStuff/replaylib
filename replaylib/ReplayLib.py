"""A library for parsing Heroes of the Storm replays."""
from s2protocol.mpyq import mpyq
from s2protocol import protocol34784 as proto


class Replay(object):
    def __init__(self, replay_file):
        self.replay_file = replay_file
        self.archive = mpyq.MPQArchive(self.replay_file)

    def _get_header(self):
        contents = self.archive.header['user_data_header']['content']
        header = proto.decode_replay_header(contents)
        return header

    def _get_details(self):
        contents = self.archive.read_file('replay.details')
        return proto.decode_replay_details(contents)

    def _get_game_events(self):
        contents = self.archive.read_file('replay.game.events')
        return [event for event in
                proto.decode_replay_game_events(contents)]

    def _get_tracker_events(self):
        contents = self.archive.read_file('replay.tracker.events')
        return [event for event in
                proto.decode_replay_tracker_events(contents)]

    def get_deaths(self):
        events = self._get_tracker_events()
        death_event = ('NNet.Replay.Tracker.SUnitDiedEvent',)
        return self.filter_events(events, death_event)

    @staticmethod
    def filter_events(events, event_names):
        """Filter events given a tuple of a event types.

        :param events: Full list of event dictionaries
        :param event_names: a tuple of event names to filter on
        :return: a filtered event list containing only the specific events
        """
        return [event for event in events if event['_event'] in event_names]

    def get_players(self):
        details = self._get_details()
        player_list = details.get('m_playerList')
        return player_list

    def get_hotkey_presses(self):
        keys = ('NNet.Game.STriggerHotkeyPressedEvent',
                'NNet.Game.STriggerKeyPressedEvent')
        game_events = self._get_game_events()
        key_presses = [event for event in game_events
                       if event['_event'] in keys]
        return key_presses
