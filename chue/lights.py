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

    def action_on_light_by_id(self, light_id, action):
        """
        Action on one light by light_id.
        """
        if action == 'on': self.bridge.set_light(light_id, 'on', True)
        else:  self.bridge.set_light(light_id, 'on', False)

        return

    def action_on_group_of_lights(self, lights, action):
        """
        Action on one light by light_id.
        """
        for l in lights:
            if action == 'on':
               self.bridge.set_light(l.light_id, 'on', True)
            else : self.bridge.set_light(l.light_id, 'on', False)

        return

    def on(self, light_id=None):
        if light_id:
            l = int(light_id )
            self.action_on_light_by_id(l, 'on' )
            self.print('Turning on light %s: Status ' % (l))
        else:
            self.print('Turning on all lights')
            for l in self.bridge.lights:
                self.action_on_light_by_id(l.light_id, 'on' )

    def off(self, light_id = None):
        if light_id:
            l = int(light_id)
            self.print('Turning off light %s' % l)
            self.action_on_light_by_id(l, 'off' )
        else:
            self.print('Turning off all lights')
            for l in self.bridge.lights:
                self.action_on_light_by_id(l.light_id, 'off' )


if __name__ == '__main__':
    fire.Fire(Light)
