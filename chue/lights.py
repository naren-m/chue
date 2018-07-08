#!/usr/local/bin/python3
"""
CLI module to control philips hue lights.
"""
import phue
import fire


BRIDGE_IP = "10.0.1.47"
# BRIDGE_IP = "10.0.1.6"

class Light(object):

    def __init__(self):
        self.bridge = phue.Bridge(BRIDGE_IP)
        self.bridge.connect()
        phue.logger.propagate = False
        phue.logger.disabled = False

    def print(self, *args, **kwargs):
        print(*args, **kwargs)

    def _action_on_light_by_id(self, light_id, action):
        """
        Action on one light by light_id.
        """
        if action == 'on': self.bridge.set_light(light_id, 'on', True)
        else:  self.bridge.set_light(light_id, 'on', False)
        self.print('Turning %s light %s' % (light_id , action))

        return

    def _action_on_group_of_lights(self, lights, action):
        """
        Action on group of lights.
        """
        for l in lights:
            if action == 'on': self.bridge.set_light(l.light_id, 'on', True)
            else : self.bridge.set_light(l.light_id, 'on', False)

        return

    def on(self, id=None):
        if id:
            l = int(id )
            self._action_on_light_by_id(l, 'on' )
        else:
            self.print('Turning on all lights')
            self._action_on_group_of_lights(self.bridge.lights, 'on' )


    def off(self, id = None):
        if id:
            l = int(id)
            self._action_on_light_by_id(l, 'off' )
        else:
            self.print('Turning off all lights')
            for l in self.bridge.lights:
                self._action_on_light_by_id(l.light_id, 'off' )


if __name__ == '__main__':
    fire.Fire(Light)
