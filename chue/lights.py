#!/usr/local/bin/python3
"""
CLI module to control philips hue lights.
"""
import phue
import fire


# BRIDGE_IP = "10.0.1.47"

class Light(object):

    def __init__(self):
        self._bridge = None
        self.connect()

    def _log(self, *args, **kwargs):
        print(args, kwargs)

    def connect(self, ip=None, username=None, config_file_path=None):
        ip = '10.0.1.6'
        username='newdeveloper'
        self._bridge = phue.Bridge(ip=ip, username=username, config_file_path = config_file_path)
        self._bridge.connect()
        self._log(self._bridge.config_file_path)

    def _action_on_light_by_id(self, light_id, action):
        """
        Action on one light by light_id.
        """
        if action == 'on': self._bridge.set_light(light_id, 'on', True)
        else:  self._bridge.set_light(light_id, 'on', False)
        self._log('Turning %s light %s' % (action, light_id))

        return

    def _action_on_group_of_lights(self, lights, action):
        """
        Action on group of lights.
        """
        for l in lights:
            if action == 'on': self._action_on_light_by_id(l.light_id, 'on' )
            else : self._action_on_light_by_id(l.light_id, 'off' )

        return

    def on(self, id=None):
        if id:
            l = int(id )
            self._action_on_light_by_id(l, 'on' )
        else:
            self._action_on_group_of_lights(self._bridge.lights, 'on' )


    def off(self, id = None):
        if id:
            l = int(id)
            self._action_on_light_by_id(l, 'off' )
        else:
            for l in self._bridge.lights:
                self._action_on_light_by_id(l.light_id, 'off' )

    def status(self, id=None):
        if id:
            self._log(self._bridge[id].on)



if __name__ == '__main__':
    fire.Fire(Light)
