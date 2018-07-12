#!/usr/local/bin/python3
"""
CLI module to control philips hue lights.
"""
import phue
import fire


BRIDGE_IP = "10.0.1.47"

class Light(object):

    def __init__(self):
        self._bridge = phue.Bridge(BRIDGE_IP)
        self._bridge.connect()

    def _log(self, *args, **kwargs):
        print(args, kwargs)

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
            self.brid



if __name__ == '__main__':
    fire.Fire(Light)
